# Pomodoro Timer ⚡⚡⚡

This Python script implements a Pomodoro timer using the Tkinter library. The Pomodoro Technique is a time management method that uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks.

## Functionality

- The timer runs for 25 minutes of work time followed by a 5-minute short break.
- After completing 4 work sessions, a longer break of 20 minutes is initiated.
- Users can start, pause, and reset the timer.

  
![Pomodoro](https://github.com/HarshanaPrabhath/Pomodora_time_sheduel_app_Python/assets/132127313/67f65265-5ebe-40b6-8f03-e89d93c61d75)


## Features
- **Work Session**: 25 minutes
- **Short Break**: 5 minutes
- **Long Break**: 20 minutes
- Display of checkmarks to indicate completed work sessions.

## UI Components
- Timer display
- Start button
- Reset button
- Checkmarks to indicate completed work sessions

## Usage
1. Click the "Start" button to initiate the Pomodoro timer.
2. The timer will display the remaining time for the current session (work or break).
3. After completing a work session, the timer will automatically switch to a short break. Similarly, after completing 4 work sessions, the timer will switch to a long break.
4. Click the "Reset" button to reset the timer and start a new session.

## Components Used
- **Tkinter**: GUI library for Python.
- **Math Module**: For mathematical calculations.
- **PhotoImage**: For loading and displaying images.

## How It Works
- The script initializes a Tkinter window with various UI components such as labels, buttons, and canvas for the timer display.
- It utilizes the Pomodoro technique to manage work and break sessions.
- The countdown mechanism updates the timer display every second.
- Upon completion of each session, the script updates the session type and initiates the next session accordingly.



