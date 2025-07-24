#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Gambler King - Teaching Session Runner
Run this to teach the AI about Pinata Wins game interface
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from game_analyzer import GameAnalyzer

def main():
    print("🎯 AI Gambler King - Teaching Session")
    print("=" * 50)
    print("🎰 Target Game: Pinata Wins")
    print("🎯 Objective: Analyze game interface and teach AI")
    print("=" * 50)
    
    # Start the teaching session
    analyzer = GameAnalyzer()
    
    print("\n🚀 Starting game analysis...")
    print("📚 This will:")
    print("   1. Open browser directly to Pinata Wins")
    print("   2. Analyze all game controls and buttons")
    print("   3. Map the game board layout")
    print("   4. Identify betting controls")
    print("   5. Capture game state and screenshots")
    print("   6. Generate detailed analysis report")
    
    response = input("\n🎮 Start teaching session? (y/n): ").lower()
    
    if response == 'y':
        results = analyzer.start_analysis()
        
        if results:
            print("\n✅ Teaching session completed successfully!")
            print("\n📊 Generated Files:")
            print("   📄 game_analysis_results.json - Detailed analysis data")
            print("   🖼️ game_analysis_screenshot.png - Game screenshot")
            print("   📄 game_page_source.html - Page source code")
            
            print("\n🧠 AI has learned:")
            print("   🎯 Game layout and structure")
            print("   🎮 All clickable buttons and controls")
            print("   💰 Betting interface elements")
            print("   📊 Display and information panels")
            print("   🎰 Game board positioning")
            
            print("\n🎉 Ready for next phase: Implementing gameplay logic!")
        else:
            print("\n❌ Teaching session failed. Please check logs.")
    else:
        print("📚 Teaching session cancelled.")
    
    print("\n🎯 AI Gambler King teaching session complete!")

if __name__ == "__main__":
    main()
