import cv2
import numpy as np
from collections import deque
from utils.memory_manager import ai_memory, save_memory  # AI Memory Manager Load

scatter_history = ai_memory.get("scatter_history", deque(maxlen=5))  # AI di yaad da data

def detect_scatter(frame, scatter_template):
    result = cv2.matchTemplate(frame, scatter_template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    loc = np.where(result >= threshold)
    scatter_positions = list(zip(*loc[::-1]))
    scatter_history.append(scatter_positions)  # AI nu yaad rahega!
    save_memory({"scatter_history": list(scatter_history)})  # AI memory save karega
    return scatter_positions

def predict_next_scatter():
    if len(scatter_history) < 5:
        return None
    avg_x = int(np.mean([pos[0] for frame in scatter_history for pos in frame])) if scatter_history else None
    avg_y = int(np.mean([pos[1] for frame in scatter_history for pos in frame])) if scatter_history else None
    return (avg_x, avg_y) if avg_x and avg_y else None
