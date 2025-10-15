from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ---------------- CONFIG ----------------
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSf3Q_u2sKYVCwLlMvBVh3QOj0CxVSzKUfWqRsyYpZ6QfE2Jww/viewform?usp=header"
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/141.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "DNT": "1",
    "Connection": "keep-alive",
}

# ---------------- SCRAPING SECTION ----------------
response = requests.get(ZILLOW_CLONE_URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

# Extract property details
all_links = [link["href"] for link in soup.select(".StyledPropertyCardDataWrapper a")]
all_addresses = [addr.get_text().replace(" | ", " ").strip()
                 for addr in soup.select(".StyledPropertyCardDataWrapper address")]
all_prices = [price.get_text().replace("/mo", "").split("+")[0]
              for price in soup.select(".PropertyCardWrapper span") if "$" in price.text]

print(f"✅ Found {len(all_links)} listings.")
print(f"Addresses: {all_addresses}")
print(f"Prices: {all_prices}")
print(f"Links: {all_links}")

# ---------------- FORM SUBMISSION SECTION ----------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get(FORM_URL)
    time.sleep(2)

    address_field = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address_field.send_keys(all_addresses[n])
    price_field.send_keys(all_prices[n])
    link_field.send_keys(all_links[n])
    submit_button.click()

print("\n🎉 All listings successfully submitted to the Google Form!")
driver.quit()
