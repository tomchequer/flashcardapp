import random
from tkinter import *
from numpy import flip
import pandas as pd

BACKGROUNDCOLOR = "#B1DDC6"



#-----------------Logic-----------------#
try:
    raw_data = pd.read_csv('data/word_to_learn.csv')
except FileNotFoundError:
    raw_data = pd.read_csv('data/alemaobruto.csv')
    data = pd.DataFrame(raw_data)
    to_learn = data.to_dict(orient='records')   
else:
    to_learn = raw_data.to_dict(orient='records')


current_card = {}

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/word_to_learn.csv', index=False)
    new_card()

def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    german = current_card['GERMAN']
    english = current_card['ENGLISH']
    canvas.itemconfig(title, text='German/English')
    canvas.itemconfig(word_in_german, text=german)
    canvas.itemconfig(word_in_english, text=english)    
    canvas.itemconfig(background_image, image=card_front)
    canvas.itemconfig(title, text='German/English', fill='black')
    canvas.itemconfig(word_in_german, text=german, fill='black')
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(background_image, image=card_back)
    canvas.itemconfig(title, text='Portuguese', fill='white')
    canvas.itemconfig(word_in_german, text=current_card['PORTUGUESE'], fill='white')
    canvas.itemconfig(word_in_english, text='')
    window.after(5000, func=flip_card)

#-------------------UI----------------#
window = Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50, bg=BACKGROUNDCOLOR)
flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
background_image = canvas.create_image((400, 253),image=card_front, )
title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, "italic"))
word_in_german = canvas.create_text(400, 270, text='Word', font=('Ariel', 40, 'bold'))
word_in_english = canvas.create_text(400, 350, text='Word', font=('Ariel', 40, 'bold'))
canvas.config(bg=BACKGROUNDCOLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

red_image = PhotoImage(file="images/wrong.png")
red_button = Button(image=red_image, width=50, height=50, command=new_card) 
red_button.grid(column=0, row=1)

green_image = PhotoImage(file="images/right.png")
green_button = Button(image=green_image, width=50, height=50, command=is_known) 
green_button.grid(column=1, row=1)

german = Label(text='German')

new_card()

window.mainloop()