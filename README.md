# Connect 4

**Play Connect 4 against an alpha-beta search bot, with a pygame interface.**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![pygame](https://img.shields.io/badge/pygame-2-green)

## How the Bot Works

- **Minimax with alpha-beta pruning,** searching 4 moves ahead by default.
- **A single shared board:** instead of copying the board at every node, the search drops a coin, recurses, then removes the coin. This keeps memory use flat and avoids allocating a new board per position.
- **Heuristic evaluation:** non-winning positions are scored by counting each player's runs of 1, 2 and 3 coins, with longer runs weighted 10 times more. Four in a row is scored as a decisive win.

## Running

```bash
pip install pygame
python3 main.py
```

You play as yellow. Choose a column with `←` `→` (or `A` `D`), and drop your coin with `Space`, `S` or `Enter`. The bot replies straight away.

## Status

This is an early prototype. The bot and board work, but win detection in the interface, restarting and choosing difficulty or colour aren't finished yet. For a more complete, reusable version of the same search, see [generic_minimaxer](https://github.com/nagahole/generic_minimaxer).

## Project Structure

```
├── main.py              # pygame window and main loop
└── src/
    ├── game.py          # Rendering and input handling
    ├── gamestate.py     # Turn management and bot moves
    └── port/            # Board, players, evaluation and alpha-beta search
```
