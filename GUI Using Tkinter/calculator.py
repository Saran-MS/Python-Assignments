import tkinter as tk
from functools import partial

#functions

def add(label_result, n1, n2):  
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(text="Result  %s + %s = %d" %(num1,num2,result),fg="blue",font=1)

def sub(label_result, n1, n2):  
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)-int(num2)
    label_result.config(text="Result  %s - %s = %d" %(num1,num2,result),fg="blue",font=1)


def mul(label_result, n1, n2):  
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)*int(num2)
    label_result.config(text="Result  %s * %s = %d" %(num1,num2,result),fg="blue",font=1)

def div(label_result, n1, n2):  
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)/int(num2)
    label_result.config(text="Result  %s / %s = %d" %(num1,num2,result),fg="blue",font=1)

#tkinter widgets root 
root = tk.Tk()
root.title("Calculator")

#tkinter variables
number1 = tk.StringVar()
number2 = tk.StringVar()

#val1 val2 text entry intialization
tk.Label(root,text="First Number",fg="blue",padx=5).grid(row=0)
tk.Label(root,text="Second Number",fg="blue",padx=5).grid(row=1)
e1 = tk.Entry(root,textvariable=number1).grid(row=0,column=1,padx=10,pady=10)
e2 = tk.Entry(root,textvariable=number2).grid(row=1,column=1,padx=10,pady=10)

#result label
labelResult = tk.Label(root)
labelResult.grid(row=4,column=0,padx=20,pady=10) 

#partial functions
add = partial(add, labelResult, number1, number2)
sub = partial(sub, labelResult, number1, number2)
mul = partial(mul, labelResult, number1, number2)
div = partial(div, labelResult, number1, number2)

#buttons to call corresponding functions
b1 = tk.Button(root,text="+",command=add,fg="red",width=2,font=5).grid(row=2,column=0,padx=10,pady=10)
b2 = tk.Button(root,text="-",command=sub,fg="blue",width=2,font=5).grid(row=2,column=1,padx=10,pady=10)
b3 = tk.Button(root,text="*",command=mul,fg="green",width=2,font=5,).grid(row=3,column=0,padx=10,pady=10)
b4= tk.Button(root,text="/",command=div,fg="violet",width=2,font=5).grid(row=3,column=1,padx=10,pady=10)


root.mainloop()
