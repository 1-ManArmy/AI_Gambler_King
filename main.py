# -*- coding: utf-8 -*-
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utils.browser_login import browser_login

print("🚀 Starting AI Gambler King...")

# Direct Pinata Wins game URL
PINATA_WINS_URL = "https://m.56myu5u3v.com/1492288/index.html?ot=AF64C68B-E04E-45E5-A4A3-3D7C2A34463D&btt=1&ops=gt61741327361818-gt6ta6eight4seven3&l=en&or=14ghohwq%3D56ami5i3j%3Dqca&__hv=2fMEUCIFCr8i03AvZCeXdw4o1daP%2BiKKvvU3bddzw8lEeWn2uRAiEAysTYMqIR8d6IWBwPVFJRZ31Fi38BAwnT0IPOz12BeP8%3D"

# ✅ STEP 1: Open Game Directly
try:
    driver = browser_login(direct_game_url=PINATA_WINS_URL)
    print("✅ Direct navigation to Pinata Wins game successful!")
    print("🎰 Game board should be loading...")
    time.sleep(10)  # Give game time to load
except Exception as e:
    print(f"❌ Browser setup failed: {e}")
    exit(1)

def check_game_ready():
    """Check if the game is fully loaded and ready"""
    try:
        print("🔍 Checking if game is ready...")
        
        # Wait for game elements to load
        time.sleep(5)
        
        # Look for common game elements that indicate it's ready
        game_ready_indicators = [
            (By.TAG_NAME, "canvas"),  # Game canvas
            (By.CSS_SELECTOR, "button[class*='spin']"),  # Spin button
            (By.CSS_SELECTOR, "div[class*='game']"),  # Game container
            (By.CSS_SELECTOR, "iframe"),  # Game iframe
        ]
        
        for selector_type, selector_value in game_ready_indicators:
            try:
                element = driver.find_element(selector_type, selector_value)
                if element:
                    print(f"✅ Game ready indicator found: {selector_type}, {selector_value}")
                    return True
            except NoSuchElementException:
                continue
        
        print("⚠️ Game readiness unclear. Proceeding anyway...")
        print("📋 Current URL:", driver.current_url)
        return True
        
    except Exception as e:
        print(f"⚠️ Error checking game readiness: {e}")
        return True

# Check if game is ready
check_game_ready()

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
