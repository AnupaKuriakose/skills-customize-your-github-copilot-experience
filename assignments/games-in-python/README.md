
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game to practice string manipulation, loops, conditionals, and handling user input. The program should provide a clear playable loop and win/lose feedback.

## 📝 Tasks

### 🛠️	Implement Hangman core gameplay

#### Description
Create the playable Hangman game: randomly pick a secret word, accept single-letter guesses, reveal correct letters in the displayed word, and track remaining incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (use `random.choice`).
- Prompt the player for single-letter guesses and treat input case-insensitively.
- Display current progress with underscores for unknown letters (e.g., `p _ t _ o n`).
- Show a list of letters already guessed and ignore repeated guesses (do not penalize repeats).
- Track and display remaining incorrect attempts (e.g., start with 6 attempts).
- End the game with a clear win or lose message and reveal the secret word on loss.

Example gameplay snippet:
```
Word: _ _ _ _ _
Guessed: a, e
Attempts left: 4
Enter a letter: o
Correct! Word: _ o _ _ _
```

### 🛠️	Optional: Enhancements

#### Description
Add extra features to improve playability and user experience.

#### Requirements
Completed program may (optional):

- Offer difficulty levels that change allowed attempts or select longer/shorter words.
- Load words from an external file (e.g., `words.txt`) instead of a hardcoded list.
- Display simple ASCII-art hangman stages as attempts are lost.
- Save and display high scores or fastest wins in a small local file.

--- 

If you want, I can:
- produce a ready-to-run `starter-code.py` for this assignment, or
- show the exact patch you can apply to `assignments/games-in-python/README.md`.
Which would you prefer?
