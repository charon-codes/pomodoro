# Handoff

## Project
Simple Pomodoro timer for Windows. Python 3 + tkinter, single file: main.py.
Run with: python main.py

## Done
- Step 2: window with "25:00" label and a Start button
- Step 3: Start/Pause button, 25-minute countdown using root.after (updates every second)

## Next
- Step 4: let the user change the duration, and add a Reset button

## Decisions
- tkinter chosen because it ships with Python (no extra installs)
- root.after is used instead of a sleep loop, otherwise the window freezes
- One branch per step (e.g. step-3-countdown), merged into main when it works