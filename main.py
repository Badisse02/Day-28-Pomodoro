from tkinter import *
from math import *
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
ident = NONE

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    window.bell()
    if reps in [1, 3, 5, 7]:
        count_down(WORK_MIN * 60)
        timer.config(text=" Work ", foreground=GREEN)
    elif reps in [2, 4, 6]:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Break", foreground=PINK)
        check_mark["text"] += "✔"
    else:
        count_down(LONG_BREAK_MIN * 60)
        check_mark["text"] += "✔"
        timer.config(text="Break", foreground=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global ident
    count_min = floor(count / 60)
    count_sec = int(count % 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count < 0 and reps == 8:
        count_min = "00"
        count_sec = "00"
    canvas.itemconfig(counter_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        ident = window.after(1000, count_down, count - 1)
    else:
        if reps < 8:
            start_timer()


def reset_counter():
    global reps, ident
    reps = 0
    canvas.itemconfig(counter_text, text="00:00")
    timer.config(text="Timer", foreground=GREEN)
    check_mark["text"] = ""
    window.after_cancel(ident)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro Program")


timer = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
timer.grid(row=1, column=2)

canvas = Canvas(width=200, height=233, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
counter_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset_counter)
reset_button.grid(row=3, column=3)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15))
check_mark.grid(row=4, column=2)

window.mainloop()
