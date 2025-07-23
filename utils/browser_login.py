from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from webdriver_manager.chrome import ChromeDriverManager

def browser_login():
    # Fix for Selenium 4.x compatibility
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get("https://t8thai.vip")  # 🎯 Game URL
        print("✅ Page loaded successfully!")
        
        # Wait for page to load
        wait = WebDriverWait(driver, 10)
        time.sleep(5)
        
        # Try multiple possible selectors for username/password fields
        username_selectors = [
            (By.NAME, "username"),
            (By.ID, "username"),
            (By.CSS_SELECTOR, "input[type='text']"),
            (By.CSS_SELECTOR, "input[placeholder*='username']"),
            (By.CSS_SELECTOR, "input[placeholder*='Username']"),
            (By.CSS_SELECTOR, "input[placeholder*='user']")
        ]
        
        password_selectors = [
            (By.NAME, "password"),
            (By.ID, "password"),
            (By.CSS_SELECTOR, "input[type='password']"),
            (By.CSS_SELECTOR, "input[placeholder*='password']"),
            (By.CSS_SELECTOR, "input[placeholder*='Password']")
        ]
        
        username_input = None
        password_input = None
        
        # Try to find username field
        for selector_type, selector_value in username_selectors:
            try:
                username_input = driver.find_element(selector_type, selector_value)
                print(f"✅ Found username field with: {selector_type}, {selector_value}")
                break
            except NoSuchElementException:
                continue
        
        # Try to find password field
        for selector_type, selector_value in password_selectors:
            try:
                password_input = driver.find_element(selector_type, selector_value)
                print(f"✅ Found password field with: {selector_type}, {selector_value}")
                break
            except NoSuchElementException:
                continue
        
        if username_input and password_input:
            # 🔑 Enter login details
            username_input.send_keys("5three8three")
            password_input.send_keys("88peeti88")
            password_input.send_keys(Keys.RETURN)
            
            time.sleep(5)  # Wait for login
            print("✅ Login attempted successfully!")
        else:
            print("⚠️ Could not find login fields. Manual login may be required.")
            print("📋 Current page title:", driver.title)
            print("📋 Current URL:", driver.current_url)
            
            # Keep browser open for manual interaction
            input("Press Enter after manual login to continue...")
        
        return driver
        
    except Exception as e:
        print(f"❌ Error during browser login: {e}")
        # Don't close the browser, return it anyway
        return driver

# Example usage
if __name__ == "__main__":
    driver = browser_login()
    print("✅ Browser session ready! AI can proceed...")
