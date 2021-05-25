from  tkinter import *
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
def reset_time():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    if reps % 2 == 0 :
        count_down(short_break_sec)
        timer_label.config(text="Short Break" , fg=PINK)
    elif reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work Time" , fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min_remaining = math.floor(count/60)
    sec_remaining = count % 60

    if (sec_remaining) < 10:
        sec_remaining = f"0{sec_remaining}"
    canvas.itemconfig(timer_text, text=f"{min_remaining}:{sec_remaining}")
    if count > 0:
        global timer

        timer = window.after(1000, count_down, count-1)
    else:
        global reps
        start_timer()
        mark = ""
        number_of_sessions = math.floor(reps/2)
        for _ in range(number_of_sessions):
            mark += "✔"
        tick_label.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold") )
canvas.grid(row=1,column = 1)


timer_label = Label( text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)
timer_label.config(pady=20, padx=20)

start_button = Button(text="Start",  font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(command=reset_time, text="Reset" ,font=(FONT_NAME, 10, "bold") )
reset_button.grid(column=2, row =2)

tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)




















window.mainloop()