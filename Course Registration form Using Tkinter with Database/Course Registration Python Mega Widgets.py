from tkinter import *
import Pmw
import sqlite3

root = Pmw.initialise(fontScheme = 'pmw1')
root.geometry('750x750')
root.title("Registration Form")
root.config(background="#ffb6b3")

label_0 = Label(root, text="Registration form PMW",bg="#ffb6b3",width=20,font=("bold", 20))
label_0.place(x=230,y=20)


fname = Pmw.EntryField(
    label_text = 'Full Name',
    labelpos='w',
    entry_bg="#e4e3ff",
    validate="alphabetic",
    hull_borderwidth = 2,
    hull_relief = 'ridge'
)
fname.pack(fill='x',padx=76,pady=80)

date = Pmw.EntryField(
    entry_bg="#e4e3ff",
    labelpos = 'w',
    label_text = 'DOB (dd/mm/yy):',
    validate = {
    'validator' : 'date'},
    hull_borderwidth = 2,
    hull_relief = 'ridge',
)
date.place(x=75,y=140,width=600)

gender = Pmw.RadioSelect(
    labelpos='w',
    label_text= 'Gender',
    buttontype='radiobutton',
    selectmode='single',
    hull_borderwidth = 2,
    hull_relief = 'ridge',
)
gender.place(x=75,y=200,width=600)
for text in  ('Male','Female'):
    gender.add(text)


mobile = Pmw.EntryField(
    label_text = 'Mobile Number',
    labelpos='w',
    entry_bg="#e4e3ff",
    hull_borderwidth = 2,
    hull_relief = 'ridge',
    validate='numeric'
)
mobile.pack(fill='x',padx=75,pady=90)


email = Pmw.EntryField(
    label_text = 'Email',
    labelpos='w',
    entry_bg="#e4e3ff",
    hull_borderwidth = 2,
    hull_relief = 'ridge',
)
email.place(x=75,y=340,width=600)


address = Pmw.EntryField(
    label_text = 'Address',
    labelpos='w',
    entry_bg="#e4e3ff",
    hull_borderwidth = 2,
    hull_relief = 'ridge',
    validate='alphabetic'
)
address.place(x=75,y=400,width=600)

course = ('CSE','IT','ECE','EEE','EIE','BME','Mech')
simple = Pmw.ComboBox(
    label_text='Select Course',
    labelpos = 'nw',
    scrolledlist_items = course,
    entry_bg="#e4e3ff",
    dropdown = 1,
    listheight=100,
)
simple.place(width=600,x=75,y=460)



Reason = StringVar()
reason = Pmw.EntryField(
    label_text = 'Reason',
    labelpos='w',
    entry_bg="#e4e3ff",
    hull_borderwidth = 2,
    hull_relief = 'ridge',
    validate='alphabetic'
)
reason.place(x=75,y=630,width=600)

dialog1 = Pmw.MessageDialog(
    title = 'Submit',
    defaultbutton = 1,
    message_text = 'Submitted Successfully')
dialog1.withdraw()

def database(): 
    Name = fname.getvalue()
    dob = date.getvalue()
    Gender= gender.getvalue()
    Mobile = mobile.getvalue()
    mail = email.getvalue()
    Address = address.getvalue()
    dpt = simple.getvalue()
    Reason = reason.getvalue()
    str =''.join(dpt)
    dialog1.show()
    conn = sqlite3.connect('FormPMW.db')
    with conn:
      cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (FullName TEXT,DOB TEXT,Gender TEXT,Mobile NUMBER,Email TEXT,Address TEXT,Course TEXT,Reason TEXT)')
    cursor.execute('INSERT INTO Student (FullName,DOB,Gender,Mobile,Email,Address,Course,Reason) VALUES(?,?,?,?,?,?,?,?)',(Name,dob,Gender,Mobile,mail,Address,str,Reason))
    conn.commit()

Button(root, text='Submit',width=10,bg='brown',fg='white',command=database).place(x=300,y=680)


root.mainloop()