from tkinter import *

# Function to clear the screen and reset the expression
def clr_scr():
    global exp
    input_text.set("")
    exp = ""

# Function to handle button press events
def button_press(num):
    global exp
    exp = input_text.get()
    exp = str(exp) + str(num)
    input_text.set(exp)

# Function to handle operator button press events
def button_oper(opr):
    global exp
    exp = input_text.get()
    exp = str(exp) + str(opr)
    input_text.set(exp)
    global oper
    oper = opr

# Function to perform calculation and update display
def equal(event):
    global exp
    global oper
    exp = input_text.get()
    input_text.set("")
    result = float(eval(exp))
    exp = result
    input_text.set(result)

# Create the main Tkinter window
win = Tk()
win.title("My Calculator")
win.resizable(False, False)

# LabelFrame for display frame
display_frame = LabelFrame(win, relief=SUNKEN, padx=2, pady=2)
display_frame.grid(row=0, column=0, columnspan=4, padx=2, pady=4)

# StringVar for input text
input_text = StringVar()

# Entry widget for display
display = Entry(display_frame, font=('Arial', 18, 'bold'), textvariable=input_text, width=22, bg="#eee", bd=0, justify=RIGHT)
display.pack(ipady=12)

# Buttons with modified colors and designs
button_1 = Button(win, padx=30, pady=30, text="1", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press(1))
button_2 = Button(win, padx=30, pady=30, text="2", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press(2))
button_3 = Button(win, padx=30, pady=30, text="3", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press(3))
button_4 = Button(win, padx=30, pady=30, text="4", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press(4))
button_5 = Button(win, padx=30, pady=30, text="5", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press(5))
button_6 = Button(win, padx=30, pady=30, text="6", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press(6))
button_7 = Button(win, padx=30, pady=30, text="7", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press(7))
button_8 = Button(win, padx=30, pady=30, text="8", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press(8))
button_9 = Button(win, padx=30, pady=30, text="9", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press(9))
button_0 = Button(win, padx=30, pady=30, text="0", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press(0))
button_add = Button(win, padx=30, pady=30, text="+", bg="white", fg="black", font=('Arial', 12), command=lambda: button_oper("+"))
button_sub = Button(win, padx=30, pady=30, text="-", bg="white", fg="black", font=('Arial', 12), command=lambda: button_oper("-"))
button_div = Button(win, padx=30, pady=30, text="/", bg="white", fg="black", font=('Arial', 12), command=lambda: button_oper("/"))
button_mul = Button(win, padx=30, pady=30, text="*", bg="white", fg="black", font=('Arial', 12), command=lambda: button_oper("*"))
button_equal = Button(win, padx=30, pady=30, text="=", bg="white", fg="black", font=('Arial', 12), command=lambda: equal(""))
button_clear = Button(win, padx=30, pady=30, text="C", bg="white", fg="black", font=('Arial', 12), command=clr_scr)
button_dec = Button(win, padx=30, pady=30, text=".", bg="white", fg="black", font=('Arial', 12), command=lambda: button_press("."))

# Grid layout for buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_div.grid(row=3, column=3)

button_equal.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_dec.grid(row=4, column=2)
button_mul.grid(row=4, column=3)

# Event binding for Enter key to call the equal function
win.bind("<Return>", equal)

win.mainloop()
