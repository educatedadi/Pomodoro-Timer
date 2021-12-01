from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#11E100"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.15
reps = 0
tick = '✔'
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, tick
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='TIMER', fg=PINK)
    tick_label.config(text=' ')
    reps = 0
    tick = '✔'


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, timer_label
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        timer_label.config(text='WORK', fg=GREEN)
        count_down(work_sec)

    elif reps % 8 == 0:
        timer_label.config(text='Break', fg=PINK)
        count_down(long_break)

    else:
        timer_label.config(text='Break', fg=RED)
        count_down(short_break)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global tick, timer
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = screen.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            tick_label.config(text=tick)
            tick += '✔'

        if reps % 8 == 0:
            reset_timer()
        else:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title('Pomodoro Timer')
screen.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='TIMER', font=(FONT_NAME, 32, 'bold'), fg=PINK, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.grid(row=1, column=1)

start_btn = Button(text='START', command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text='RESET', command=reset_timer)
reset_btn.grid(row=2, column=2)

tick_label = Label(text=' ', font=(FONT_NAME, 18, 'bold'), fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)



screen.mainloop()
