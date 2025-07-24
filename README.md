# AI Gambler King - Automated Slot Game Player 🎰

## Overview
AI Gambler King is an advanced automated slot game player designed to interact with browser-based slot games. It uses sophisticated computer vision, artificial intelligence, and automation techniques to detect symbols, calculate winnings, make intelligent betting decisions, and log game observations. The AI can observe game states, learn from patterns, and save results for analysis.

---

## Features
- **Advanced Game Automation**: Automatically spins the game and waits for results with intelligent timing.
- **AI-Powered Symbol Detection**: Detects all symbols on the game board using advanced computer vision and template matching.
- **Intelligent Betting Strategy**: Makes smart betting decisions based on pattern analysis and confidence levels.
- **Machine Learning**: Learns from outcomes and adapts strategies over time.
- **Real-time Decision Making**: Uses enhanced brain system for complex game analysis.
- **Winning Calculation**: Calculates total winnings based on symbol values and game patterns.
- **Game State Awareness**: Detects when the game is spinning, idle, or in bonus modes.
- **Comprehensive Logging**: Logs detected symbols, winnings, decisions, and game states to files.
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
   git clone https://github.com/1-manarmy/AI_Gambler_King.git
   cd AI_Gambler_King
---
## 📂 Project Structure

```
AI_Gambler_King/
├── main.py                    # Main entry point
├── ai_gambler.py             # Core AI gambling engine
├── ai_gambler_customized.py  # Custom configuration loader
├── enhanced_brain.py         # Advanced AI brain system
├── intelligent_agent.py      # Intelligent game agent
├── chroma_brain.py           # Chrome brain module
├── cortex_batch.py           # Batch processing
├── cortex_brain_llm.py       # LLM integration
├── cortex_panel.html         # Control panel UI
├── cortex_ui.py              # User interface
├── shared_brain.py           # Shared brain functions
├── symbol_tracker.py         # Symbol tracking system
├── symbol_value_ai.py        # Symbol value analysis
├── vision_detector.py        # Computer vision detector
├── game_launcher.py          # Game launcher
├── spin_controller.py        # Spin control logic
├── bet_adjuster.py           # Betting adjustment
├── bet_optimizer.py          # Betting optimization
├── hot_mode.py               # Hot mode functionality
├── free_spin_tracker.py      # Free spin tracking
├── glow_detector.py          # Special effects detection
├── alert_engine.py           # Alert system
├── auto_ingest.py            # Auto data ingestion
├── auto_sentinel.py          # Monitoring system
├── brain_backup.py           # Brain backup system
├── trainer_engine.py         # Training engine
├── identity_module.py        # Identity management
├── pixel_click_ai.py         # Pixel-based clicking
├── log_summary.py            # Log summarization
├── tool_usage_chart.py       # Usage analytics
├── test_ai_gambler.py        # Test suite
├── test_modules.py           # Module testing
├── experience_log.json       # Experience data
├── assets_config.json        # Asset configuration
├── memory_blocks.json        # Memory storage
├── intel_triggers.json       # Intelligence triggers
├── symbols_watchlist.txt     # Symbol watchlist
├── batch_log.txt             # Batch execution log
├── requirements.txt          # Python dependencies
├── geckodriver.exe           # WebDriver executable
├── utils/                    # Utility modules
│   ├── browser_login.py      # Browser automation
│   ├── image_processing.py   # Image processing
│   ├── click_controller.py   # Click automation
│   ├── screen_capture.py     # Screen capture
│   └── memory_manager.py     # Memory management
├── assets/                   # Game assets and templates
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
├── ruleset/                  # Game rules and tactics
│   └── tactic.json
├── intel/                    # Intelligence data
│   ├── intel_triggers.json
│   └── symbols_watchlist.txt
├── memory/                   # Memory and learning data
│   ├── experience_log.json
│   └── freespins.json
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

