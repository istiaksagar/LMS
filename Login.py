from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *


root = Tk()
root.title("IIUC Central Library")
root.iconbitmap('logo.ico')
#img = PhotoImage('logo.png')
#root.iconphoto(True, img)
root.resizable(0, 0)
bg = Image.open('BG.jpg')
bg.thumbnail((600,500))
width, height = bg.size
bg = ImageTk.PhotoImage(bg)


def new():
    if user_entry.get() == "":
        messagebox.showinfo("Login System", "Please enter the Username")
    elif password_entry.get() == "":
        messagebox.showinfo("Login System", "Please enter the Password")
    elif user_entry.get() == "" and password_entry.get() == "":
        messagebox.showinfo("Login System", "Please enter the Username and Password")
    elif user_entry.get() == "Emrus" and password_entry.get() == "1234":
        root.destroy()
        import main
        # messagebox.showinfo("Login System", "Successfully Loged in")
    else:
        messagebox.showinfo("Login System", "Please enter the correct Username and Password")


canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')
label = Label(root, text="Login Page", font=("Georgia 25 bold"), bg='#800000', fg='white', relief=SUNKEN)
canvas.create_window(180, 40, anchor="nw", window=label)
user_label = Label(root, text="User name:", font=("Georgia 18 bold"), bg='#cb4154', fg='white')
canvas.create_window(75, 150, anchor="nw", window=user_label)
password_label = Label(root, text="Password:", font=("Georgia 18 bold"), bg='#cb4154', fg='white')
canvas.create_window(85, 210, anchor="nw", window=password_label)
user_entry = Entry(root, font=("Lora 14"))
user_entry.focus()
canvas.create_window(230, 150, anchor="nw", window=user_entry)
paswd = StringVar()
password_entry = Entry(root, textvar=paswd, font=("Lora 14"), show="*")
canvas.create_window(230, 210, anchor="nw", window=password_entry)
login = Button(root, text="Log In", font=("Impact 22 bold"), width=8, bg="#cb4154", fg='White', relief=RAISED, command=new)
canvas.create_window(210, 290, anchor="nw", window=login)

root.mainloop()