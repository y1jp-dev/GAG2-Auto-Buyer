# GAG2 Afker

Auto-clicker and anti-AFK tool for Roblox Grow a Garden 2. Keeps you active in-game by spam clicking and periodically moving your character forward and backward.

## Features

- Spam clicks on a set position to continuously buy items
- Periodic forward/backward movement to prevent idle kick
- Press F6 to auto-capture mouse position and start
- Press F6 again to stop
- Clean dark GUI
- Adjustable click speed, move time, and move delay

## Requirements

- Python 3.7 or higher
- Windows (pydirectinput is Windows-only)

## Installation

1. Clone the repo:

git clone https://github.com/y1jp-dev/GAG2-Afker.git
cd GAG2-Afker

2. Install dependencies:

pip install -r requirements.txt

3. Run the script:

python GAG2-Afker.py

## Usage

1. Launch Roblox and open Grow a Garden 2
2. Enable Shift Lock in Roblox settings (prevents camera drift)
3. Hover your mouse over the buy button
4. Press *F6* to start
5. Press *F6* again to stop
6. Close the window or press the X to quit

### Settings

| Setting     | Default | Description                       |
|-------------|---------|-----------------------------------|
| Click Speed | 0.1 sec | Delay between each click          |
| Move Time   | 0.5 sec | How long to walk forward/backward |
| Move Delay  | 60 sec  | Time between walk cycles          |

### Emergency Stop

Slam your mouse to the top-left corner of the screen to instantly kill the script.

## Dependencies

- pyautogui
- keyboard
- pydirectinput
- tkinter (built-in)

## Notes

- Stand facing a wall or in a corner so the movement doesn't walk you off ledges
- Make sure your inventory isn't full or the clicks won't register
- The script captures your mouse position on F6 press, no manual coordinate entry needed.
