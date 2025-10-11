from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time

# ---------------- CONFIGURATION ---------------- #
ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={os.path.join(os.getcwd(), 'chrome_profile')}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)
wait = WebDriverWait(driver, 5)   


# ---------------- HELPER: RETRY ---------------- #
def retry(action, retries=7, description=""):
    """Try running an action several times if it times out."""
    for attempt in range(1, retries + 1):
        print(f"[{time.strftime('%H:%M:%S')}] Trying {description} (Attempt {attempt})")
        try:
            return action()
        except TimeoutException:
            if attempt == retries:
                raise
            time.sleep(1)


# ---------------- LOGIN FLOW ---------------- #
def login():
    """Logs into the gym website with stored credentials."""
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    email_box = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    email_box.clear()
    email_box.send_keys(ACCOUNT_EMAIL)

    password_box = driver.find_element(By.ID, "password-input")
    password_box.clear()
    password_box.send_keys(ACCOUNT_PASSWORD)

    driver.find_element(By.ID, "submit-button").click()
    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))


# ---------------- BOOKING ACTION ---------------- #
def book_class(button):
    """Clicks a booking/waitlist button and waits until its text updates."""
    button.click()
    wait.until(lambda d: button.text in ["Booked", "Waitlisted"])


# ---------------- START PROCESS ---------------- #
retry(login, description="Login")

booked_count = waitlist_count = already_booked_count = 0
processed_classes = []

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    day_section = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_section.find_element(By.TAG_NAME, "h2").text

    # Focus only on Tue/Thu 6 PM classes
    if any(day in day_title for day in ("Tue", "Thu")):
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            info = f"{class_name} on {day_title}"

            if button.text == "Booked":
                print(f"✓ Already booked: {info}")
                already_booked_count += 1
                processed_classes.append(f"[Booked] {info}")

            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {info}")
                waitlist_count += 1
                processed_classes.append(f"[Waitlisted] {info}")

            elif button.text == "Book Class":
                retry(lambda: book_class(button), description="Booking")
                print(f"✓ Successfully booked: {info}")
                booked_count += 1
                processed_classes.append(f"[New Booking] {info}")
                time.sleep(0.5)

            elif button.text == "Join Waitlist":
                retry(lambda: book_class(button), description="Waitlisting")
                print(f"✓ Joined waitlist for: {info}")
                waitlist_count += 1
                processed_classes.append(f"[New Waitlist] {info}")
                time.sleep(0.5)


# ---------------- VERIFY BOOKINGS ---------------- #
total_booked = booked_count + waitlist_count + already_booked_count
print(f"\n--- Total Tuesday/Thursday 6 PM classes: {total_booked} ---")
print("\n--- VERIFYING ON 'MY BOOKINGS' PAGE ---")

def get_my_bookings():
    """Navigate to 'My Bookings' and return the booking cards."""
    wait.until(EC.element_to_be_clickable((By.ID, "my-bookings-link"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))
    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
    if not cards:
        raise TimeoutException("No booking cards found – page may not have loaded")
    return cards

booking_cards = retry(get_my_bookings, description="Get My Bookings")

verified_count = 0
for card in booking_cards:
    try:
        when_text = card.find_element(By.XPATH, ".//p[strong[text()='When:']]").text
        if any(day in when_text for day in ("Tue", "Thu")) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        continue

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

input("\nPress Enter to close browser...")
driver.quit()
