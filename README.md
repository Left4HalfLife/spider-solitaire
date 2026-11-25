# spider-solitaire
ai slop spider solitaire

A complete Spider Solitaire game in a single, self-contained `index.html`:
no external scripts, fonts or images. Cards are drawn with Unicode and CSS.

## Play

Download `index.html` and open it in any modern browser (desktop or mobile).
No internet connection or server is needed.

## Features

- **1, 2 or 4 suits**: choose from the mode dropdown (this starts a new game).
- **New game**, **Undo** (unlimited) and **Hint** (press repeatedly to cycle
  through every legal move, best first; it suggests dealing when that is the
  only option).
- **Automatic game-over detection**: when no sequence of moves can reveal a
  card, complete a suit or allow a deal (only loops remain), the game says so
  and offers Undo, New game or Change mode.
- Tap or click a card to auto-move it, or drag it. Tap the stock (top right)
  to deal a row.
- Responsive layout for phones and desktops; the game is saved in the browser
  and restored when you reopen the file.

### Keyboard shortcuts

| Key | Action |
| --- | --- |
| `Ctrl+Z` / `U` | Undo |
| `H` | Hint |
| `D` | Deal from the stock |
| `N` | New game |
| `Esc` | Close dialog |
