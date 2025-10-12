from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

FB_EMAIL = "YOUR_FACEBOOK_EMAIL"
FB_PASSWORD = "YOUR_FACEBOOK_PASSWORD"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

driver.get("https://tinder.com/")
print("Opened Tinder.")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'I accept')]"))).click()
    print("✅ Cookies accepted.")
except:
    print("No cookie popup found or already accepted.")

try:
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Log in') or contains(text(),'Login')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", login_btn)
    time.sleep(1)
    login_btn.click()
    print("✅ Clicked login button.")
except Exception as e:
    print("❌ Could not click login button:", e)

time.sleep(3)

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'More options')]"))).click()
    print("✅ Clicked 'More options'.")
except:
    print("ℹ️ No 'More options' button, continuing...")

time.sleep(2)

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Facebook')]"))).click()
    print("✅ Clicked Facebook login.")
except Exception as e:
    print("❌ Facebook login not found:", e)

time.sleep(5)

try:
    base_window = driver.current_window_handle
    fb_window = [w for w in driver.window_handles if w != base_window][0]
    driver.switch_to.window(fb_window)
    print("🔄 Switched to Facebook window.")
except Exception as e:
    print("❌ Could not switch to Facebook window:", e)

try:
    email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
    pass_input = wait.until(EC.presence_of_element_located((By.ID, "pass")))
    email_input.send_keys(FB_EMAIL)
    pass_input.send_keys(FB_PASSWORD)
    pass_input.send_keys(Keys.ENTER)
    print("✅ Logged in to Facebook.")
except TimeoutException:
    print("❌ Facebook login fields not found (maybe already logged in).")

time.sleep(8)

try:
    driver.switch_to.window(base_window)
    print("🔁 Switched back to Tinder.")
except:
    print("⚠️ Could not switch back to Tinder, already in main window.")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Allow')]"))).click()
    print("✅ Allowed location.")
except:
    print("No location popup found.")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not interested') or contains(text(),'Later')]"))).click()
    print("✅ Dismissed notifications.")
except:
    print("No notification popup found.")

print("Starting auto-like...")
for i in range(20):
    time.sleep(1.5)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Like']"))).click()
        print(f"❤️ Liked profile #{i+1}")
    except Exception:
        print("Could not click like — retrying.")
        time.sleep(2)

print("🎯 Finished!")
