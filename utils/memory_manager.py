import json
import os

MEMORY_FILE = "data/memory.json"

def load_memory():
    """ Load AI memory from file """
    if not os.path.exists(MEMORY_FILE):
        return {"scatter_history": []}
    
    with open(MEMORY_FILE, "r") as file:
        return json.load(file)

def save_memory(memory):
    """ Save AI memory to file """
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

# Initialize memory
ai_memory = load_memory()
