from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def clear():
    adharnoEntry.delete(0,END)
    passwordEntry.delete(0,END)
    

def connect_database():
    adharno = adharnoEntry.get()
    password = passwordEntry.get()

    if adharno == '' or password == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif len(adharno) != 9 or not adharno.isdigit():
        messagebox.showerror('Error', 'Adhar Number should be 9 digits only')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Root@123')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,adharno int(9),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
            query = 'select * from data where adharno=%s'
            mycursor.execute(query, (adharno,))

            row = mycursor.fetchone()
            if row != None:
                messagebox.showerror('Error', 'Adhar Number Already Exists')
            else:
                query = 'insert into data(Adharno,password) values(%s,%s)'
                mycursor.execute(query, (adharno, password))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Registration is successfull')
                clear()
                signup_window.destroy()
                import login


def register_page():
    signup_window.destroy()
    import login


signup_window=Tk()
signup_window.geometry('1920x1080')
signup_window.resizable(0,0)
signup_window.title('Signin Page')
bgImage=ImageTk.PhotoImage(file='image/signin.png')

bgLabel=Label(signup_window,image=bgImage)
bgLabel.pack()

heading=Label(signup_window,text='Adhar Number',font=('Microsoft Yahei UI Light',28,'bold'),bg='#F5F5F5')
heading.place(x=900,y=300)

adharnoEntry=Entry(signup_window,width=22,font=("'Microsoft Yahei UI Light",25))
adharnoEntry.place(x=900,y=350)

heading=Label(signup_window,text='Password',font=('Microsoft Yahei UI Light',25,'bold'),bg='#F5F5F5')
heading.place(x=900,y=450)

passwordEntry=Entry(signup_window,width=22,show='*',font=("'Microsoft Yahei UI Light",25))
passwordEntry.place(x=900,y=500)

singupButton=Button(
    signup_window,
    text='Register',
    font=('Times', 25),
    command=connect_database,
    bg='blue',
    width=10,
    fg='white',
    activebackground='green',
    activeforeground='white'
    ).place(x=1001, y=640)

signupLabel=Label(signup_window,text='Have Account ',font=('Open Sans',9,'bold'),bg='#F5F5F5')
signupLabel.place(x=950,y=740)

newaccountButton=Button(
    signup_window,
    text='Login',
    font=('Open Sans',9,'bold underline'),
    command=register_page,
    fg='blue',
    bg='#F5F5F5',
    activebackground='white',
    cursor='hand2',
    bd=0
    ).place(x=1090, y=740)

signup_window.mainloop()