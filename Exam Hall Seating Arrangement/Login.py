import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry, Checkbutton, BooleanVar
from PIL import Image, ImageTk
import ast

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

def toggle_password_visibility():
    global show_password
    show_password = not show_password
    if show_password:
        code.config(show="")
    else:
        code.config(show="*")

def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        screen = Toplevel()
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen, text='Hello Everyone', bg="#fff", font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

        screen.mainloop()
    elif username != 'admin' and password != '1234':
        show_custom_error("Incorrect", "Incorrect Username and Password")
        
    elif password != '1234':
        show_custom_error("Incorrect", "Incorrect Password")

    elif username != 'admin':
        show_custom_error("Incorrect", "Incorrect Password")

root = tk.Tk()
root.title('EXAM HALL SEATING ARRANGEMENT')
root.iconbitmap(r'C:\Users\sures\OneDrive\Desktop\Exam Seat\Assests\img\logoico.ico')
root.geometry('925x500+300+200')
root.configure(bg='#e84118')  # Set background color to #e84118
root.resizable(False, False)

# Load and display the background image
try:
    pil_image = Image.open(r'C:\Users\sures\OneDrive\Desktop\Exam Seat\Assests\img\bg1.jpg')
    img = ImageTk.PhotoImage(pil_image)
    label = Label(root, image=img)
    label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"An error occurred: {e}")

# Create a custom title bar
title_bar = tk.Frame(root, bg='#1abc9c', height=30)
title_bar.pack(fill='x')

# Create a label for the title
title_label = tk.Label(title_bar, text='Login Page', bg='#1abc9c', fg='white', font=('Helvetica', 12,'bold'))
title_label.pack(side='left', padx=10)

# Create the frame
frame = tk.Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

# Add heading label to the frame
heading = tk.Label(frame, text='Sign In', fg='#1abc9c', bg='white', font=('Microsoft Vahei UI L', 23, 'bold'))
heading.place(x=120, y=5)

###==================================================
# Create an Username Entry widget

def on_enter_user(e):
    user.delete(0,'end')

def on_leave_user(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user = tk.Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Vahei UI Light', 11))
user.place(x=30, y=80)  # Adjust the position as needed
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter_user)
user.bind('<FocusOut>',on_leave_user)

tk.Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

###==================================================
# Create a Password Entry widget
def on_enter_code(e):
    code.delete(0,'end')

def on_leave_code(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

show_password = False
code = tk.Entry(frame, width=20, fg='black', border=0, bg='white', font=('Microsoft Vahei UI Light', 11), show="*")
code.place(x=30, y=150)  # Adjust the position as needed
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter_code)
code.bind('<FocusOut>',on_leave_code)

tk.Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##=============================================================
##=============================================================
tk.Button(frame, width=39, pady=7, text='Sign in', bg='#1abc9c', fg='white', border=0, command=signin).place(x=35, y=240)
label = tk.Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Vahei UI Light', 9))
label.place(x=75, y=290)

sign_up = tk.Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#1abc9c')
sign_up.place(x=210, y=290)


# Checkbox for hiding and showing password
show_password_var = BooleanVar()
show_password_check = Checkbutton(frame, text="Show Password", variable=show_password_var, command=toggle_password_visibility, bg='white', fg='#1abc9c')
show_password_check.place(x=30, y=200)

root.mainloop()
