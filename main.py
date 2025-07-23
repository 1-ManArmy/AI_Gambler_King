# -*- coding: utf-8 -*-
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utils.browser_login import browser_login

print("🚀 Starting AI Gambler King...")

# ✅ STEP 1: Login & Open Game
try:
    driver = browser_login()
    print("✅ Browser session established!")
except Exception as e:
    print(f"❌ Browser login failed: {e}")
    exit(1)

def open_game():
    try:
        time.sleep(5)
        
        # Try multiple selectors for the game button
        game_selectors = [
            (By.XPATH, "//img[contains(@alt, 'Pinata Wins')]"),
            (By.XPATH, "//img[contains(@alt, 'pinata')]"),
            (By.XPATH, "//a[contains(text(), 'Pinata')]"),
            (By.CSS_SELECTOR, "img[alt*='Pinata']"),
            (By.CSS_SELECTOR, "a[href*='pinata']")
        ]
        
        game_button = None
        for selector_type, selector_value in game_selectors:
            try:
                game_button = driver.find_element(selector_type, selector_value)
                print(f"✅ Found game button with: {selector_type}, {selector_value}")
                break
            except NoSuchElementException:
                continue
        
        if game_button:
            game_button.click()
            print("🎰 Entered Game!")
        else:
            print("⚠️ Game button not found. Manual navigation may be required.")
            print("📋 Current URL:", driver.current_url)
            input("Press Enter after manually opening the game to continue...")
            
    except Exception as e:
        print(f"❌ Error opening game: {e}")
        print("📋 Continuing anyway...")

# Try to open the game
open_game()

# ✅ STEP 2: AI Auto Gameplay
scatter_count = 0

def auto_play():
    global scatter_count  # AI di memory track kare!
    
    print("🎮 Starting auto-play mode...")
    print("⚠️ Make sure the game window is visible and active!")
    
    try:
        while True:
            pyautogui.click(960, 820)  # Spin Button
            print("🎲 Rolling...")

            time.sleep(1.5)  # Wait for result

            # Look for scatter symbol (you'll need to capture this image first)
            try:
                scatter = pyautogui.locateOnScreen("scatter_symbol.png", confidence=0.8)
                if scatter:
                    pyautogui.click(scatter)
                    print("✅ Scatter Found! Stopping Roll!")
                    scatter_count += 1
                else:
                    scatter_count = max(0, scatter_count - 1)
            except pyautogui.ImageNotFoundException:
                print("🔍 Scatter symbol image not found on screen")
                scatter_count = max(0, scatter_count - 1)

            adjust_bet()
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n⏹️ Auto-play stopped by user")
    except Exception as e:
        print(f"❌ Error in auto-play: {e}")

# ✅ STEP 3: AI Betting Strategy
def adjust_bet():
    global scatter_count
    try:
        if scatter_count >= 3:
            pyautogui.click(1100, 820)  # Increase bet
            print("⬆️ Increasing Bet!")
        elif scatter_count == 0:
            pyautogui.click(800, 820)  # Decrease bet
            print("⬇️ Decreasing Bet!")
    except Exception as e:
        print(f"⚠️ Error adjusting bet: {e}")

# **Start Auto Play**
if __name__ == "__main__":
    print("🎯 Ready to start auto-play!")
    print("⚠️ Make sure:")
    print("   1. Game is open and visible")
    print("   2. You have the scatter_symbol.png image in the current directory")
    print("   3. Press Ctrl+C to stop auto-play anytime")
    
    response = input("\nStart auto-play? (y/n): ")
    if response.lower() == 'y':
        auto_play()
    else:
        print("✅ AI Gambler King ready! Browser session remains open.")
        print("📝 You can manually interact with the game or run specific modules.")
