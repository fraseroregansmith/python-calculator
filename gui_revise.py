# Fraser O'Regan Smith
# 15/9/22

# *********************************
# Python Calculator with GUI 
# *********************************

from tkinter import *
from turtle import bgcolor # import the tkinker library

def button_press(num):   # defining each button press
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

    


def equals():   # theis block checks for the button_press (e)

    global equation_text

    try:  # try is used in try..  except blocks. it defines a block of code test if it contains any error.
          # you can define different blocks for different error types, it blocks to exceuts if nothing went wrong.
        total = str(eval(equation_text))  # parses the expression arguement and evalutates it as a python expression 

        equation_label.set(total)  # 

        equation_text = total

    except SyntaxError: # check for syntax error    

        equation_text.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:   

        equation_label.set ("arithmetic error")

        equation_text = ""

def clear() :   # clears the equation_label for the next calculation
    global equation_text

    equation_label.set("")
    
    equation_text = ""






    




window = Tk()
window.title("Python Calculator")
window.geometry("600x500")
window.configure(bg="pink")

equation_text = ""

equation_label = StringVar()

label =  Label(window, textvariable=equation_label, font=("console", 20), bg = "lightgreen", width=22, height = 2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height = 4, width = 9, font = 35, bg = "lightblue", command = lambda: button_press(1))
button1.grid(row=0, column=0)


button2 = Button(frame, text=2, height = 4, width = 9, font = 35, bg = "lightblue", command = lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height = 4, width = 9, font = 35, bg = "lightblue", command = lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height = 4, width = 9, font = 35, bg = "lightblue", command = lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height = 4, width = 9, font = 35, bg = "lightblue", command = lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height = 4, width = 9, font = 35, bg = "lightblue", command = lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height = 4, width = 9, font = 35, bg = "lightblue", command = lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height = 4, width = 9, font = 35, bg = "lightblue", command = lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height = 4, width = 9, font = 35, bg = "lightblue", command = lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height = 4, width = 9, font = 35, bg = "lightblue",  command = lambda: button_press(0))
button0.grid(row=3, column=0) 


# Create the operation button 

plus = Button(frame, text="+", height = 4, width = 9, font = 35, bg = "lightcoral", command=lambda: button_press("+"))
plus.grid(row=0, column=3)


minus = Button(frame, text="-", height = 4, width = 9, font = 35, bg = "lightcoral", command=lambda: button_press("-"))
minus.grid(row=1, column=3)

multiply = Button(frame, text="×", height = 4, width = 9, font = 35, bg = "lightcoral", command=lambda: button_press("x"))
multiply.grid(row=2, column=3)

divide = Button(frame, text="÷", height = 4, width = 9, font = 60, bg = "lightcoral", command=lambda: button_press("/"))
divide.grid(row=3, column=3)

# create equals 

equal = Button(frame, text="=", height = 4, width = 9, font = 35, bg = "lightcoral", command=equals)
equal.grid(row=3, column=2)

# create decimal

decimal = Button(frame, text="point", height = 4, width = 9, font = 35, bg = "lightcoral",  command=lambda: button_press("."))
decimal.grid(row=3, column=1)


# create clear button

clear = Button(window, text="clear", height = 4, width = 38, font = 35, bg = "cyan", command=clear)
clear.pack() 



window.mainloop()



