from tkinter import *
from tkcalendar import *
import sqlite3
from tkinter import messagebox as mb


root = Tk()
root.geometry('650x750')
root.title("Registration Form")
root.config(background="#b5ffc6")

label_0 = Label(root, text="Registration form",bg="#b5ffc6",width=20,font=("bold", 20))
label_0.place(x=140,y=20)


Fullname = StringVar()
label_1 = Label(root, text="Full Name",width=20,bg="#b5ffc6",font=("bold", 10))
label_1.place(x=80,y=80)
entry_1 = Entry(root,textvariable=Fullname)
entry_1.place(x=250,y=80)

dob = StringVar()
label_2 = Label(root, text="D.O.B",width=20,bg="#b5ffc6",font=("bold", 10))
label_2.place(x=68,y=120)
cal = Calendar(root, width=30, selectmode="day", year=2020, month=8, day=22,background="blue",foreground="white",textvariable=dob).place(x=250, y=120)


GenderList = [
    "Male",
    "Female"
]
genderSelect = StringVar()
label_3 = Label(root, text="Gender",bg="#b5ffc6",width=20,font=("bold", 10))
label_3.place(x=68,y=325)
genderSelect.set('Select Gender')
gender = OptionMenu(root, genderSelect, *GenderList)
gender.config(width=15)
gender.place(x=250, y=320)


Mobile = IntVar()
label_4 = Label(root, text="Mobile Number",width=20,bg="#b5ffc6",font=("bold", 10))
label_4.place(x=90,y=370)
entry_4 = Entry(root,textvariable=Mobile)
entry_4.place(x=250,y=370)


Email= StringVar()
label_5 = Label(root, text="Email ID",width=20,bg="#b5ffc6",font=("bold", 10))
label_5.place(x=69,y=420)
entry_5 = Entry(root,textvariable=Email)
entry_5.place(x=250,y=420)



label_6 = Label(root, text="Address",width=20,bg="#b5ffc6",font=("bold", 10))
label_6.place(x=68,y=460)
entry_6 = Text(root,height=4,width=30)
entry_6.place(x=250,y=460)


label_7 = Label(root, text="Course Choice",width=20,bg="#b5ffc6",font=("bold", 10))
label_7.place(x=90,y=550)
CourseList = [
    "CSE",
    "IT",
    "ECE",
    "EEE",
    "EIE",
    "BME",
    "Mech"
]
CourseSelect = StringVar()
CourseSelect.set('Select Course')
Course = OptionMenu(root, CourseSelect, *CourseList)
Course.config(width=15)
Course.place(x=250, y=550)


label_8 = Label(root, text="Reason",width=20,bg="#b5ffc6",font=("bold", 10))
label_8.place(x=68,y=600)
entry_8 = Text(root,height=4,width=30)
entry_8.place(x=250,y=600)

def database():
   name=Fullname.get()
   date = dob.get()
   gender= genderSelect.get()
   call =Mobile.get()
   mail =Email.get()
   Address = entry_6.get(1.0,END)
   dpt = CourseSelect.get()
   reason = entry_8.get(1.0,END)
   mb.showinfo('Submit', 'Your Form is Successfully Submitted')
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,DOB TEXT,Gender TEXT,Mobile NUMBER,Email TEXT,Address TEXT,course TEXT,Reason TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Dob,Gender,Mobile,Email,Address,course,Reason) VALUES(?,?,?,?,?,?,?,?)',(name,date,gender,call,mail,Address,dpt,reason))
   conn.commit()


    
Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=700)


root.mainloop()