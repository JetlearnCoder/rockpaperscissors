from tkinter import*
import tkinter.font as font

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("600x300")

gametitle = Label(window,text = "Rock Paper Scissors",
                    font = font.Font(size = 25)).place(x = 135,y = 25)

winnerlabel = Label(window,text = "Lets Start!",
                    font = font.Font(size = 15), fg = "green").place(x = 200, y = 75)

input_frame = Frame(window)
input_frame.place(x = 20, y = 110)

options = Label(input_frame,text = "Your options:",
                font = font.Font(size = 12),fg = "grey")
rock_btn = Button(input_frame,text = "Rock", width = 10,padx = 8, pady = 5)
                    #padding creates more space inside the button
paper_btn = Button(input_frame,text = "Paper", width = 10,padx = 8, pady = 5)
scissors_btn = Button(input_frame,text = "Scissors", width = 10,padx = 8, pady = 5)

score_frame = Frame(window)
score_frame.place(x = 20 , y = 220)
scorelabel = Label(score_frame,text = "Score:",
                   font = font.Font(size = 12),fg = "grey")



options.grid(row = 0, column = 0)
rock_btn.grid(row = 1, column = 1)
paper_btn.grid(row = 1, column = 2)
scissors_btn.grid(row = 1, column = 3)

scorelabel.grid(row = 0, column = 0)

window.mainloop()