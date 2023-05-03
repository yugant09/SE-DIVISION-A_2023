from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def clear():
    AreaEntry.set('')
    TimeEntry.set('')


def slot_data():
    if AreaEntry.get() == '' or TimeEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Root@123')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
        try:
            query = 'CREATE DATABASE IF NOT EXISTS sdata'
            mycursor.execute(query)
            query='use sdata'
            mycursor.execute(query)
            query = "CREATE TABLE data (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, Area VARCHAR(50) NOT NULL, Time VARCHAR(50) NOT NULL);"
            mycursor.execute(query)

        except:
            mycursor.execute('use sdata')
            query = 'insert into data (Area, Time) values (%s, %s)'     
            mycursor.execute(query, (AreaEntry.get(), TimeEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is Successful')
            clear()
            slot_window.destroy()



# create the drop-down boxes for the area and time slot selection
slot_window = Tk()
slot_window.geometry('1920x1080')
slot_window.resizable(0, 0)
slot_window.title('Slot Booking')

bgImage = ImageTk.PhotoImage(file='image/slot booking.png')
bgLabel = Label(slot_window, image=bgImage)
bgLabel.pack()

heading = Label(slot_window, text='Select Your Slot', font=('times', 25, 'bold'), bg='#F5F5F5')
heading.place(x=835, y=300)

heading=Label(slot_window,text='Select Area :',font=('Microsoft Yahei UI Light',18,'bold'),bg='#F5F5F5')
heading.place(x=700,y=440)

heading=Label(slot_window,text='Select time :',font=('Microsoft Yahei UI Light',18,'bold'),bg='#F5F5F5')
heading.place(x=700,y=540)

def show():
    mylabel = Label(slot_window, text=AreaEntry.get()).pack()

options=[
    "Savarkar Nagar",
    "Lokmany Nagar", 
    "Vartak Nagar", 
    "Samta Nagar", 
    "Ramchandra Nagar", 
    "Shastri Nagar",
    "Indira Nagar",
    "Sathe Nagar",
]

AreaEntry = StringVar()
AreaEntry.set(options[0])

drop = OptionMenu(slot_window, AreaEntry, *options)
drop.place(x=1000,y=440) 

def show():
    mylabel = Label(slot_window, text=TimeEntry.get()).pack()

options2=[
    "9:00 am - 10:00 am",
    "10:00 am - 11:00 am", 
    "11:00 am - 12:00 am", 
    "12:00 am - 1:00 pm", 
    "1:00 pm - 2:00 pm", 
    "2:00 pm - 3:00 pm",
    "3:00 pm - 4:00 pm",
    "4:00 pm - 5:00 pm",                              
]

TimeEntry= StringVar()
TimeEntry.set(options2[0])

drop = OptionMenu(slot_window, TimeEntry, *options2)
drop.place(x=1000,y=540) 

RegisterButton=Button(
    slot_window,
    text='Select Slot',
    font=('Times', 25),
    command=slot_data,
    bg='blue',
   

    width=10,
    fg='white',
    activebackground='green',
    activeforeground='white'
    ).place(x=855, y=640)

slot_window.mainloop()
