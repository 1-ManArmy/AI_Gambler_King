#!/usr/bin/env python3
"""
🧪 AI Gambler King - Module Test Suite
Tests all core modules to ensure they're working properly
"""

import sys
import importlib
import traceback

def test_import(module_name, description=""):
    """Test if a module can be imported successfully"""
    try:
        importlib.import_module(module_name)
        print(f"✅ {module_name} - {description}")
        return True
    except Exception as e:
        print(f"❌ {module_name} - {description}")
        print(f"   Error: {e}")
        return False

def main():
    print("🧪 Testing AI Gambler King Modules...\n")
    
    # Test core dependencies
    print("📦 Testing Core Dependencies:")
    deps_passed = 0
    deps_total = 7
    
    deps_passed += test_import("selenium", "Web automation framework")
    deps_passed += test_import("cv2", "OpenCV for image processing") 
    deps_passed += test_import("numpy", "Numerical computing")
    deps_passed += test_import("pyautogui", "GUI automation")
    deps_passed += test_import("PIL", "Python Imaging Library")
    deps_passed += test_import("requests", "HTTP library")
    deps_passed += test_import("openai", "OpenAI API client")
    
    print(f"\n📊 Dependencies: {deps_passed}/{deps_total} passed\n")
    
    # Test project modules
    print("🎮 Testing Project Modules:")
    modules_passed = 0
    modules_total = 8
    
    modules_passed += test_import("utils.browser_login", "Browser automation")
    modules_passed += test_import("utils.image_processing", "Image processing utilities")
    modules_passed += test_import("utils.click_controller", "Click automation")
    modules_passed += test_import("utils.screen_capture", "Screen capture")
    modules_passed += test_import("utils.memory_manager", "Memory management")
    
    # Test AI modules
    modules_passed += test_import("ai_gambler", "Main AI gambler")
    modules_passed += test_import("chroma_brain", "Chrome brain module")
    modules_passed += test_import("symbol_tracker", "Symbol tracking")
    
    print(f"\n📊 Project Modules: {modules_passed}/{modules_total} passed\n")
    
    # Test main application
    print("🚀 Testing Main Application:")
    try:
        # Test if main.py can be parsed with UTF-8 encoding
        with open("main.py", 'r', encoding='utf-8') as f:
            compile(f.read(), "main.py", "exec")
        print("✅ main.py - Syntax check passed")
        main_passed = True
    except Exception as e:
        print(f"❌ main.py - Syntax error: {e}")
        main_passed = False
    
    # Final summary
    total_passed = deps_passed + modules_passed + (1 if main_passed else 0)
    total_tests = deps_total + modules_total + 1
    
    print(f"\n{'='*50}")
    print(f"🎯 FINAL RESULTS: {total_passed}/{total_tests} tests passed")
    
    if total_passed == total_tests:
        print("🎉 ALL TESTS PASSED! AI Gambler King is ready to run!")
    elif total_passed >= total_tests * 0.8:
        print("⚠️ Most tests passed. Minor issues may exist.")
    else:
        print("❌ Multiple issues detected. Please check dependencies.")
    
    print(f"{'='*50}")
    
    return total_passed == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
