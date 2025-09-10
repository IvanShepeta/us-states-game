#  US States Game 🗺️

This is a simple learning game where you have to guess the names of the U.S. states. Built using Python’s **turtle** module and data handling with `pandas`.

---

##  Game Overview

- A blank map of the USA is displayed.
- You are prompted to enter the name of a U.S. state.
- If correct, the state name is written on the map at its location.
- The goal is to name as many states as possible.
- The game ends when you’ve guessed all 50 states or if you choose to exit.

---

##  Files in the Repository

- **`main.py`** – The main script that runs the game:
  - Loads the blank map and CSV data.
  - Prompts for user input and validates guesses.
  - Writes correct answers onto the map.

- **`50_states.csv`** – Contains data for all 50 U.S. states:
  - Columns: `state`, `x`, `y` — state name and position coordinates for text placement.

- **`blank_states_img.gif`** – Background image of the blank U.S. map.

- **`mis_state.csv`** – (Optional) Stores states you missed (if implemented).

---

##  How to Play

```bash
git clone https://github.com/IvanShepeta/us-states-game.git
cd us-states-game
python main.py
