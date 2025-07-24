#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Gambler King - Pinata Wins Quick Start
Ready-to-use controller based on game analysis
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pinata_wins_player import PinataWinsPlayer

def main():
    print("🎰 AI GAMBLER KING - PINATA WINS")
    print("=" * 40)
    print("🎯 Ready to play Pinata Wins!")
    print("💰 Default bet: 1.00 Baht")
    print("🎮 Coordinate-based control system")
    print("=" * 40)
    
    print("\n🧠 What the AI has learned:")
    print("   ✅ Game loads in 60-90 seconds")
    print("   ✅ Manual START button click required")
    print("   ✅ Game canvas at (374, 0) - size 289x515")
    print("   ✅ Game center point: (518, 257)")
    print("   ✅ Estimated control coordinates mapped")
    
    response = input("\n🚀 Start Pinata Wins session? (y/n): ").lower()
    
    if response == 'y':
        player = PinataWinsPlayer()
        
        print("\n🎮 Starting session...")
        if player.start_game_session():
            print("\n🎉 Session started! Choose your mode:")
            print("1. 🎯 Test single spin")
            print("2. 🤖 Auto-play 3 spins")
            print("3. 🎮 Manual control")
            
            mode = input("\nSelect mode (1-3): ").strip()
            
            if mode == "1":
                print("🎲 Testing single spin...")
                if player.click_spin():
                    player.wait_for_spin_complete()
                    player.capture_result()
                    print("✅ Test completed!")
                    
            elif mode == "2":
                print("🤖 Auto-play mode...")
                player.auto_play_session(3)
                
            elif mode == "3":
                print("🎮 Manual control mode...")
                player.manual_control()
            
            else:
                print("❌ Invalid selection")
        
        player.close_session()
        
    else:
        print("👋 Session cancelled")
    
    print("\n🎯 Thanks for using AI Gambler King!")

if __name__ == "__main__":
    main()
