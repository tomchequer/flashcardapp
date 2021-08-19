from tkinter import *


BACKGROUNDCOLOR = "#B1DDC6"

window = Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50, bg=BACKGROUNDCOLOR)


canvas = Canvas(width=800, height=526)

card_front = PhotoImage("images/card_front.png")
canvas.create_image((400, 263),image=card_front)
canvas.grid(column=0, row=0)


german = Label(text='German')

window.mainloop()