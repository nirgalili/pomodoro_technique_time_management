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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# window

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=30, bg=YELLOW)

# canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# labels

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer.grid(column=2, row=1)

check_marks = Label(text=" ✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=2, row=4)

# bottons

timer = Button(text="Start", fg="black", bg="white", font=(FONT_NAME, 10))
timer.grid(column=1, row=3)

reset = Button(text="Reset", fg="black", bg="white", font=(FONT_NAME, 10))
reset.grid(column=3, row=3)



window.mainloop()