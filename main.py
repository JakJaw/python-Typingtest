from tkinter import *
from random import choice

Words = ["crisis", "step", "habit", "hour", "mean", "favor", "misery", "extend",
         "temple", "meadow", "presidency", "barrel", "voucher", "refrigerator", "rain",
         "forward", "halt", "brake", "deprive", "digital", "blue", "know", "husband",
         "trolley", "be", "wine", "selection", "pleasant", "snub", "sign", "excuse",
         "dominate", "fascinate", "economic", "even", "abstract", "quota", "jewel"]
Title_text = "               How fast are you? Do the one-minute typing test to find out.\nPress the space bar after " \
             "each word. Later u will get words per minute score"
Entry_font = ("Arial", 20, "bold")
Font_main = ("Arial", 10, "bold")
Font_word = ("Arial", 22, "bold")
Time = 0
Score = 0
Rep = 0
User_word = ""
Word = ""


def random_word():
    return str(choice(Words) + " ")


def check(key):
    global User_word, Word, Score
    User_word = entry.get()

    if User_word == Word:
        Score += 1
        entry.delete(0, "end")
        Word = random_word()
        canvas_word.itemconfig(word_text, text=f"{Word}")
        start()
    elif User_word != Word:
        entry.delete(0, "end")
        start()


def start():
    window.update()
    global Time, Score, Rep, Word
    if Rep == 0:
        Time = 60
        Score = 0
        Word = random_word()
        canvas_word.itemconfig(word_text, text=f"{Word}")
        canvas_text.itemconfig(timer_text, text=f"Time start when u enter first word", font=Font_word)
        canvas_score.itemconfig(score_text, text=f"Score: {Score}")
        Rep += 1
    elif Rep > 0:
        while Time > 0:
            canvas_word.itemconfig(word_text, text=f"{Word}")
            canvas_text.itemconfig(timer_text, text=f"Time left: {round(Time)}", font=Font_word)
            canvas_score.itemconfig(score_text, text=f"Score: {Score}")
            window.update()
            window.after(100)
            Time -= 0.1
        canvas_score.itemconfig(score_text, text=f"Final score is {Score} words per minute!!!")
        canvas_text.itemconfig(timer_text, text="Thank u for using my program")
        canvas_word.itemconfig(word_text, text="")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Typing Test")
window.config(padx=50, pady=50)
window.geometry("700x900")
window.resizable(False, False)
window.configure(background='Black')

canvas = Canvas(height=400, width=540)
logo_img = PhotoImage(file="1.png")
canvas.create_image(270, 200, image=logo_img)
canvas.grid(row=1, column=1)

canvas_word = Canvas(width=500, height=30, bg="black", highlightthickness=0)
word_text = canvas_word.create_text(250, 15, font=Font_word, fill="orange", text="")
canvas_word.grid(column=1, row=3)

canvas_score = Canvas(width=500, height=30, bg="black", highlightthickness=0)
score_text = canvas_score.create_text(250, 15, font=Font_word, fill="green", text="")
canvas_score.grid(column=1, row=5)

canvas_text = Canvas(width=500, height=30, bg="black", highlightthickness=0)
timer_text = canvas_text.create_text(250, 15, font=Font_main, fill="white", text=Title_text)
canvas_text.grid(column=1, row=0)

entry = Entry(width=30, font=Entry_font)
entry.grid(row=4, column=1)
entry.focus()

quit_button1 = Button(bg="red", text="Quit", command=window.destroy).grid(column=0, row=3)
start_button = Button(bg="green", text="Start", command=start).grid(column=0, row=5)

window.bind("<space>", check)
window.mainloop()
