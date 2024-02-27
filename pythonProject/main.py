from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(canvas_text, text="00:00")


def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_count()
        reps_check = math.floor(reps / 2) * "✔"
        checkmark_label.config(text=reps_check)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer_label.pack()

canvas = Canvas(height=200, width=224, bg=YELLOW, highlightthickness=0)
image_hold = PhotoImage(file="tomato.png")
canvas.create_image(105, 87, image=image_hold)
canvas_text = canvas.create_text(105, 107, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

start_button = Button(text="Start", command=start_count)
start_button.pack(side="left")
start_button.config(pady=3, padx=10)

reset_button = Button(text="Reset", command=reset)
reset_button.pack(side="right")
reset_button.config(pady=3, padx=10)

checkmark_label = Label()
checkmark_label.pack(side="bottom")

window.mainloop()
