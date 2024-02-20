from tkinter import *
from tkinter import messagebox
import ast
import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry
from PIL import Image, ImageTk


window=Tk()
window.title("EXAM HALL SEATING ARRANGEMENT")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)
window.iconbitmap(r'C:\Users\sures\OneDrive\Desktop\Exam Seat\Assests\img\logoico.ico')

def show_custom_error(title, message):
    error_dialog = Toplevel()
    error_dialog.title(title)
    error_dialog.iconbitmap(r"C:\Users\sures\OneDrive\Desktop\Exam Seat\Assests\img\logoico.ico")
    error_dialog.geometry('400x150+500+300')
    error_dialog.configure(bg='#c0392b')  # Set background color to light red
    error_dialog.resizable(False, False)
    
    Label(error_dialog, text=message, fg='#f5f6fa', bg='#c0392b', font=('Arial', 14, 'bold')).pack(pady=5)
    
    def close_dialog():
        error_dialog.destroy()
        # Resume background tasks here

    Button(error_dialog, text='OK', command=close_dialog, bg='#0652DD', fg='white', font=('Arial', 14, 'bold')).pack(pady=30)
    
    # Make the error dialog modal
    error_dialog.grab_set()
    # Wait until the error dialog is closed before continuing with the background tasks
    error_dialog.wait_window()
    
def show_custom_info(title, message):
    info_dialog = Toplevel()
    info_dialog.title(title)
    info_dialog.iconbitmap(r"C:\Users\sures\OneDrive\Desktop\Exam Seat\Assests\img\logoico.ico")
    info_dialog.geometry('400x150+500+300')
    info_dialog.configure(bg='#1abc9c')  # Set background color to light green
    info_dialog.resizable(False, False)
    
    Label(info_dialog, text=message, fg='#f5f6fa', bg='#1abc9c', font=('Arial', 14, 'bold')).pack(pady=5)
    
    def close_dialog():
        info_dialog.destroy()
        # Resume background tasks here

    Button(info_dialog, text='OK', command=close_dialog, bg='#0652DD', fg='white', font=('Arial', 14, 'bold')).pack(pady=30)
    
    # Make the info dialog modal
    info_dialog.grab_set()
    # Wait until the info dialog is closed before continuing with the background tasks
    info_dialog.wait_window()

def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            file = open('datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('datasheet.txt', 'w')
            w = file.write(str(r))

            show_custom_info('SignUp', 'Successfully Signed Up')
        except:
            file = open('datasheet.txt', 'w')
            pp = str({'Username': 'Password'})
            file.write(pp)
            file.close()
    else:
        show_custom_error('Incorrect', 'Password should not match')



def sign():
    window.destroy()

# Load and display the background image
try:
    pil_image = Image.open(r'C:\Users\sures\OneDrive\Desktop\Exam Seat\Assests\img\bg1.jpg')
    img = ImageTk.PhotoImage(pil_image)
    label = Label(window, image=img)
    label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"An error occurred: {e}")

# Create a custom title bar
title_bar = tk.Frame(window, bg='#1abc9c', height=30)
title_bar.pack(fill='x')

# Create a label for the title
title_label = tk.Label(title_bar, text='SignUp Page', bg='#1abc9c', fg='white', font=('Helvetica', 12,'bold'))
title_label.pack(side='left', padx=10)

#Create Frame
frame=Frame(window,width=350,height=390,bg='white')
frame.place(x=480,y=50)

heading = tk.Label(frame, text='Sign Up', fg='#1abc9c', bg='white', font=('Microsoft Vahei UI L', 23, 'bold'))
heading.place(x=120, y=5)

###-------------------------------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Vahei UI L', 11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

###-------------------------------------------------------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Vahei UI Light', 11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
###-------------------------------------------------------------------------------------------------------------
def on_enter(e):
    confirm_code.delete(0,'end')
def on_leave(e):
    if confirm_code.get()=='':
        confirm_code.insert(0,'Confirm Password')

confirm_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Vahei UI Light', 11))
confirm_code.place(x=30,y=220)
confirm_code.insert(0,'Confirm Password')
confirm_code.bind('<FocusIn>',on_enter)
confirm_code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
#--------------------------------------------------------------------------------

Button(frame,width=39,pady=7,text='Sign Up',bg='#1abc9c',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft Vahei UI Light', 9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#1abc9c',command=sign)
signin.place(x=190,y=340)


window.mainloop()
