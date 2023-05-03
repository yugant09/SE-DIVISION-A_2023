from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def clear():
     NameEntry.delete(0,END)
     DobEntry.delete(0,END)
     gender.set('')
     AgeEntry.delete(0,END)
     AdharEntry.delete(0,END)
     clicked.set('')

#Database

def register_user():
        if NameEntry.get()=='' or DobEntry.get()=='' or gender.get()=='' or AgeEntry.get()=='' or AdharEntry.get()=='' or clicked.get()=='':
            messagebox.showerror('Error','All Fields Are Required')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='Root@123')
                mycursor=con.cursor()
            except:
                 messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')                
                 return     
            try:
               query='create database rdata'   
               mycursor.execute(query)
               query='use rdata'
               mycursor.execute(query)
               query = "CREATE TABLE data (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(50), Dob VARCHAR(10), gender VARCHAR(10), age INT DEFAULT 18 , adharno INT NOT NULL, Vaccine VARCHAR(50) NOT NULL);"
               mycursor.execute(query)
            except:
                 mycursor.execute('use rdata')
                 adhar_no = AdharEntry.get()
            if not adhar_no.isdigit() or len(adhar_no) != 9:
                messagebox.showerror('Error', 'Adhar ID must be a 9-digit number')
                return
            query='insert into data(name,Dob,gender,age,adharno,Vaccine) values(%s,%s,%s,%s,%s,%s)'     
            mycursor.execute(query,(NameEntry.get(),DobEntry.get(),gender.get(),AgeEntry.get(),AdharEntry.get(),clicked.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is Successfull')
            clear()
            register_window.destroy()
            import slotbooking
                 


#Image
register_window=Tk()
register_window.geometry('1920x1080')
register_window.resizable(0,0)
register_window.title('Home Page')
bgImage=ImageTk.PhotoImage(file='image/reigster.png')

bgLabel=Label(register_window,image=bgImage)
bgLabel.pack()

# Registration Heading

heading=Label(register_window,text='Register Page',font=('Microsoft Yahei UI Light',23,'bold'),bg='#D9D9D9')
heading.place(x=800,y=100)

#Name

heading=Label(register_window,text='Name',font=('Microsoft Yahei UI Light',23,'bold'),bg='#D9D9D9')
heading.place(x=800,y=193)

NameEntry=Entry(register_window,width=50,font=("'Microsoft Yahei UI Light",25))
NameEntry.place(x=800,y=250)

#Date of Birth

heading=Label(register_window,text='Enter your birthdate (MM/DD/YYYY):',font=('Microsoft Yahei UI Light',23,'bold'),bg='#D9D9D9')
heading.place(x=800,y=327)

DobEntry=Entry(register_window,width=50,font=("'Microsoft Yahei UI Light",25))
DobEntry.place(x=800,y=384)

#Gender

heading=Label(register_window,text='Gender',font=('Microsoft Yahei UI Light',23,'bold'),bg='#D9D9D9')
heading.place(x=800,y=465)

gender = StringVar()

# create the radio buttons and bind them to the variable
Radiobutton(register_window, width=8,height=2,font=("time",15), text="Male", variable=gender, value="Male").place(x=930,y=461)
Radiobutton(register_window, width=8,height=2,font=("time",15), text="Female", variable=gender, value="Female").place(x=1050,y=461)

#Age

heading=Label(register_window,text='Age',font=('Microsoft Yahei UI Light',23,'bold'),bg='#D9D9D9')
heading.place(x=800,y=530)

AgeEntry=Entry(register_window,width=50,font=("'Microsoft Yahei UI Light",25))
AgeEntry.place(x=800,y=590)

#Adhar ID

heading=Label(register_window,text='Adhar Id',font=('Microsoft Yahei UI Light',23,'bold'),bg='#D9D9D9')
heading.place(x=800,y=660)

AdharEntry=Entry(register_window,width=50,font=("'Microsoft Yahei UI Light",25))
AdharEntry.place(x=800,y=710)

#Vaccine Type

def show():
    mylabel = Label(register_window, text=clicked.get()).pack()

options=[
    'COWIN',
    'COVISHIELD',
    'INFRANIX',
    'ADACEL',
    'Hepatitis-A',
    'Hepatitis-B',
    'Polio'
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(register_window, clicked, *options,)
drop.place(x=1050,y=799)   

heading=Label(register_window,text='Select Vaccine',font=('Microsoft Yahei UI Light',23,'bold'),bg='#D9D9D9')
heading.place(x=800,y=790)

#area and time



#button
RegisterButton=Button(
    register_window,
    text='Select Slot',
    font=('Times', 25),
    command=register_user,
    bg='blue',
    width=10,
    fg='white',
    activebackground='green',
    activeforeground='white'
    ).place(x=1120, y=870)



register_window.mainloop()
