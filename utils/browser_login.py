from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

def browser_login():
    driver = webdriver.Chrome(ChromeDriverManager().install())  
    driver.get("https://t8thai.vip")  # 🎯 Game URL

    time.sleep(5)  # Wait for page to load

    # ✅ Find username & password fields (Adjust selectors!)
    username_input = driver.find_element(By.NAME, "username")  # UPDATE THIS!
    password_input = driver.find_element(By.NAME, "password")  # UPDATE THIS!

    # 🔑 Enter login details
    username_input.send_keys("5three8three")
    password_input.send_keys("88peeti88")
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for login
    return driver

# Example usage
if __name__ == "__main__":
    driver = browser_login()
    print("✅ Login Successful! AI Ready to Play!")
