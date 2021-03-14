from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}




try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card =  random.choice(to_learn)
    canvas.itemconfig(title,text  = "French",fill="Black")
    canvas.itemconfig(word, text=current_card["French"],fill="Black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000,flip_card)





def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def isKnown():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



window = Tk()
window.title("Flash Card App")
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR )

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width = 800, height = 525,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 262.5, image=card_front_img)

canvas.grid(row=0, column=0, columnspan=2)

title = canvas.create_text(400,150,text="Title", font=('Arial', 40, "italic"))
word = canvas.create_text(400,263,text="Word", font=('Arial', 40, "bold"))


correct_image= PhotoImage(file='./images/right.png')
correct_button = Button(image=correct_image,highlightthickness=0, command=isKnown)
correct_button.grid(row = 1 , column = 0)

wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row = 1, column=1)


next_card()




window.mainloop()