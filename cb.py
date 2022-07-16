import tkinter as tk                        ###   requirements 
from tkinter import *
from typing import Collection
from PIL import Image, ImageTk              ###   requirements

root = tk.Tk()                    ### START of APP  ###

canvas = tk.Canvas(root, width=350, height=400)     ###  How big the window is 
canvas.grid(columnspan=4, rowspan=4)
#logo
logo = Image.open('cb.png')                     ### Where the logo img is 
logo = ImageTk.PhotoImage(logo)                     
logo_lable = tk.Label(image=logo)
logo_lable.image = logo
logo_lable.grid(columnspan=4, column=0, row=0)

#instructions
instructions = tk.Label(root, text=             ### Main Question
"How many pallets? ", font= "Cambria")
instructions.grid(columnspan=4, column=0, row=1)    

def get_count(entryWidget):                 ### Math to get cornerboard count from entry
    value = entryWidget.get()
    try:
        return int (value) * 4
    except ValueError:
        return None

e = Entry(root, width=50)                  ### Entry field box 
e.grid(columnspan=4, column=0, row=2)


def myClick():
    myLabel = Label (root, text= 
    get_count(e), font = "cambira")            
    myLabel.grid(columnspan=3, column=0, row=3)
   

    myCornerBoards = Label (root, text= 
    "CornerBoards", font= "cambria")
    myCornerBoards.grid(columnspan=3, column=1, row=3)


myButton = Button(root, text="Enter", command=myClick)
myButton.invoke()
myButton.grid(columnspan=4, column=0, row=4)

root.bind('<Return>', lambda event=None: myButton.invoke())

root.mainloop()                  ### END of APP ###

