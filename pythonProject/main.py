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


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_count():
    countdown(5*60)


def countdown(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, countdown, count - 1)


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

reset_button = Button(text="Reset")
reset_button.pack(side="right")
reset_button.config(pady=3, padx=10)

checkmark_label = Label(text="✔")
checkmark_label.pack(side="bottom")

window.mainloop()
