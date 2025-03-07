import pyautogui
import time
from utils.image_processing import predict_next_scatter

def stop_roll():
    prediction = predict_next_scatter()
    if prediction:
        x, y = prediction
        print(f'AI Predicting Scatter at: {x}, {y}')
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.05)
        pyautogui.click()
        print('🎯 AI Stopped Roll at Perfect Timing!')
    else:
        print('⚠️ Not enough data for AI prediction. Waiting...')
