from tkinter import *
from PIL import ImageTk
import webbrowser

def login_page():
    home_window.destroy()
    import signin


home_window=Tk()
home_window.geometry('1920x1080')
home_window.resizable(0,0)
home_window.title('Home Page')
bgImage=ImageTk.PhotoImage(file='image/home11.png')

bgLabel=Label(home_window,image=bgImage)        
bgLabel.pack()


def about_connet():
    home_window.destroy()
    import about


button=Button(
   home_window,                                        
    text='ABOUT US ',
    font=('Times', 12),
    command=about_connet,
    bg='blue',
    width=10,
    fg='white',
    activebackground='green',
    activeforeground='white'
    )
button.place(x=home_window.winfo_screenwidth() - 100, y=0)



homeButton=Button(
    home_window,                                        
    text='Sign In',
    font=('Times', 35),
    command=login_page,
    padx=10,
    pady=10,
    bg='blue',
    width=20,
    fg='white',
    activebackground='green',
    activeforeground='white'
    ).place(x=630, y=600)

home_window.mainloop()

