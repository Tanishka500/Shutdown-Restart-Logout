from tkinter import *
import os

def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")

def logout():
    return os.system("shutdown -l")

master = Tk()
master.title("System Shortcuts")
master.configure(bg='dark grey')
master.geometry('300x200')

heading_label = Label(master, text="System Shortcuts", bg='dark grey', fg='black', font=('Arial', 14, 'bold'))
heading_label.pack(pady=10)

button_frame = Frame(master, bg='dark grey')
button_frame.pack(expand=True)

Button(button_frame, text="Shutdown", command=shutdown, width=15).pack(pady=10)
Button(button_frame, text="Restart", command=restart, width=15).pack(pady=10)
Button(button_frame, text="Log out", command=logout, width=15).pack(pady=10)

master.mainloop()
