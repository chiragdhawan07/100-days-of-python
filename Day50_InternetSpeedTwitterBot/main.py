from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "your_email@gmail.com"
TWITTER_PASSWORD = "your_password"


class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.up = None
        self.down = None

    def get_internet_speed(self):
        print("🌐 Opening speedtest.net ...")
        self.driver.get("https://www.speedtest.net/")
        wait = WebDriverWait(self.driver, 60)

        # ✅ Step 1: Accept cookies if present
        try:
            consent = wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            consent.click()
            print("✅ Accepted cookie popup.")
        except Exception:
            print("ℹ️ No cookie popup found.")

        # ✅ Step 2: Click GO
        go_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
        go_btn.click()
        print("🚀 Started speed test, waiting for results...")

        # ✅ Step 3: Wait for results
        time.sleep(45) # Wait time may vary based on connection speed

        try:
            self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
            self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
            print(f"✅ Speed Test Results: {self.down} Mbps down / {self.up} Mbps up")
        except Exception as e:
            print("❌ Could not get results:", e)
            return

    def tweet_at_provider(self):
        print("🐦 Opening Twitter login...")
        self.driver.get("https://twitter.com/login")
        wait = WebDriverWait(self.driver, 60)

        try:
            email = wait.until(EC.presence_of_element_located((By.NAME, "text")))
            email.send_keys(TWITTER_EMAIL)
            email.send_keys(Keys.ENTER)
            print("✅ Entered email.")
            time.sleep(2)

            password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            print("✅ Logged in successfully.")
        except Exception as e:
            print("❌ Twitter login failed:", e)
            return

        time.sleep(5)
        tweet_text = (
            f"Hey Internet Provider, why is my internet speed {self.down} down / {self.up} up "
            f"when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up?"
        )

        try:
            tweet_box = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Post text"]'))
            )
            tweet_box.send_keys(tweet_text)
            print("✅ Tweet typed.")
        except Exception as e:
            print("❌ Could not type tweet:", e)
            return

        try:
            post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Post"]')))
            post_button.click()
            print("✅ Tweet sent successfully!")
        except Exception as e:
            print("❌ Could not find Post button:", e)

        print("✅ Done — browser left open for checking.")
        input("🔹 Press Enter to close browser...")  
        self.driver.quit()


# Run
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
