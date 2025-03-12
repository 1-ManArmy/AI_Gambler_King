import time
import pyautogui
from selenium.webdriver.common.by import By
from utils.browser_login import browser_login

# ✅ STEP 1: Login & Open Game
driver = browser_login()

def open_game():
    time.sleep(5)
    game_button = driver.find_element(By.XPATH, "//img[contains(@alt, 'Pinata Wins')]")  # Adjust XPATH!
    game_button.click()
    print("🎰 Entered Game!")

open_game()

# ✅ STEP 2: AI Auto Gameplay
scatter_count = 0

def auto_play():
    global scatter_count  # AI di memory track kare!

    while True:
        pyautogui.click(960, 820)  # Spin Button
        print("🎲 Rolling...")

        time.sleep(1.5)  # Wait for result

        scatter = pyautogui.locateOnScreen("scatter_symbol.png", confidence=0.8)
        if scatter:
            pyautogui.click(scatter)
            print("✅ Scatter Found! Stopping Roll!")
            scatter_count += 1
        else:
            scatter_count = max(0, scatter_count - 1)

        adjust_bet()
        time.sleep(2)

# ✅ STEP 3: AI Betting Strategy
def adjust_bet():
    global scatter_count
    if scatter_count >= 3:
        pyautogui.click(1100, 820)  # Increase bet
        print("⬆️ Increasing Bet!")
    elif scatter_count == 0:
        pyautogui.click(800, 820)  # Decrease bet
        print("⬇️ Decreasing Bet!")

# **Start Auto Play**
auto_play()
