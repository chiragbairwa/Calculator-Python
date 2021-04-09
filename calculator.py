from tkinter import *
root =Tk()
root.title("CALCULATOR")

"""inputs"""
num = Entry(root, text="Enter A Number", width=40,borderwidth=5)
num.grid(row = 1, column = 0, columnspan =3)

"""NUMERIC"""
def numb(num_pass):
	temp = num.get()
	num.delete(0, END)
	num.insert(0, str(temp) + str(num_pass))

"""ARITHMETIC OPERATOR"""
def plus():
	first_plus = num.get()
	global all_new
	all_new = int(first_plus)
	num.delete(0, END)

def minus():
    return
""" first_sub = num.get()
	global f_num
	sub = int(first_sub)
	num.delete(0,END)
"""
def multi():
	return
"""    first_number = num.get()
	global mul
	mul = int(first_number)
	num.delete(0,END)
"""

"""RESULT"""
def equal():
	second_number = num.get()
	something_new = (all_new) + int(second_number)
	num.delete(0,END)
	num.insert(0, str(something_new) )


"""ARITH_Buttons"""
plus_b  = Button(root, text="+" , width=8  , height = 3 , command=plus   ,bg="Grey" , fg="red")
minus_b = Button(root, text="-" , width=8  , height = 3 , command=minus  ,bg="Grey" , fg="red")
multi_b = Button(root, text="*" , width=8  , height = 3 , command=multi  ,bg="Grey" , fg="red")
equal_b = Button(root, text="=" , width=20 , height = 3 , command=equal  ,bg="Blue" , fg="red")

"""NUM_BUTTON"""
button1 = Button(root, text="1" , width = 8 , height = 3 , bg="lightgrey", command=lambda: numb(1) )
button2 = Button(root, text="2" , width = 8 , height = 3 , bg="lightgrey", command=lambda: numb(2) )
button3 = Button(root, text="3" , width = 8 , height = 3 , bg="lightgrey", command=lambda: numb(3) )
button4 = Button(root, text="4" , width = 8 , height = 3 , bg="lightgrey", command=lambda: numb(4) )
button5 = Button(root, text="5" , width = 8 , height = 3 , bg="lightgrey", command=lambda: numb(5) )
button6 = Button(root, text="6" , width = 8 , height = 3 , bg="lightgrey", command=lambda: numb(6) )
button7 = Button(root, text="7" , width = 8 , height = 3 , bg="lightgrey", command=lambda: numb(7) )
button8 = Button(root, text="8" , width = 8 , height = 3 , bg="lightgrey", command=lambda: numb(8) )
button9 = Button(root, text="9" , width = 8 , height = 3 , bg="lightgrey", command=lambda: numb(9) )
button0 = Button(root, text="0" , width = 8 , height = 3 , bg="lightgrey", command=lambda: numb(0) )

"""PACKING"""
button1.grid(row = 2 , column = 0 )
button2.grid(row = 2 , column = 1 )
button3.grid(row = 2 , column = 2 )
button4.grid(row = 3 , column = 0 )
button5.grid(row = 3 , column = 1 )
button6.grid(row = 3 , column = 2 )
button7.grid(row = 4 , column = 0 )
button8.grid(row = 4 , column = 1 )
button9.grid(row = 4 , column = 2 )
button0.grid(row = 5 , column = 0, columnspan=1)
equal_b.grid(row = 5 , column = 1, columnspan=2)
plus_b.grid (row = 6 , column = 0)
minus_b.grid(row = 6 , column = 1)
multi_b.grid(row = 6 , column = 2)



root.mainloop()