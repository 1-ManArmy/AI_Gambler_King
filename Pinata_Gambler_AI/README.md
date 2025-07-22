# AI Gambler - Automated Slot Game Player 🎰

## Overview
AI Gambler is an automated slot game player designed to interact with browser-based slot games. It uses computer vision and automation techniques to detect symbols, calculate winnings, and log game observations. The AI can also observe game states and save results for analysis.

---

## Features
- **Game Automation**: Automatically spins the game and waits for results.
- **Symbol Detection**: Detects all symbols on the game board using template matching.
- **Winning Calculation**: Calculates total winnings based on symbol values.
- **Game State Awareness**: Detects when the game is spinning or idle.
- **Logging**: Logs detected symbols, winnings, and game states to a file.
- **Scalable Configuration**: Easily add or modify symbols and their values in `assets_config.json`.

---

## Requirements
- Python 3.8 or higher
- Dependencies:
  - `opencv-python`
  - `pillow`
  - `pyautogui`
  - `selenium`
  - `python-dotenv`
  - `openai`

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MY-Checkmate/My_Slots_Game.git
   cd My_Slots_Game
---
## 📂 Project Structure
```
My_Slots_Game/
├── ai_gambler.py
├── chroma_brain.py
├── config.py
├── cortex_panel.html
├── cortex_ui.py
├── experience_log.json
├── folder_structure.txt
├── free_spin_tracker.py
├── game_launcher.py
├── get_coordinates.py
├── glow_detector.py
├── hot_mode.py
├── identity_module.py
├── intel_triggers.json
├── log_summary.py
├── memory_blocks.json
├── pixel_click_ai.py
├── project_structure.txt
├── requirements.txt
├── shared_brain.py
├── spin_controller.py
├── symbols_watchlist.txt
├── symbol_tracker.py
├── symbol_value_ai.py
├── test_ai_gambler.py
├── tool_usage_chart.py
├── trainer_engine.py
├── vision_detector.py
├── .env
├── assets/
│   ├── scatter_template.png
│   ├── symbol_spin_button.png
│   ├── game_poster_start.png
│   ├── game_start_button.png
│   ├── maracas_pair.png.png
│   ├── multiplier_x100_template.png
│   ├── multiplier_x2_template.png
│   ├── symbol_A_letter.png
│   ├── symbol_chili_pepper.png
│   ├── symbol_decrease_bet.png
│   ├── symbol_girl.png
│   ├── symbol_increase_bet.png
│   ├── symbol_J_letter.png
│   ├── symbol_K_letter.png
│   ├── symbol_Q_letter.png
│   ├── symbol_shawarma_taco.png
│   ├── symbol_skull.png
│   ├── symbol_sombrero.png
│   ├── symbol_wallet_balance.png
│   └── symbol_winning_bet_lines.png
├── ruleset/
│   └── tactic.json
├── assets_config.json
├── observations.json
├── geckodriver.exe
└── README.md
```

---

## Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

---


### **Set Up and Run AI Gambler for Slot Game Automation**

#### 1. **Create and Activate a Virtual Environment**:

To ensure your project dependencies are isolated, create and activate a virtual environment:

* On **Windows**:

  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

* On **macOS/Linux**:

  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

#### 2. **Install Dependencies**:

Install all necessary dependencies as defined in `requirements.txt`:

```bash
pip install -r requirements.txt
```

#### 3. **Add OpenAI API Key to `.env` File**:

Create a `.env` file and add your OpenAI API key to it:

```plaintext
OPENAI_API_KEY=sk-your-openai-api-key
```

#### 4. **Configuration**

##### **Game Assets**:

Define the symbols, templates, and values in `assets_config.json` for the game. Example:

```json
{
    "symbols": {
        "scatter": {"template": "scatter_template", "value": 100},
        "x2_multiplier": {"template": "multiplier_x2_template", "value": 50},
        "girl": {"template": "symbol_girl", "value": 30},
        "chili_pepper": {"template": "symbol_chili_pepper", "value": 20}
    }
}
```

##### **Game Region**:

Set the game screen region for symbol detection and automation in `ai_gambler.py`. Update the `REGION` variable as per your game’s resolution:

```python
REGION = (500, 300, 1200, 700)  # Adjust based on your game screen resolution
```

#### 5. **Usage**

##### **Running the AI Gambler Script**:

To start the AI and let it automate the slot game, run the following command:

```bash
python ai_gambler.py
```

##### **Follow the Prompts**:

The script will ask you to:

1. **Enter the scatter threshold** (or press Enter to use the default value).
2. **Enter the game screen region** (or press Enter to use the default region defined in `ai_gambler.py`).

##### **Log Output**:

The script will log the following details to the console and save them in `observations.json`:

* Detected symbols.
* Winnings.
* Game states.

Example log output in `observations.json`:

```json
{
    "timestamp": "2025-05-09 16:00:00",
    "state": "idle",
    "symbols_detected": {
        "scatter": 2,
        "girl": 3,
        "A": 1
    },
    "win": true,
    "total_value": 130
}
```

#### 6. **Contributing**

Feel free to fork this repository and submit pull requests to improve the script or add new features!

#### 7. **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

#### 8. **Disclaimer**

This project is for educational purposes only. Please use responsibly and ensure compliance with the terms and conditions of the game you are automating.

