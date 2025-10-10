from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")
print("🍪 Loading Cookie Clicker...")

sleep(3)
try:
    driver.find_element(By.ID, "langSelect-EN").click()
    print("✅ English selected.")
    sleep(3)
except NoSuchElementException:
    print("⚠️ Language selection not found, continuing...")

cookie = driver.find_element(By.ID, "bigCookie")
print("🚀 Bot started! Clicking cookies non-stop...")

check_interval = 5
run_duration = 60 * 5
next_check = time() + check_interval
end_time = time() + run_duration

while True:
    cookie.click()

    if time() > next_check:
        try:
            cookies_text = driver.find_element(By.ID, "cookies").text
            cookies_count = int(cookies_text.split()[0].replace(",", ""))

            products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    product.click()
                    print(f"💰 Bought: {product.get_attribute('id')}")
                    break

        except Exception as e:
            print(f"⚠️ Error while buying: {e}")

        next_check = time() + check_interval

    if time() > end_time:
        try:
            final_cookies = driver.find_element(By.ID, "cookies").text
            print(f"\n🏁 Session complete! Final cookie count: {final_cookies}")
        except NoSuchElementException:
            print("❌ Couldn't fetch final cookie count.")
        break
