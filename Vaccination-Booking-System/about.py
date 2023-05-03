from tkinter import *
from PIL import ImageTk
import webbrowser

about_window=Tk()
about_window.geometry('1920x1080')
about_window.resizable(0,0)
about_window.title('About us')
bgImage=ImageTk.PhotoImage(file='image/about us.png')

bgLabel=Label(about_window,image=bgImage)        
bgLabel.pack()

def reg_window():
    about_window.destroy()
    import home

button=Button(
   about_window,                                        
    text='Home',
    font=('Times', 12),
    command=reg_window,
    bg='blue',
    width=10,
    fg='white',
    activebackground='green',
    activeforeground='white'
    )
button.place(x=about_window.winfo_screenwidth() - 100, y=0)

about_window.mainloop()
