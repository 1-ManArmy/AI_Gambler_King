# -*- coding: utf-8 -*-
"""
AI Gambler King - Pinata Wins Specialized Controller
Based on actual game analysis and coordinate mapping
"""

import time
import json
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.browser_login import browser_login

class PinataWinsPlayer:
    def __init__(self):
        self.driver = None
        self.game_url = "https://m.56myu5u3v.com/1492288/index.html?ot=AF64C68B-E04E-45E5-A4A3-3D7C2A34463D&btt=1&ops=gt61741327361818-gt6ta6eight4seven3&l=en&or=14ghohwq%3D56ami5i3j%3Dqca&__hv=2fMEUCIFCr8i03AvZCeXdw4o1daP%2BiKKvvU3bddzw8lEeWn2uRAiEAysTYMqIR8d6IWBwPVFJRZ31Fi38BAwnT0IPOz12BeP8%3D"
        
        # Game coordinates based on analysis
        self.game_center = (518, 257)  # Canvas center point
        self.canvas_location = (374, 0)
        self.canvas_size = (289, 515)
        
        # Estimated control coordinates (will be refined through testing)
        self.spin_button = (518, 450)      # Bottom center of canvas
        self.bet_increase = (580, 450)     # Right of spin button
        self.bet_decrease = (456, 450)     # Left of spin button
        self.max_bet = (518, 480)          # Below spin button
        
        # Game state
        self.current_bet = 1.00  # Default bet in Baht
        self.is_spinning = False
        self.game_active = False
        self.session_stats = {
            "spins": 0,
            "wins": 0,
            "total_bet": 0.0,
            "total_win": 0.0
        }
    
    def start_game_session(self):
        """Start a new Pinata Wins game session"""
        print("🎰 Starting Pinata Wins Session...")
        print("=" * 50)
        
        try:
            # Open browser to game
            print("🌐 Opening browser...")
            self.driver = browser_login(direct_game_url=self.game_url)
            
            # Wait for game to load
            print("⏳ Waiting for game to load (60-90 seconds)...")
            self.wait_for_game_loading()
            
            # Manual START button intervention
            print("🔧 Manual START button click required...")
            print("   👆 Please click the START button to enter the game board")
            input("   ✅ Press Enter after clicking START...")
            
            # Wait for game board
            print("⏳ Waiting for game board to stabilize...")
            time.sleep(5)
            
            # Verify game is ready
            self.verify_game_ready()
            
            print("✅ Pinata Wins session ready!")
            return True
            
        except Exception as e:
            print(f"❌ Error starting session: {e}")
            return False
    
    def wait_for_game_loading(self, timeout=90):
        """Wait for initial game loading"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                # Check for canvas element
                canvas = self.driver.find_element(By.TAG_NAME, "canvas")
                if canvas:
                    print("✅ Game canvas detected!")
                    time.sleep(2)
                    return True
            except:
                pass
            
            elapsed = int(time.time() - start_time)
            if elapsed % 10 == 0:  # Print every 10 seconds
                print(f"   ⏳ Still loading... ({elapsed}s)")
            
            time.sleep(1)
        
        print("⚠️ Loading timeout, proceeding...")
        return True
    
    def verify_game_ready(self):
        """Verify game board is ready for interaction"""
        try:
            canvas = self.driver.find_element(By.TAG_NAME, "canvas")
            if canvas:
                location = canvas.location
                size = canvas.size
                
                print(f"✅ Game verification:")
                print(f"   📍 Canvas at: {location}")
                print(f"   📐 Canvas size: {size}")
                print(f"   🎯 Game center: {self.game_center}")
                
                self.game_active = True
                return True
        except Exception as e:
            print(f"⚠️ Game verification warning: {e}")
        
        self.game_active = False
        return False
    
    def click_spin(self):
        """Click the spin button"""
        if not self.game_active:
            print("❌ Game not active!")
            return False
        
        if self.is_spinning:
            print("⚠️ Already spinning!")
            return False
        
        try:
            print(f"🎲 Clicking SPIN at {self.spin_button}...")
            pyautogui.click(self.spin_button[0], self.spin_button[1])
            
            self.is_spinning = True
            self.session_stats["spins"] += 1
            self.session_stats["total_bet"] += self.current_bet
            
            print(f"✅ Spin #{self.session_stats['spins']} initiated! (Bet: {self.current_bet} Baht)")
            return True
            
        except Exception as e:
            print(f"❌ Error clicking spin: {e}")
            return False
    
    def click_increase_bet(self):
        """Increase bet amount"""
        try:
            print(f"⬆️ Increasing bet at {self.bet_increase}...")
            pyautogui.click(self.bet_increase[0], self.bet_increase[1])
            
            self.current_bet += 0.50  # Estimate increment
            print(f"💰 Bet increased to: {self.current_bet} Baht")
            return True
            
        except Exception as e:
            print(f"❌ Error increasing bet: {e}")
            return False
    
    def click_decrease_bet(self):
        """Decrease bet amount"""
        try:
            print(f"⬇️ Decreasing bet at {self.bet_decrease}...")
            pyautogui.click(self.bet_decrease[0], self.bet_decrease[1])
            
            self.current_bet = max(0.50, self.current_bet - 0.50)  # Minimum 0.50 Baht
            print(f"💰 Bet decreased to: {self.current_bet} Baht")
            return True
            
        except Exception as e:
            print(f"❌ Error decreasing bet: {e}")
            return False
    
    def wait_for_spin_complete(self, timeout=8):
        """Wait for spin to complete"""
        print("⏳ Waiting for spin to complete...")
        
        start_time = time.time()
        
        # Simple time-based waiting (can be enhanced with visual detection)
        while time.time() - start_time < timeout:
            elapsed = time.time() - start_time
            
            if elapsed > 3:  # Minimum spin time
                # Check if spin might be complete (simplified)
                print(f"   ⏰ Spin time: {elapsed:.1f}s")
                
                if elapsed > 5:  # Typical slot spin duration
                    break
            
            time.sleep(0.5)
        
        self.is_spinning = False
        print("✅ Spin completed!")
        return True
    
    def capture_result(self):
        """Capture game result after spin"""
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"spin_result_{timestamp}.png"
            
            self.driver.save_screenshot(screenshot_path)
            print(f"📸 Result captured: {screenshot_path}")
            
            return screenshot_path
        except Exception as e:
            print(f"⚠️ Error capturing result: {e}")
            return None
    
    def auto_play_session(self, num_spins=5):
        """Automated play session"""
        print(f"\n🎮 Starting auto-play: {num_spins} spins")
        print("=" * 40)
        
        if not self.game_active:
            print("❌ Game not ready for auto-play!")
            return
        
        for spin_num in range(1, num_spins + 1):
            print(f"\n🎲 SPIN {spin_num}/{num_spins}")
            
            # Click spin
            if self.click_spin():
                # Wait for result
                self.wait_for_spin_complete()
                
                # Capture result
                self.capture_result()
                
                # Simple betting strategy
                if spin_num % 3 == 0:  # Every 3rd spin
                    print("📊 Adjusting strategy...")
                    # Could implement more sophisticated logic here
                
                # Wait between spins
                time.sleep(2)
            else:
                print("❌ Spin failed, stopping auto-play")
                break
        
        self.print_session_stats()
    
    def manual_control(self):
        """Manual control mode"""
        print("\n🎮 MANUAL CONTROL MODE")
        print("=" * 30)
        print("Commands:")
        print("  's' - Spin")
        print("  '+' - Increase bet")
        print("  '-' - Decrease bet")
        print("  'c' - Capture screenshot")
        print("  'r' - Show session stats")
        print("  'q' - Quit")
        print("=" * 30)
        
        while True:
            command = input(f"\n💰 Bet: {self.current_bet} Baht | Command: ").lower().strip()
            
            if command == 's':
                if self.click_spin():
                    self.wait_for_spin_complete()
                    self.capture_result()
            elif command == '+':
                self.click_increase_bet()
            elif command == '-':
                self.click_decrease_bet()
            elif command == 'c':
                self.capture_result()
            elif command == 'r':
                self.print_session_stats()
            elif command == 'q':
                print("👋 Exiting manual control")
                break
            else:
                print("❌ Invalid command")
    
    def print_session_stats(self):
        """Print session statistics"""
        print(f"\n📊 SESSION STATISTICS:")
        print(f"   🎲 Total Spins: {self.session_stats['spins']}")
        print(f"   💰 Total Bet: {self.session_stats['total_bet']:.2f} Baht")
        print(f"   🏆 Total Wins: {self.session_stats['wins']}")
        print(f"   💵 Total Won: {self.session_stats['total_win']:.2f} Baht")
        print(f"   📈 Current Bet: {self.current_bet:.2f} Baht")
    
    def close_session(self):
        """Close the game session"""
        self.print_session_stats()
        
        if self.driver:
            print("🔚 Closing browser session...")
            self.driver.quit()
            print("✅ Session closed!")

def main():
    """Main function to run Pinata Wins player"""
    player = PinataWinsPlayer()
    
    print("🎰 AI GAMBLER KING - PINATA WINS PLAYER")
    print("=" * 50)
    print("🎯 Specialized controller for Pinata Wins slot game")
    print("💰 Default bet: 1.00 Baht (as requested)")
    print("=" * 50)
    
    # Start session
    if player.start_game_session():
        print(f"\n🎮 Game Mode Selection:")
        print("1. 🤖 Auto-play (5 spins)")
        print("2. 🎮 Manual control")
        print("3. 🚀 Quick test (1 spin)")
        print("4. 🔚 Exit")
        
        choice = input("\nSelect mode (1-4): ").strip()
        
        if choice == "1":
            player.auto_play_session(5)
        elif choice == "2":
            player.manual_control()
        elif choice == "3":
            print("🚀 Quick test...")
            if player.click_spin():
                player.wait_for_spin_complete()
                player.capture_result()
        elif choice == "4":
            print("👋 Exiting...")
        else:
            print("❌ Invalid choice")
    
    # Close session
    player.close_session()

if __name__ == "__main__":
    main()
