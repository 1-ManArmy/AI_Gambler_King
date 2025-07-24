# -*- coding: utf-8 -*-
"""
AI Gambler King - Pinata Wins Controller
Enhanced game controller based on learned game interface
"""

import time
import json
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utils.browser_login import browser_login

class PinataWinsController:
    def __init__(self):
        self.driver = None
        self.game_url = "https://m.56myu5u3v.com/1492288/index.html?ot=AF64C68B-E04E-45E5-A4A3-3D7C2A34463D&btt=1&ops=gt61741327361818-gt6ta6eight4seven3&l=en&or=14ghohwq%3D56ami5i3j%3Dqca&__hv=2fMEUCIFCr8i03AvZCeXdw4o1daP%2BiKKvvU3bddzw8lEeWn2uRAiEAysTYMqIR8d6IWBwPVFJRZ31Fi38BAwnT0IPOz12BeP8%3D"
        self.analysis_data = self.load_analysis_data()
        self.game_center = None
        self.canvas_location = None
        
        # Game state
        self.current_bet = 1.00  # Default bet in Baht
        self.balance = 0.0
        self.is_spinning = False
        self.game_ready = False
        
    def load_analysis_data(self):
        """Load previously analyzed game data"""
        try:
            with open("game_analysis_results.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️ No analysis data found. Run teaching session first!")
            return None
    
    def start_game_session(self):
        """Start a new game session"""
        print("🎰 Starting Pinata Wins game session...")
        
        try:
            # Open browser and navigate to game
            self.driver = browser_login(direct_game_url=self.game_url)
            print("✅ Browser opened successfully!")
            
            # Wait for game to load
            time.sleep(10)
            
            # Initialize game layout
            self.initialize_game_layout()
            
            # Check game readiness
            self.check_game_ready()
            
            return True
            
        except Exception as e:
            print(f"❌ Error starting game session: {e}")
            return False
    
    def initialize_game_layout(self):
        """Initialize game layout based on analysis data"""
        if not self.analysis_data:
            print("⚠️ No analysis data available")
            return
        
        # Get canvas information
        canvas_info = self.analysis_data.get("game_board", {}).get("canvas", {})
        if canvas_info.get("found"):
            self.canvas_location = canvas_info.get("location", {})
            canvas_size = canvas_info.get("size", {})
            self.game_center = canvas_info.get("center", {})
            
            print(f"✅ Game canvas found at: {self.canvas_location}")
            print(f"📐 Canvas size: {canvas_size}")
            print(f"🎯 Game center: {self.game_center}")
        else:
            print("⚠️ Game canvas not found in analysis data")
    
    def check_game_ready(self):
        """Check if the game is ready for interaction"""
        try:
            # Look for canvas element
            canvas = self.driver.find_element(By.TAG_NAME, "canvas")
            if canvas:
                self.game_ready = True
                print("✅ Game is ready!")
                return True
        except NoSuchElementException:
            print("⚠️ Game canvas not found")
        
        self.game_ready = False
        return False
    
    def click_spin_button(self):
        """Click the spin button to start a spin"""
        if not self.game_ready:
            print("⚠️ Game not ready!")
            return False
        
        try:
            print("🎲 Clicking spin button...")
            
            # Based on typical slot games, spin button is usually at bottom center
            # Using canvas center as reference point
            if self.game_center:
                spin_x = self.game_center["x"]
                spin_y = self.game_center["y"] + 200  # Approximate spin button location
                
                # Click using pyautogui (more reliable for canvas games)
                pyautogui.click(spin_x, spin_y)
                print(f"🎯 Clicked at coordinates: ({spin_x}, {spin_y})")
                
                self.is_spinning = True
                return True
            else:
                print("⚠️ Game center not available")
                return False
                
        except Exception as e:
            print(f"❌ Error clicking spin button: {e}")
            return False
    
    def click_increase_bet(self):
        """Increase bet amount"""
        try:
            print("⬆️ Increasing bet...")
            
            if self.game_center:
                # Increase bet button typically on right side
                bet_increase_x = self.game_center["x"] + 100
                bet_increase_y = self.game_center["y"] + 200
                
                pyautogui.click(bet_increase_x, bet_increase_y)
                self.current_bet += 0.50  # Estimate bet increment
                print(f"💰 Bet increased to: {self.current_bet} Baht")
                return True
            
        except Exception as e:
            print(f"❌ Error increasing bet: {e}")
            return False
    
    def click_decrease_bet(self):
        """Decrease bet amount"""
        try:
            print("⬇️ Decreasing bet...")
            
            if self.game_center:
                # Decrease bet button typically on left side
                bet_decrease_x = self.game_center["x"] - 100
                bet_decrease_y = self.game_center["y"] + 200
                
                pyautogui.click(bet_decrease_x, bet_decrease_y)
                self.current_bet = max(0.50, self.current_bet - 0.50)  # Minimum bet
                print(f"💰 Bet decreased to: {self.current_bet} Baht")
                return True
            
        except Exception as e:
            print(f"❌ Error decreasing bet: {e}")
            return False
    
    def wait_for_spin_complete(self, timeout=10):
        """Wait for spin to complete"""
        print("⏳ Waiting for spin to complete...")
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            time.sleep(0.5)
            
            # Check if spin is complete (simplified check)
            # In a real implementation, you'd check for visual cues
            if time.time() - start_time > 3:  # Assume 3 seconds for spin
                self.is_spinning = False
                print("✅ Spin completed!")
                return True
        
        print("⚠️ Spin timeout!")
        self.is_spinning = False
        return False
    
    def capture_game_state(self):
        """Capture current game state"""
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"game_state_{timestamp}.png"
            self.driver.save_screenshot(screenshot_path)
            print(f"📸 Game state captured: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"❌ Error capturing game state: {e}")
            return None
    
    def auto_play_session(self, spins=10):
        """Run automated play session"""
        print(f"🎮 Starting auto-play session ({spins} spins)...")
        
        if not self.game_ready:
            print("❌ Game not ready for auto-play!")
            return
        
        for spin_count in range(1, spins + 1):
            print(f"\n🎲 Spin {spin_count}/{spins}")
            
            # Click spin button
            if self.click_spin_button():
                # Wait for spin to complete
                self.wait_for_spin_complete()
                
                # Capture game state
                self.capture_game_state()
                
                # Simple betting strategy (example)
                if spin_count % 5 == 0:
                    self.click_increase_bet()
                
                # Wait between spins
                time.sleep(2)
            else:
                print("❌ Failed to spin, stopping auto-play")
                break
        
        print("✅ Auto-play session completed!")
    
    def manual_control_mode(self):
        """Enter manual control mode with keyboard commands"""
        print("\n🎮 Manual Control Mode")
        print("=" * 30)
        print("Commands:")
        print("  's' - Spin")
        print("  '+' - Increase bet")
        print("  '-' - Decrease bet")
        print("  'c' - Capture screenshot")
        print("  'q' - Quit")
        print("=" * 30)
        
        while True:
            command = input("\nEnter command: ").lower().strip()
            
            if command == 's':
                self.click_spin_button()
                self.wait_for_spin_complete()
            elif command == '+':
                self.click_increase_bet()
            elif command == '-':
                self.click_decrease_bet()
            elif command == 'c':
                self.capture_game_state()
            elif command == 'q':
                print("👋 Exiting manual control mode")
                break
            else:
                print("❌ Invalid command")
    
    def close_session(self):
        """Close the game session"""
        if self.driver:
            print("🔚 Closing game session...")
            self.driver.quit()
            print("✅ Session closed!")

def main():
    """Main function to run Pinata Wins controller"""
    controller = PinataWinsController()
    
    print("🎰 AI Gambler King - Pinata Wins Controller")
    print("=" * 50)
    
    # Start game session
    if controller.start_game_session():
        print("\n🎮 Choose game mode:")
        print("1. Auto-play (10 spins)")
        print("2. Manual control")
        print("3. Exit")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == "1":
            controller.auto_play_session(10)
        elif choice == "2":
            controller.manual_control_mode()
        elif choice == "3":
            print("👋 Exiting...")
        else:
            print("❌ Invalid choice")
    
    # Close session
    controller.close_session()

if __name__ == "__main__":
    main()
