
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = NONE
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import math
def count_down(count):
    count_min = math.floor(count/60)
    count_second = count%60
    if count_second < 10:
        count_second=f"0{count_second}"


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_second}")
    print(count)
    if count >0:
        global  timer
        timer = window.after(1000,count_down,count-1)
    else:
        click_start_button()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark+="✓"
        click.config(text=f"{mark}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


label= Label(text="Timer")
label.config(fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,"bold"))
label.grid(row=0,column=1)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)
# count_down(5)
def click_start_button():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    work_break_sec =SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # count_down(5*60)
    # count_down(work_sec)
    # count_down(work_break_sec)
    if reps%8 == 0:
        count_down(long_break_sec)
        label.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(work_break_sec)
        label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="WORK",fg=GREEN)

    print("start button")
start_button = Button(text="Start",command=click_start_button,bg=YELLOW,highlightthickness=0)

def click_reset_button():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    click.config(text="")
    global  reps
    reps=0
    print("reset button ")
reset_button = Button(text="Reset",command=click_reset_button,highlightthickness=0, bg=YELLOW)
start_button.grid(row=2,column=0)
reset_button.grid(row=2,column=2)


click = Label(bg=YELLOW,fg=GREEN,font=(GREEN,15,"bold"))
click.grid(row=3,column=1)

window.mainloop()