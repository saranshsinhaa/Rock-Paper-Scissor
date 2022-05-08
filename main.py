#-------------------------------------------------------------------------------------------

from tkinter import *
from random import randint

#-------------------------------------------------------------------------------------------


root=Tk()
root.title("Rock, Paper, Scissors")
root.geometry("700x500")
root.config(bg="#929292")


#-------------------------------------------------------------------------------------------


home=PhotoImage(file='images/home.png')
rock=PhotoImage(file='images/rock.png')
paper=PhotoImage(file='images/paper.png')
scissor=PhotoImage(file='images/scissors.png')


#-------------------------------------------------------------------------------------------

image_label=Label(root, image=home)
image_label.pack(padx=10, pady=10)

#-------------------------------------------------------------------------------------------


choice_list=[rock,paper,scissor]


#-------------------------------------------------------------------------------------------

def pick():
    random_number=randint(0,2)
    image_label.config(image=choice_list[random_number])

#-------------------------------------------------------------------------------------------

start_button=Button(root, font=('showcard gothic',7,"bold"),bg="#1995ED",
                    width=20,height=20, text="Start!", bd=2, relief='raised', command=pick)
start_button.pack(padx=10, pady=10)

#-------------------------------------------------------------------------------------------


root.mainloop()

#-------------------------------------------------------------------------------------------