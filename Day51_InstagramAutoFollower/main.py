from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import dotenv_values
import time

# Load credentials
config = dotenv_values(".env")
SIMILAR_ACCOUNT = config.get("SIMILAR_ACCOUNT")
USERNAME = config.get("USERNAME")
PASSWORD = config.get("PASSWORD")


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        print("🔹 Logging in...")
        self.driver.get("https://www.instagram.com/accounts/login/")

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        try:
            cookie_btn = self.driver.find_element(
                By.XPATH, "//button[contains(text(),'Only allow essential cookies')]"
            )
            cookie_btn.click()
        except NoSuchElementException:
            pass

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        username.clear()
        password.clear()
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        try:
            login_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_btn.click()
        except NoSuchElementException:
            password.send_keys(Keys.ENTER)

        time.sleep(5)

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(@href,'/home') or contains(@href,'/explore')]")
                )
            )
        except TimeoutException:
            time.sleep(10)

        for text in ["Not now", "Not Now"]:
            try:
                btn = self.driver.find_element(By.XPATH, f"//button[contains(text(), '{text}')]")
                btn.click()
                time.sleep(1)
            except NoSuchElementException:
                pass

        print("✅ Logged in successfully!")

    def find_and_follow_followers(self):
        print(f"🔹 Opening @{SIMILAR_ACCOUNT}'s followers...")
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)

        # Click on followers link
        try:
            followers_link = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "followers"))
            )
            followers_link.click()
            print("✅ Followers modal opened.")
        except TimeoutException:
            print("⚠️ Couldn't open followers list.")
            return

        # Wait for modal to appear (new method: JS check)
        time.sleep(5)
        modal = None
        try:
            modal = self.driver.execute_script("""
                return document.querySelector('div[role="dialog"] div[style*="overflow: auto"]');
            """)
        except Exception:
            pass

        if not modal:
            print("⚠️ Followers modal not found in DOM (hidden or delayed).")
            return

        print("✅ Followers modal detected.")
        time.sleep(2)

        # Scroll through followers list
        print("🔹 Scrolling through followers...")
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

        # Find and follow visible users
        buttons = self.driver.find_elements(
            By.XPATH, "//div[@role='dialog']//button//div/div[text()='Follow']/ancestor::button"
        )
        print(f"🔹 Found {len(buttons)} users to follow.")

        followed = 0
        for button in buttons:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                button.click()
                followed += 1
                print(f"✅ Followed user {followed}/{len(buttons)}")
                time.sleep(2)
            except ElementClickInterceptedException:
                try:
                    cancel = self.driver.find_element(By.XPATH, "//button[contains(text(),'Cancel')]")
                    cancel.click()
                except NoSuchElementException:
                    pass
                print("⚠️ Skipped one user.")
                time.sleep(1)

        print("🎯 Finished following all visible users!")



if __name__ == "__main__":
    bot = InstaFollower()
    bot.login()
    bot.find_and_follow_followers()
    print("✅ All done!")
