# -*- coding: utf-8 -*-
"""
AI Gambler King - Game Analyzer
Comprehensive game interface analysis for Pinata Wins slot game
"""

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.browser_login import browser_login
from utils.screen_capture import capture_screen
import pyautogui

class GameAnalyzer:
    def __init__(self):
        self.driver = None
        self.game_url = "https://m.56myu5u3v.com/1492288/index.html?ot=AF64C68B-E04E-45E5-A4A3-3D7C2A34463D&btt=1&ops=gt61741327361818-gt6ta6eight4seven3&l=en&or=14ghohwq%3D56ami5i3j%3Dqca&__hv=2fMEUCIFCr8i03AvZCeXdw4o1daP%2BiKKvvU3bddzw8lEeWn2uRAiEAysTYMqIR8d6IWBwPVFJRZ31Fi38BAwnT0IPOz12BeP8%3D"
        self.analysis_results = {
            "game_info": {},
            "buttons": {},
            "display_elements": {},
            "game_board": {},
            "betting_controls": {},
            "symbols": {}
        }
    
    def start_analysis(self):
        """Start comprehensive game analysis"""
        print("🔍 AI Gambler King - Game Analysis Starting...")
        
        try:
            # Open browser and navigate to game
            self.driver = browser_login(direct_game_url=self.game_url)
            print("✅ Successfully navigated to Pinata Wins game!")
            
            # STEP 1: Wait for initial game loading
            if not self.wait_for_game_loading():
                print("❌ Game failed to load properly")
                return None
            
            # STEP 2: Find and click START button
            if not self.find_and_click_start_button():
                print("❌ Could not find or click START button")
                return None
            
            # STEP 3: Wait for game board to load
            if not self.wait_for_game_board():
                print("❌ Game board failed to load")
                return None
            
            # STEP 4: Now analyze everything on the game board
            print("🎰 Game board loaded! Starting comprehensive analysis...")
            self.analyze_page_structure()
            self.analyze_game_board()
            self.analyze_betting_controls()
            self.analyze_display_elements()
            self.analyze_buttons()
            self.capture_game_state()
            
            # Save analysis results
            self.save_analysis()
            
            print("✅ Game analysis completed successfully!")
            return self.analysis_results
            
        except Exception as e:
            print(f"❌ Error during game analysis: {e}")
            return None
    
    def wait_for_game_loading(self, timeout=90):
        """Wait for initial game loading to complete"""
        print("⏳ Waiting for game to load (this may take up to 90 seconds)...")
        
        start_time = time.time()
        loading_indicators = [
            "loading",
            "Loading",
            "LOADING",
            "load",
            "progress",
            "wait",
            "initializing"
        ]
        
        while time.time() - start_time < timeout:
            try:
                # Check page title and content
                page_text = self.driver.page_source.lower()
                
                # Look for loading indicators
                is_loading = any(indicator in page_text for indicator in loading_indicators)
                
                if not is_loading:
                    # Check if we can find potential start elements
                    potential_start_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'START') or contains(text(), 'Start') or contains(text(), 'PLAY') or contains(text(), 'Play')]")
                    
                    if potential_start_elements:
                        print("✅ Game loaded! START button should be available.")
                        time.sleep(2)  # Small additional wait
                        return True
                
                print(f"⏳ Still loading... ({int(time.time() - start_time)}s)")
                time.sleep(3)
                
            except Exception as e:
                print(f"⚠️ Error checking loading status: {e}")
                time.sleep(3)
        
        print("⚠️ Loading timeout reached, proceeding anyway...")
        return True
    
    def find_and_click_start_button(self):
        """Find and click the START button to enter game board"""
        print("🔍 Looking for START button...")
        
        # Multiple possible selectors for START button
        start_selectors = [
            # Text-based selectors
            (By.XPATH, "//button[contains(text(), 'START')]"),
            (By.XPATH, "//button[contains(text(), 'Start')]"),
            (By.XPATH, "//div[contains(text(), 'START')]"),
            (By.XPATH, "//div[contains(text(), 'Start')]"),
            (By.XPATH, "//span[contains(text(), 'START')]"),
            (By.XPATH, "//span[contains(text(), 'Start')]"),
            (By.XPATH, "//a[contains(text(), 'START')]"),
            (By.XPATH, "//a[contains(text(), 'Start')]"),
            
            # PLAY button alternatives
            (By.XPATH, "//button[contains(text(), 'PLAY')]"),
            (By.XPATH, "//button[contains(text(), 'Play')]"),
            (By.XPATH, "//div[contains(text(), 'PLAY')]"),
            (By.XPATH, "//div[contains(text(), 'Play')]"),
            
            # Class-based selectors
            (By.CSS_SELECTOR, "button[class*='start']"),
            (By.CSS_SELECTOR, "button[class*='Start']"),
            (By.CSS_SELECTOR, "button[class*='play']"),
            (By.CSS_SELECTOR, "button[class*='Play']"),
            (By.CSS_SELECTOR, "div[class*='start'][onclick]"),
            (By.CSS_SELECTOR, "div[class*='play'][onclick]"),
            
            # ID-based selectors
            (By.ID, "start"),
            (By.ID, "Start"),
            (By.ID, "play"),
            (By.ID, "Play"),
            (By.ID, "startButton"),
            (By.ID, "playButton"),
        ]
        
        for selector_type, selector_value in start_selectors:
            try:
                elements = self.driver.find_elements(selector_type, selector_value)
                
                for element in elements:
                    # Check if element is visible and clickable
                    if element.is_displayed() and element.is_enabled():
                        print(f"✅ Found START button: {selector_type} = {selector_value}")
                        print(f"   Text: '{element.text}'")
                        print(f"   Location: {element.location}")
                        
                        # Try to click the element
                        try:
                            element.click()
                            print("✅ Successfully clicked START button!")
                            time.sleep(3)  # Wait for transition
                            return True
                        except Exception as click_error:
                            print(f"⚠️ Click failed, trying JavaScript: {click_error}")
                            # Try JavaScript click as fallback
                            try:
                                self.driver.execute_script("arguments[0].click();", element)
                                print("✅ Successfully clicked START button with JavaScript!")
                                time.sleep(3)
                                return True
                            except Exception as js_error:
                                print(f"⚠️ JavaScript click also failed: {js_error}")
                                continue
                        
            except Exception as e:
                continue
        
        print("❌ Could not find START button with any selector")
        print("📋 Available elements with 'start' or 'play' text:")
        
        # Debug: Show all elements containing start/play
        try:
            all_elements = self.driver.find_elements(By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'start') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'play')]")
            for elem in all_elements[:10]:  # Show first 10
                try:
                    print(f"   - {elem.tag_name}: '{elem.text}' at {elem.location}")
                except:
                    pass
        except:
            pass
        
        # Ask user for manual intervention
        print("🔧 Manual intervention required:")
        print("   Please manually click the START button to enter the game board")
        input("   Press Enter after clicking START button...")
        
        time.sleep(3)
        return True
    
    def wait_for_game_board(self, timeout=30):
        """Wait for game board to fully load"""
        print("⏳ Waiting for game board to load...")
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                # Look for game board indicators
                game_board_indicators = [
                    (By.TAG_NAME, "canvas"),
                    (By.CSS_SELECTOR, "div[class*='game']"),
                    (By.CSS_SELECTOR, "div[class*='board']"),
                    (By.CSS_SELECTOR, "div[class*='slot']"),
                    (By.CSS_SELECTOR, "div[class*='reel']"),
                ]
                
                for selector_type, selector_value in game_board_indicators:
                    try:
                        elements = self.driver.find_elements(selector_type, selector_value)
                        if elements:
                            print(f"✅ Game board detected: {selector_type}")
                            time.sleep(2)  # Additional stabilization time
                            return True
                    except:
                        continue
                
                print(f"⏳ Waiting for game board... ({int(time.time() - start_time)}s)")
                time.sleep(2)
                
            except Exception as e:
                print(f"⚠️ Error waiting for game board: {e}")
                time.sleep(2)
        
        print("⚠️ Game board timeout, proceeding with analysis...")
        return True
    
    def analyze_page_structure(self):
        """Analyze overall page structure"""
        print("📋 Analyzing page structure...")
        
        try:
            # Basic page info
            self.analysis_results["game_info"] = {
                "title": self.driver.title,
                "url": self.driver.current_url,
                "window_size": self.driver.get_window_size(),
                "page_source_length": len(self.driver.page_source)
            }
            
            # Find all interactive elements
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            inputs = self.driver.find_elements(By.TAG_NAME, "input")
            clickable_divs = self.driver.find_elements(By.CSS_SELECTOR, "div[onclick], div[class*='btn'], div[class*='button']")
            
            print(f"   📊 Found {len(buttons)} buttons")
            print(f"   📊 Found {len(inputs)} input fields")
            print(f"   📊 Found {len(clickable_divs)} clickable divs")
            
        except Exception as e:
            print(f"⚠️ Error analyzing page structure: {e}")
    
    def analyze_game_board(self):
        """Analyze the game board area"""
        print("🎰 Analyzing game board...")
        
        try:
            # Look for common slot game selectors
            board_selectors = [
                "canvas",
                "div[class*='game']",
                "div[class*='board']",
                "div[class*='reel']",
                "div[class*='slot']",
                "iframe[src*='game']"
            ]
            
            game_board_info = {}
            
            for selector in board_selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        element = elements[0]
                        location = element.location
                        size = element.size
                        
                        game_board_info[selector] = {
                            "found": True,
                            "count": len(elements),
                            "location": location,
                            "size": size,
                            "center": {
                                "x": location['x'] + size['width'] // 2,
                                "y": location['y'] + size['height'] // 2
                            }
                        }
                        print(f"   ✅ Found game element: {selector} at {location}")
                        
                except Exception as e:
                    game_board_info[selector] = {"found": False, "error": str(e)}
            
            self.analysis_results["game_board"] = game_board_info
            
        except Exception as e:
            print(f"⚠️ Error analyzing game board: {e}")
    
    def analyze_betting_controls(self):
        """Analyze betting controls"""
        print("💰 Analyzing betting controls...")
        
        try:
            # Common betting control patterns
            betting_patterns = [
                # Increase bet
                {"type": "increase", "selectors": [
                    "button[class*='plus']",
                    "button[class*='increase']",
                    "button[class*='up']",
                    "div[class*='plus']",
                    "div[onclick*='increase']",
                    "[class*='bet'][class*='plus']"
                ]},
                # Decrease bet
                {"type": "decrease", "selectors": [
                    "button[class*='minus']",
                    "button[class*='decrease']",
                    "button[class*='down']",
                    "div[class*='minus']",
                    "div[onclick*='decrease']",
                    "[class*='bet'][class*='minus']"
                ]},
                # Spin button
                {"type": "spin", "selectors": [
                    "button[class*='spin']",
                    "button[class*='play']",
                    "button[class*='start']",
                    "div[class*='spin']",
                    "div[onclick*='spin']",
                    "[class*='roll']"
                ]},
                # Max bet
                {"type": "max_bet", "selectors": [
                    "button[class*='max']",
                    "div[class*='max'][class*='bet']"
                ]}
            ]
            
            betting_controls = {}
            
            for pattern in betting_patterns:
                control_type = pattern["type"]
                betting_controls[control_type] = []
                
                for selector in pattern["selectors"]:
                    try:
                        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                        for element in elements:
                            location = element.location
                            size = element.size
                            text = element.text.strip()
                            
                            betting_controls[control_type].append({
                                "selector": selector,
                                "location": location,
                                "size": size,
                                "text": text,
                                "center": {
                                    "x": location['x'] + size['width'] // 2,
                                    "y": location['y'] + size['height'] // 2
                                }
                            })
                            
                            print(f"   ✅ Found {control_type} control: '{text}' at {location}")
                            
                    except Exception as e:
                        continue
            
            self.analysis_results["betting_controls"] = betting_controls
            
        except Exception as e:
            print(f"⚠️ Error analyzing betting controls: {e}")
    
    def analyze_display_elements(self):
        """Analyze display elements (balance, bet amount, etc.)"""
        print("📊 Analyzing display elements...")
        
        try:
            # Common display patterns
            display_patterns = [
                {"type": "balance", "selectors": [
                    "[class*='balance']",
                    "[class*='money']",
                    "[class*='credit']",
                    "[id*='balance']",
                    "span[class*='amount']"
                ]},
                {"type": "bet_amount", "selectors": [
                    "[class*='bet'][class*='amount']",
                    "[class*='stake']",
                    "[id*='bet']",
                    "input[type='number']"
                ]},
                {"type": "win_amount", "selectors": [
                    "[class*='win']",
                    "[class*='prize']",
                    "[class*='payout']"
                ]}
            ]
            
            display_elements = {}
            
            for pattern in display_patterns:
                element_type = pattern["type"]
                display_elements[element_type] = []
                
                for selector in pattern["selectors"]:
                    try:
                        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                        for element in elements:
                            location = element.location
                            size = element.size
                            text = element.text.strip()
                            value = element.get_attribute("value") if element.tag_name == "input" else None
                            
                            display_elements[element_type].append({
                                "selector": selector,
                                "location": location,
                                "size": size,
                                "text": text,
                                "value": value,
                                "tag": element.tag_name
                            })
                            
                            print(f"   ✅ Found {element_type}: '{text or value}' at {location}")
                            
                    except Exception as e:
                        continue
            
            self.analysis_results["display_elements"] = display_elements
            
        except Exception as e:
            print(f"⚠️ Error analyzing display elements: {e}")
    
    def analyze_buttons(self):
        """Analyze all buttons on the page"""
        print("🔘 Analyzing all buttons...")
        
        try:
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            clickable_divs = self.driver.find_elements(By.CSS_SELECTOR, "div[onclick], div[class*='btn']")
            
            all_buttons = []
            
            for button in buttons + clickable_divs:
                try:
                    location = button.location
                    size = button.size
                    text = button.text.strip()
                    class_name = button.get_attribute("class")
                    onclick = button.get_attribute("onclick")
                    
                    all_buttons.append({
                        "tag": button.tag_name,
                        "text": text,
                        "class": class_name,
                        "onclick": onclick,
                        "location": location,
                        "size": size,
                        "center": {
                            "x": location['x'] + size['width'] // 2,
                            "y": location['y'] + size['height'] // 2
                        }
                    })
                    
                    print(f"   🔘 Button: '{text}' | Class: '{class_name}' at {location}")
                    
                except Exception as e:
                    continue
            
            self.analysis_results["buttons"]["all_buttons"] = all_buttons
            
        except Exception as e:
            print(f"⚠️ Error analyzing buttons: {e}")
    
    def capture_game_state(self):
        """Capture screenshot and game state"""
        print("📸 Capturing game state...")
        
        try:
            # Take screenshot
            screenshot_path = "game_analysis_screenshot.png"
            self.driver.save_screenshot(screenshot_path)
            print(f"   📸 Screenshot saved: {screenshot_path}")
            
            # Get page source
            with open("game_page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            print("   💾 Page source saved: game_page_source.html")
            
        except Exception as e:
            print(f"⚠️ Error capturing game state: {e}")
    
    def save_analysis(self):
        """Save analysis results to JSON file"""
        try:
            with open("game_analysis_results.json", "w", encoding="utf-8") as f:
                json.dump(self.analysis_results, f, indent=2, ensure_ascii=False)
            print("💾 Analysis results saved: game_analysis_results.json")
            
        except Exception as e:
            print(f"⚠️ Error saving analysis: {e}")
    
    def print_summary(self):
        """Print analysis summary"""
        print("\n" + "="*60)
        print("🎯 PINATA WINS GAME BOARD ANALYSIS SUMMARY")
        print("="*60)
        
        # Game info
        game_info = self.analysis_results.get("game_info", {})
        print(f"🎮 Game Title: {game_info.get('title', 'N/A')}")
        print(f"🌐 Game URL: {game_info.get('url', 'N/A')}")
        print(f"📐 Window Size: {game_info.get('window_size', 'N/A')}")
        print(f"📄 Page Source Length: {game_info.get('page_source_length', 'N/A')} characters")
        
        # Game board analysis
        print(f"\n🎰 GAME BOARD ANALYSIS:")
        game_board = self.analysis_results.get("game_board", {})
        for element_type, info in game_board.items():
            if info.get("found"):
                location = info.get("location", {})
                size = info.get("size", {})
                center = info.get("center", {})
                print(f"   ✅ {element_type.upper()}:")
                print(f"      📍 Location: x={location.get('x', 'N/A')}, y={location.get('y', 'N/A')}")
                print(f"      📐 Size: {size.get('width', 'N/A')}x{size.get('height', 'N/A')}")
                print(f"      🎯 Center: x={center.get('x', 'N/A')}, y={center.get('y', 'N/A')}")
                print(f"      🔢 Count: {info.get('count', 'N/A')}")
        
        # Betting controls
        print(f"\n💰 BETTING CONTROLS FOUND:")
        betting_controls = self.analysis_results.get("betting_controls", {})
        total_controls = 0
        for control_type, controls in betting_controls.items():
            if controls:
                total_controls += len(controls)
                print(f"   🎮 {control_type.upper().replace('_', ' ')}: {len(controls)} found")
                for i, control in enumerate(controls[:3]):  # Show first 3
                    location = control.get("location", {})
                    print(f"      {i+1}. Text: '{control.get('text', 'N/A')}' at ({location.get('x', 'N/A')}, {location.get('y', 'N/A')})")
        
        if total_controls == 0:
            print("   ⚠️ No betting controls detected")
        
        # Display elements
        print(f"\n📊 DISPLAY ELEMENTS:")
        display_elements = self.analysis_results.get("display_elements", {})
        total_displays = 0
        for element_type, elements in display_elements.items():
            if elements:
                total_displays += len(elements)
                print(f"   � {element_type.upper().replace('_', ' ')}: {len(elements)} found")
                for i, elem in enumerate(elements[:2]):  # Show first 2
                    location = elem.get("location", {})
                    print(f"      {i+1}. Text: '{elem.get('text', 'N/A')}' | Value: '{elem.get('value', 'N/A')}' at ({location.get('x', 'N/A')}, {location.get('y', 'N/A')})")
        
        if total_displays == 0:
            print("   ⚠️ No display elements detected")
        
        # Buttons
        buttons = self.analysis_results.get("buttons", {}).get("all_buttons", [])
        print(f"\n🔘 INTERACTIVE BUTTONS: {len(buttons)} total")
        if buttons:
            for i, button in enumerate(buttons[:5]):  # Show first 5
                location = button.get("location", {})
                print(f"   {i+1}. '{button.get('text', 'No text')}' ({button.get('tag', 'unknown')}) at ({location.get('x', 'N/A')}, {location.get('y', 'N/A')})")
            if len(buttons) > 5:
                print(f"   ... and {len(buttons) - 5} more buttons")
        else:
            print("   ⚠️ No interactive buttons detected")
        
        print("="*60)
        print("📁 GENERATED FILES:")
        print("   📄 game_analysis_results.json - Complete analysis data")
        print("   🖼️ game_analysis_screenshot.png - Game board screenshot")
        print("   📄 game_page_source.html - Full page HTML source")
        print("="*60)

def main():
    """Main function to run game analysis"""
    analyzer = GameAnalyzer()
    
    print("🎰 AI Gambler King - Teaching Session")
    print("📚 Analyzing Pinata Wins slot game...")
    print("🔗 Target URL: Pinata Wins Game Board")
    
    # Start analysis
    results = analyzer.start_analysis()
    
    if results:
        analyzer.print_summary()
        print("\n✅ Game analysis completed!")
        print("📁 Files generated:")
        print("   - game_analysis_results.json")
        print("   - game_analysis_screenshot.png")
        print("   - game_page_source.html")
        
        # Keep browser open for manual inspection
        input("\n🔍 Browser will remain open for manual inspection. Press Enter to close...")
        
    else:
        print("❌ Game analysis failed!")
    
    # Close browser
    if analyzer.driver:
        analyzer.driver.quit()

if __name__ == "__main__":
    main()
