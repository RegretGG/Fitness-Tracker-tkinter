from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox
import re
import random
import mysql.connector as my
import smtplib
try:
  mydb= my.connect(host='localhost',user='root',database='FITNESS',password="gautham2004")
  C=mydb.cursor()
except:
  mydb =my.connect(host='localhost',user='root',password="gautham2004")
  C=mydb.cursor()
  C.execute("create database FITNESS")
  C.execute("create table FITNESS.account(acc_name varchar(25),BMI float(3),password varchar(25),email varchar(25))")
  mydb.commit()




def register():
    def BMIREG():
        bmi=Tk()
        bmi.title("BMI Calculator")
        bmi.geometry("500x400")

        def Calculate():
            global BMI
            weigh=int(weightentry.get())
            heigh=int(heightentry.get())
            gende=str(genderentry.get())
            ag=int(ageentry.get())
            BMI=(weigh/((heigh*heigh)/10000))
            BMI= round(BMI, 1)
            Label(bmi,text=f"{BMI}",font="arial 30 bold").place(x=200,y=290)

        weight=Label(bmi, text="Weight(in kgs)", font="arial 15")
        height=Label(bmi, text="Height(in m)", font="arial 15")
        gender=Label(bmi, text="Gender(M or F)" ,font="arial 15")
        age=Label(bmi, text="Age", font="arial 15")

        weight.place(x=50,y=20)
        height.place(x=50,y=90)
        gender.place(x=50,y=160)
        age.place(x=50, y=230)

        BMI=Label(bmi,text="BMI:",font="arial 15")
        BMI.place(x=50,y=300)

        weightvalue=StringVar()
        heightvalue=StringVar()
        gendervalue=StringVar()
        agevalue=StringVar()

        weightentry=Entry(bmi, textvariable=weightvalue, font="arial 20", width=8)
        heightentry=Entry(bmi, textvariable=heightvalue, font="arial 20", width=8)
        genderentry=Entry(bmi, textvariable=gendervalue, font="arial 20" , width=8)
        ageentry=Entry(bmi, textvariable=agevalue, font="arial 20" , width=8)

        weightentry.place(x=200,y=20)
        heightentry.place(x=200,y=90)
        genderentry.place(x=200,y=160)
        ageentry.place(x=200, y=230)

        Button(bmi, text="Calculate",font="arial 15",command=Calculate).place(x=350,y=20)
        Button(bmi,text="Exit",command= lambda:bmi.destroy(),font="arial 15",width=8).place(x=350,y=90)
        bmi.mainloop()
    def mail(add,sub,msg):
        sender_address = 'fitnesstrackercasestudy@gmail.com'
        sender_pass = 'Password@2021'
        receiver_address = add
        message = MIMEMultipart()
        message['Subject'] = sub
        message.attach(MIMEText(msg, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    def create():
        def pass_strength(p):
            global passwordstrength
            passwordstrength = 0
            while True:  
                if (len(p)<6):
                    break
                elif not re.search("[a-z]",p):
                    break
                elif not re.search("[A-Z]",p):
                    break
                elif not re.search("[0-9]",p):
                    break
                elif not re.search("[@!#$%^&*-+]",p):
                    break
                elif re.search("\s",p):
                    break
                else:
                    passwordstrength = 100
                    break
            if passwordstrength == 100:
                pass
            else:
                messagebox.showwarning("Password isnt strong enough!", "Please Re-enter your password.")
        def confirm():
            while True:
                if code.get()== i:
                    V.destroy()
                    rs.destroy()
                    return
                else:
                    messagebox.showwarning("Incorrect Verification Code"," Please enter the correct verification code.")
                    continue
        while True:
            p = password.get()
            while True:
                pass_strength(p)
                break
            if passwordstrength == 100:
                break
            else:
                return


        msg = "Welcome to Fitness Life!\nHere is your verification code:\n"+i+"\nWe welcome you to the start of your new fitness journey.\n\n\n\nPlease ignore this message if it doesn't concern you"
        mail(email.get(),"Account Registration- Verification Code",msg)
        messagebox.showinfo("Verification Code", "A verification code has been sent to your inbox.")    
        V = Tk()
        V.title("Make Your Account")
        V.geometry("1366x768")
        Label(V, text="Enter verification code: ", bg="cyan").pack() 
        Label(V, text="").pack()
        code = Entry(V)
        code.pack()
        Label(V, text="").pack()
        Button(V, text="OK", width=10, height=1, bg="red", command = confirm).pack()
        Label(V, text="").pack()
        V.mainloop()
    
    i = str(random.randint(10000,99999))
    rs = Tk()
    rs.title("Make Your Account")
    rs.geometry("1366x768")
    
    Label(rs, text="Make Your Account", bg="yellow",width=1366, height=10).pack()
    Label(rs, text="").pack()
    Label(rs, text="").pack()
    Label(rs, text="Enter account name: ", bg="cyan").pack()
    Label(rs, text="").pack()
    username = Entry(rs)
    
    username.pack()
    u = username.get()
    Label(rs, text="").pack()
    Button(rs, text="Evaluate BMI: ", bg="cyan", command= BMIREG).pack()
    Label(rs, text="").pack()
    Label(rs, text="").pack()
    Label(rs, text="Enter password: ", bg="cyan").pack()
    Label(rs, text="").pack()
    password = Entry(rs)
    password.pack()
    Label(rs, text="").pack()
    Label(rs, text="Enter email ID:", bg="cyan").pack()
    Label(rs, text="").pack()
    email = Entry(rs)
    email.pack()
    Label(rs, text="").pack()
    Label(rs, text="").pack()
    
    Label(rs, text="").pack()
    Button(rs, text="Register!", width=10, height=1, bg="red", command = create).pack()
    Label(rs, text="").pack()
    rs.mainloop()
register()
