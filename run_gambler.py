#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Gambler King - Quick Start
Quick way to run the Pinata Wins controller
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pinata_wins_controller import PinataWinsController

def main():
    print("🎯 AI Gambler King - Quick Start")
    print("=" * 40)
    print("🎰 Target: Pinata Wins Slot Game")
    print("🎮 Mode: Intelligent Game Control")
    print("=" * 40)
    
    print("\n🚀 What this will do:")
    print("   1. Open browser to Pinata Wins game")
    print("   2. Load game board (default bet: 1.00 Baht)")
    print("   3. Wait for your command to start playing")
    print("   4. Provide manual or auto-play options")
    
    response = input("\n🎮 Start AI Gambler? (y/n): ").lower()
    
    if response == 'y':
        controller = PinataWinsController()
        
        if controller.start_game_session():
            print("\n🎉 Game session started successfully!")
            print("🎯 Game board is loaded and ready!")
            
            # Show options
            while True:
                print("\n🎮 Game Control Options:")
                print("1. 🎲 Auto-play (5 spins)")
                print("2. 🎮 Manual control mode")
                print("3. 📸 Take screenshot")
                print("4. 🔚 Exit")
                
                choice = input("\nSelect option (1-4): ").strip()
                
                if choice == "1":
                    controller.auto_play_session(5)
                elif choice == "2":
                    controller.manual_control_mode()
                elif choice == "3":
                    controller.capture_game_state()
                elif choice == "4":
                    break
                else:
                    print("❌ Invalid choice, try again")
            
            controller.close_session()
        else:
            print("❌ Failed to start game session")
    else:
        print("👋 Cancelled. Run again when ready!")

if __name__ == "__main__":
    main()
