from tkinter import *
from PIL import Image , ImageTk
from tkinter import filedialog

root = Tk()
root.title("File Opener")
root.geometry("500x340")
root.config(bg="orange")

def img():
    global image
    root.filename = filedialog.askopenfilename(initialdir="E:\Python",title="Select File", filetypes=(("JPEG","*.jpeg"),("all files","*.*"))) 
    image = ImageTk.PhotoImage(Image.open(root.filename))
    imageLabel = Label(image=image).pack()

def txt():
    text_file = filedialog.askopenfilename(initialdir="E:\Python",filetypes=(("Txt files","*.txt"),("all files","*.*")))
    text_file = open(text_file,'r')
    s = text_file.read()
    my_text = Text(root,width=30,height=10,font=("Helvetica",10))
    my_text.insert(END, s),Pack()
    my_text.pack(pady=20)
    text_file.close()




my_btn1 = Button(root,text="Open Image",command= img,fg="green").pack(pady=10)
my_btn2 = Button(root,text="Open Text File",command= txt,fg="red").pack(pady=10)

root.mainloop()