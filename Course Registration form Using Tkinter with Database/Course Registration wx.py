import wx
import wx.adv
import datetime
import sqlite3

app = wx.App()
frame = wx.Frame(parent=None, title='Registration Form',size=(750,750))
panel = wx.Panel(frame)
panel.SetBackgroundColour("#b8f9ff")

Title = wx.StaticText(panel, label = "Registration Form WX", pos = (250,20),style=wx.ALIGN_CENTER)
font1 = wx.Font(15,wx.DECORATIVE,wx.ITALIC,wx.BOLD,underline=False,faceName="",encoding=wx.FONTENCODING_DEFAULT)
Title.SetFont(font1)

font2 = wx.Font(13,wx.MODERN,wx.SLANT,wx.NORMAL,underline=False,faceName="",encoding=wx.FONTENCODING_DEFAULT)

l1 = wx.StaticText(panel, -1, "Full Name",pos=(160,80))
l1.SetFont(font2)
e1 = wx.TextCtrl(panel, -1, "", size=(250, -1),pos=(300,80))

l2 = wx.StaticText(panel, -1, "Dob",pos=(160,120))
l2.SetFont(font2)
e2 = wx.adv.CalendarCtrl(panel,wx.ID_ANY,wx.DefaultDateTime,size=(250,-1),pos=(300,120))

GenderList = ['Male', 'Female']
box= wx.RadioBox(panel, label = 'Gender', pos = (160,270), choices = GenderList,majorDimension = 3, style = wx.RA_SPECIFY_ROWS,size=(200,-1))
box.SetFont(font2)

l3 = wx.StaticText(panel, -1, "Mobile",pos=(160,380))
l3.SetFont(font2)
e3 = wx.TextCtrl(panel, -1, "", size=(250, -1),pos=(300,380))

l4 = wx.StaticText(panel, -1, "Email",pos=(160,420))
l4.SetFont(font2)
e4 = wx.TextCtrl(panel, -1, "", size=(250, -1),pos=(300,420))

l5 = wx.StaticText(panel, -1, "Address",pos=(160,470))
l5.SetFont(font2)
e5 = wx.TextCtrl(panel, -1, "", size=(250, -1),pos=(300,470),style = wx.TE_MULTILINE)

CourseList = [
    "CSE",
    "IT",
    "ECE",
    "EEE",
    "EIE",
    "BME",
    "Mech"
]
l6 = wx.StaticText(panel, -1, "Course",pos=(160,530))
l6.SetFont(font2)
course = wx.ComboBox(panel,choices= CourseList,size=(250,-1),pos=(300,530))


l7 = wx.StaticText(panel, -1, "Reason",pos=(160,590))
l7.SetFont(font2)
e7 = wx.TextCtrl(panel, -1, "", size=(250, -1),pos=(300,590))

def database(self):
   name=e1.GetValue()
   date = e2.PyGetDate()
   gender= box.GetStringSelection()
   call = e3.GetValue()
   mail = e4.GetValue()
   Address = e5.GetValue()
   dpt = course.GetValue()
   reason = e7.GetValue()
   wx.MessageBox("Your Form is Submitted Successfully","Submit",wx.OK)
   conn = sqlite3.connect('FormWX.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Gender TEXT,DOB DATETIME,Mobile NUMBER,Email TEXT,Address TEXT,course TEXT,Reason TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Gender,dob,Mobile,Email,Address,course,Reason) VALUES(?,?,?,?,?,?,?,?)',(name,gender,date,call,mail,Address,dpt,reason))
   conn.commit()


submit = wx.Button(panel,label="Submit",size=(150,-1),pos=(310,650))
submit.Bind(wx.EVT_BUTTON,database)

frame.Show()
app.MainLoop()

