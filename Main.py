from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import add_dll_directory
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
import random
import mysql.connector as my
import smtplib
import threading
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from base64 import b64encode
import io
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes


date = ["Day1","Day2","Day3","Day4","Day5","Day6","Day7","Day8","Day9","Day10","Day11","Day12","Day13","Day14","Day15","Day16","Day17","Day18","Day19","Day20","Day21","Day22","Day23","Day24","Day25","Day26","Day27","Day28","Day29","Day30","Day31"]
BMI = 0
try:
    mydb= my.connect(host='localhost',user='root',database='FITNESS',password="gautham2004")
    C=mydb.cursor()
except:
    mydb =my.connect(host='localhost',user='root',password="gautham2004")
    C=mydb.cursor()
    C.execute("create database FITNESS")
    mydb.commit()
    mydb= my.connect(host='localhost',user='root',database='FITNESS',password="gautham2004")
    C=mydb.cursor()
    k=C.execute
    k("create table FITNESS.account(acc_name varchar(25),BMI float(3),password varchar(25),email varchar(25),BodyFat int(5))")
    k("create table FITNESS.steps(acc_name varchar(25),Day1 int(10),Day2 int(10),Day3 int(10),Day4 int(10),Day5 int(10),Day6 int(10),Day7 int(10),Day8 int(10),Day9 int(10),Day10 int(10),Day11 int(10),Day12 int(10),Day13 int(10),Day14 int(10),Day15 int(10),Day16 int(10),Day17 int(10),Day18 int(10),Day19 int(10),Day20 int(10),Day21 int(10),Day22 int(10),Day23 int(10),Day24 int(10),Day25 int(10),Day26 int(10),Day27 int(10),Day28 int(10),Day29 int(10),Day30 int(10),Day31 int(10))")
    k("create table FITNESS.calories(acc_name varchar(25),Day1 int(10),Day2 int(10),Day3 int(10),Day4 int(10),Day5 int(10),Day6 int(10),Day7 int(10),Day8 int(10),Day9 int(10),Day10 int(10),Day11 int(10),Day12 int(10),Day13 int(10),Day14 int(10),Day15 int(10),Day16 int(10),Day17 int(10),Day18 int(10),Day19 int(10),Day20 int(10),Day21 int(10),Day22 int(10),Day23 int(10),Day24 int(10),Day25 int(10),Day26 int(10),Day27 int(10),Day28 int(10),Day29 int(10),Day30 int(10),Day31 int(10))")
    k("create table FITNESS.cell_day(day int)")
    k("create table FITNESS.steps_calories(acc_name varchar(25),Day1 int(10),Day2 int(10),Day3 int(10),Day4 int(10),Day5 int(10),Day6 int(10),Day7 int(10),Day8 int(10),Day9 int(10),Day10 int(10),Day11 int(10),Day12 int(10),Day13 int(10),Day14 int(10),Day15 int(10),Day16 int(10),Day17 int(10),Day18 int(10),Day19 int(10),Day20 int(10),Day21 int(10),Day22 int(10),Day23 int(10),Day24 int(10),Day25 int(10),Day26 int(10),Day27 int(10),Day28 int(10),Day29 int(10),Day30 int(10),Day31 int(10))")
    k("insert into FITNESS.cell_day values(1)")
    mydb.commit()
    with open("Food.txt") as f:
        commands = f.readlines()
    for command in commands:
        C.execute(command)
        mydb.commit()
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
calsum = 0
def NutrientCalculator():
    def on_keyrelease(event):
    # get text from entry
        value = event.widget.get()
        value = value.strip().lower()
        
        # get data from test_list
        if value == '':
            data = food
        else:
            data = []
            for item in food:
                if value in item.lower():
                    data.append(item)                

        # update data in listbox
        listbox_update(data)
        
        
    def listbox_update(data):
        # delete previous data
        listbox.delete(0, 'end')
        
        # sorting data 
        data = sorted(data, key=str.lower)

        # put new data
        for item in data:
            listbox.insert('end', item)


    def on_select(event):
        global choice
        choice = event.widget.get(event.widget.curselection())
    def calculatornut():
        global food
        global listbox
        global output
        global entryGram
        # open the file in read mode
        food = []
        C.execute("select food from food")
        temp = C.fetchall()
        for i in temp:
            food.append(i[0])
        calnut = Tk()
        calnut.geometry("1024x768")
        calnut.config(bg = "black")
        Label(calnut, text="",bg="black").pack()
        Label(calnut, text="",bg="black").pack()
        
        label = Label(calnut, text ="Enter a product that you ate.",  bg = "cyan")
        label.pack()
        Label(calnut, text="",bg="black").pack()
        # user input, product
        label2 = Label(calnut, text = "Name: ", bg = "red")
        label2.pack()
        Label(calnut, text="",bg="black").pack()
        entry = Entry(calnut)
        entry.pack()

        entry.bind('<KeyRelease>', on_keyrelease)
        Label(calnut, text="",bg="black").pack()
        listbox = Listbox(calnut)
        listbox.pack()
        listbox.bind('<Double-Button-1>', on_select)
        listbox.bind('<<ListboxSelect>>', on_select)
        listbox_update(food)
        Label(calnut, text="",bg="black").pack()
        label3 = Label(calnut, text = "Amount: ", bg = "yellow")
        label3.pack()
        Label(calnut, text="",bg="black").pack()
        entryGram = Entry(calnut, width = 20, bg = "white")
        entryGram.pack()
        Label(calnut, text="",bg="black").pack()
        # sub
        # output
        label4 = Label(calnut, text = "These are the nutrition values:", bg = "white")
        label4.pack()
        Label(calnut, text="",bg="black").pack()

        output = Text(calnut, width = 20, height = 6, wrap = WORD, bg = "white")
        output.pack()
        Label(calnut, text="",bg="black").pack()
        display = Button(calnut, text = "Display amount of calories.",  command = calcheck)
        display.pack()
        Label(calnut, text="",bg="black").pack()
        adder = Button(calnut, text = "Add to tracker.", command = add)
        adder.pack()
        Label(calnut, text="",bg="black").pack()
        submitter = Button(calnut, text = "Submit",  command = submit,bg = "white")
        submitter.pack()
        Label(calnut, text="",bg="black").pack()
        goodbye = Button(calnut, text = "Back",  command = lambda:calnut.destroy(),bg = "white")
        goodbye.pack()
        calnut.mainloop()
    def add():
        global calsum
        calsum+=Product
        output.delete('1.0',tk.END)
        return
    def submit():
        C.execute("select day from cell_day")
        mk=C.fetchone()
        daz='Day'+str(mk[0])
        sqlcommand = "update calories set {} = {} where acc_name = {}".format(daz,calsum,cookie)
       
        C.execute("update calories set {} = {} where acc_name = \"{}\"".format(daz,calsum,cookie))
        mydb.commit()
    def improve():
        global nameEntry
        global kcalEntry
        def inserttable():
            C.execute("insert into food values('"+nameEntry.get()+"','"+str(kcalEntry.get())+"')")
            mydb.commit()
            threading.Timer(3, lambda:add.destroy()).start()

        add= Tk()
        add.config(bg = "black")
        label = Label(add, text ="Enter the product name and its nutritional "\
        "values per serving", bg = "black", fg = "white")
        label.pack()
        Label(add, text="",bg="black").pack()
        Label(add, text="",bg="black").pack()
        label1 = Label(add, text = "Name:", bg = "black", fg = "white")
        label1.pack()   
        Label(add, text="",bg="black").pack()
        nameEntry = Entry(add, width = 20, bg = "white")
        nameEntry.pack()
        a = nameEntry.get()
        Label(add, text="",bg="black").pack()
        label2 = Label(add, text = "Calories:", bg = "black", fg = "white")
        label2.pack()
        Label(add, text="",bg="black").pack()
        kcalEntry = Entry(add, width = 20, bg = "white")
        kcalEntry.pack()
        b = kcalEntry.get()
        Label(add, text="",bg="black").pack()
        submit = Button(add, text = "Submit", width = 8, command = inserttable)
        submit.pack(padx = 10, pady = 10)
        Label(add, text="",bg="black").pack()
        button3 = Button(add, text = "Back", width = 20, command = lambda: add.destroy())
        button3.pack(padx = 10, pady = 10)
        add.mainloop()
    
    def calcheck(): 
        global Product
        C.execute("select calories from food where food = \"{}\"".format(choice))
        K = C.fetchone()
        L = K[0]
        Product = int(L)*int(entryGram.get())
        statement = "You have gained "+str(Product)+" calories."
        
        output.insert(END, statement)
    NutcalMain = Tk()
    NutcalMain.title("App calculating nutrition values")
    NutcalMain.geometry('350x350')
    NutcalMain.config(bg = "black")
    label = Label(NutcalMain, text = "Welcome in a nutrition calculator!\n Choose an option.", bg = "black", fg = "white")
    label.pack()
    button = Button(NutcalMain, text = "Calculator", width = 20, command = calculatornut )
    button.pack(padx = 10, pady = 10)
    button2 = Button(NutcalMain, text = "Add a product", width = 20, command = improve )
    button2.pack()
    button3 = Button(NutcalMain, text = "Exit", width = 20, command = lambda: NutcalMain.destroy())
    button3.pack(padx = 10, pady = 10)
    NutcalMain.mainloop()
def register():
    def BMIREG():
        bmi=Tk()
        bmi.title("BMI Calculator")
        bmi.geometry("500x400")

        def Calculate():
            global fatty1
            global BMI
            weigh=int(weightentry.get())
            heigh=int(heightentry.get())
            gende=str(genderentry.get())
            ag=int(ageentry.get())
            BMI=(weigh/((heigh*heigh)/10000))
            BMI= round(BMI, 1)
            Label(bmi,text=f"{BMI}",font="arial 30 bold").place(x=200,y=290)
            fatty1=((1.20*BMI)+(0.23*ag)-10.8)
            fatty1= round(fatty1, 1)
            Label(bmi,text=f"{fatty1}",font="arial 30 bold").place(x=200,y=350)
            threading.Timer(5, lambda:bmi.destroy()).start()

        weight=Label(bmi, text="Weight(in kgs)", font="arial 15",fg="white",bg="black")
        height=Label(bmi, text="Height(in cm)", font="arial 15",fg="white",bg="black")
        gender=Label(bmi, text="Gender(M or F)" ,font="arial 15",fg="white",bg="black")
        age=Label(bmi, text="Age", font="arial 15",fg="white",bg="black")

        weight.place(x=50,y=20)
        height.place(x=50,y=90)
        gender.place(x=50,y=160)
        age.place(x=50, y=230)

        BMI=Label(bmi,text="BMI:",font="arial 15",fg="white",bg="black")
        BMI.place(x=50,y=300)
        fatty=Label(bmi,text="BODY FAT %:",font="arial 15",fg="white",bg="black")
        fatty.place(x=50,y=350)


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
        bmi.config(background="black")
        bmi.mainloop()
    
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
                    C.execute("insert into account values('"+username.get()+"','"+str(BMI)+"','"+password.get()+"','"+email.get()+"','"+str(fatty1)+"')")
                    C.execute("insert into steps (acc_name) values('"+username.get()+"')")
                    C.execute("insert into calories (acc_name) values('"+username.get()+"')")
                    C.execute("insert into steps_calories (acc_name) values('"+username.get()+"')")
                    mydb.commit()
                    
                    V.destroy()
                    rs.destroy()
                    return
                else:
                    messagebox.showwarning("Incorrect Verification Code"," Please enter the correct verification code.")
                    continue
        if username.get() == '':
          messagebox.showwarning("Username cant be blank"," Username cant be blank, please enter a valid username.")
          return
        C.execute("select * from account where acc_name='"+username.get()+"'")  
        K = C.fetchone()
        if K:
            messagebox.showwarning("Username in Use"," This username is already taken, please try another username.")
            return
        if BMI == 0:
            messagebox.showwarning("BMI NOT EVALUATED","Please calculate your BMI before making your account.")
            return
        while True:
            p = password.get()
            while True:
                pass_strength(p)
                break
            if passwordstrength == 100:
                break
            else:
                return
        C.execute("select * from account where email='"+email.get()+"'")  
        K = C.fetchone()
        if K:
            messagebox.showwarning("Duplicate ID","You already have an account with this email id? Would you like to recover your password instead? Click the forgot password button to do so.")
            return


        msg = "Welcome to Fitness Life!\nHere is your verification code:\n"+i+"\nWe welcome you to the start of your new fitness journey.\n\n\n\nPlease ignore this message if it doesn't concern you"
        mail(email.get(),"Account Registration- Verification Code",msg)
        messagebox.showinfo("Verification Code", "A verification code has been sent to your inbox.")    
        V = Tk()
        V.title("Make Your Account")
        V.geometry("429x265")
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
    rs.geometry("870x700")
    rs.config(bg="black")
    Label(rs, text="Make Your Account", bg="yellow",width=1366, height=10).pack()
    Label(rs, text="",bg="black").pack()
    Label(rs, text="",bg="black").pack()
    Label(rs, text="Enter account name: ", bg="cyan").pack()
    Label(rs, text="",bg="black").pack()
    username = Entry(rs)
    
    username.pack()
    u = username.get()
    Label(rs, text="",bg="black").pack()
    Button(rs, text="Evaluate BMI: ", bg="cyan", command= BMIREG).pack()
    Label(rs, text="",bg="black").pack()
    Label(rs, text="",bg="black").pack()
    Label(rs, text="Enter password: ", bg="cyan").pack()
    Label(rs, text="",bg="black").pack()
    password = Entry(rs)
    password.pack()
    Label(rs, text="",bg="black").pack()
    Label(rs, text="Enter email ID:", bg="cyan").pack()
    Label(rs, text="",bg="black").pack()
    email = Entry(rs)
    email.pack()
    Label(rs, text="",bg="black").pack()
    Label(rs, text="",bg="black").pack()

    Label(rs, text="",bg="black").pack()
    Button(rs, text="Register!", width=10, height=1, bg="red", command = create).pack()
    Label(rs, text="",bg="black").pack()
    rs.mainloop()

def graphcal():
    C.execute("select * from calories where acc_name = \"{}\"".format(cookie))
    result = C.fetchone()
    calories=list(result)
    Valuelist = []
    calories.pop(0)
    for i in calories:
        if i:
            Valuelist.append(i)
    days = []
    for i in range(1,len(Valuelist)+1):
        days.append(i)
    plt.figure(4)
    plt.plot(days,Valuelist)
    plt.xlabel("Day")
    plt.ylabel("Calories Consumed")
    plt.title("CALORIES")
    plt.show()
def sendmailsteps():
    img_format = 'png'
    f = io.BytesIO()
    C.execute("select * from steps where acc_name = \"{}\"".format(cookie))
    result = C.fetchone()
    steps=list(result)
    C.execute("select email from account where acc_name = \"{}\"".format(cookie))
    adress = C.fetchone()
    emailadress=list(adress)
    emailadressforsending = emailadress[0]
    C.execute("select BMI from account where acc_name = \"{}\"".format(cookie))
    BMI1 = C.fetchone()
    BMI2=list(BMI1)
    BMI3 = BMI2[0]
    C.execute("select BodyFat from account where acc_name = \"{}\"".format(cookie))
    BF1 = C.fetchone()
    BF2=list(BF1)
    BF3 = BF2[0]

    Valuelist = []
    steps.pop(0)    
    for i in steps:
        if i:
            Valuelist.append(i)
    days=[]
    for i in range(1,len(Valuelist)+1):
        days.append(i)
    plt.figure(3)
    plt.plot(days,Valuelist)
    plt.xlabel("Date")
    plt.ylabel("STEPS")
    plt.title("STEPS")
    plt.savefig("graph1",dpi = 100)
    msg = EmailMessage()
    msg['Subject'] = 'Your personalized fitness report.'
    msg['From'] = 'fitnesstracker@gmail.com'
    msg['To'] = emailadressforsending

    # set the plain text body
    msg.set_content('This is a plain text body.')

    # now create a Content-ID for the image
    image_cid = make_msgid()
    # if `domain` argument isn't provided, it will 
    # use your computer's name

    # set an alternative html body
    msg.add_alternative("""\
    <html>
        <body>
            <p>Your BMI is """+str(BMI3)+""" and your Body fat percentage is """+str(BF3)+"""."""+"""
            </p>
            <img src="cid:{image_cid}">
        </body>
    </html>
    """.format(image_cid=image_cid[1:-1]), subtype='html')
    # image_cid looks like <long.random.number@xyz.com>
    # to use it as the img src, we don't need `<` or `>`
    # so we use [1:-1] to strip them off


    # now open the image and attach it to the email
    with open('graph1.png', 'rb') as img:

        # know the Content-Type of the image
        maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

        # attach it
        msg.get_payload()[1].add_related(img.read(), 
                                            maintype=maintype, 
                                            subtype=subtype, 
                                            cid=image_cid)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login('fitnesstrackercasestudy@gmail.com', "Password@2021")
    session.send_message(msg)
    session.quit()
def sendmailcal():
    img_format = 'png'
    f = io.BytesIO()
    C.execute("select * from calories where acc_name = \"{}\"".format(cookie))
    result = C.fetchone()
    calories=list(result)
    C.execute("select email from account where acc_name = \"{}\"".format(cookie))
    adress = C.fetchone()
    emailadress=list(adress)
    emailadressforsending = emailadress[0]
    C.execute("select BMI from account where acc_name = \"{}\"".format(cookie))
    BMI1 = C.fetchone()
    BMI2=list(BMI1)
    BMI3 = BMI2[0]
    C.execute("select BodyFat from account where acc_name = \"{}\"".format(cookie))
    BF1 = C.fetchone()
    BF2=list(BF1)
    BF3 = BF2[0]
    Valuelist = []
    calories.pop(0)    
    for i in calories:
        if i:
            Valuelist.append(i)
    days=[]
    for i in range(1,len(Valuelist)+1):
        days.append(i)
    plt.figure(1)
    plt.plot(days,Valuelist)
    plt.xlabel("Date")
    plt.ylabel("CALORIES")
    plt.title("CALORIES")
    plt.savefig("graph2",dpi = 100)
    msg = EmailMessage()
    msg['Subject'] = 'Your personalized fitness report.'
    msg['From'] = 'fitnesstracker@gmail.com'
    msg['To'] = emailadressforsending

    # set the plain text body
    msg.set_content('This is a plain text body.')

    # now create a Content-ID for the image
    image_cid = make_msgid()
    # if `domain` argument isn't provided, it will 
    # use your computer's name

    # set an alternative html body
    msg.add_alternative("""\
    <html>
        <body>
            <p>Your BMI is """+str(BMI3)+""" and your Body fat percentage is """+str(BF3)+"""."""+"""
            </p>
            <img src="cid:{image_cid}">
        </body>
    </html>
    """.format(image_cid=image_cid[1:-1]), subtype='html')
    # image_cid looks like <long.random.number@xyz.com>
    # to use it as the img src, we don't need `<` or `>`
    # so we use [1:-1] to strip them off


    # now open the image and attach it to the email
    with open('graph2.png', 'rb') as img:

        # know the Content-Type of the image
        maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

        # attach it
        msg.get_payload()[1].add_related(img.read(), 
                                            maintype=maintype, 
                                            subtype=subtype, 
                                            cid=image_cid)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()


    session.login('fitnesstrackercasestudy@gmail.com', "Password@2021")
    session.send_message(msg)
    session.quit()

def graphstep():
    C.execute("select * from steps where acc_name = \"{}\"".format(cookie))
    result = C.fetchone()
    steps=list(result)
    Valuelist = []
    steps.pop(0)    
    for i in steps:
        if i:
            Valuelist.append(i)
    days=[]
    for i in range(1,len(Valuelist)+1):
        days.append(i)
    plt.figure(2)
    plt.plot(days,Valuelist)
    plt.xlabel("STEPS")
    plt.ylabel("Date")
    plt.title("STEPS")
    plt.show()
def BMIREEVAl():
    bmi=Tk()
    bmi.title("BMI Calculator")
    bmi.geometry("500x400")

    def Calculate():
        weigh=int(weightentry.get())
        heigh=int(heightentry.get())
        gende=str(genderentry.get())
        ag=int(ageentry.get())
        Reval=(weigh/((heigh*heigh)/10000))
        Reval= round(Reval, 1)
        Label(bmi,text=f"{Reval}",font="arial 30 bold").place(x=200,y=290)
        C.execute("update account set BMI = {} where acc_name = \"{}\"".format(Reval,cookie))
        
        fatty=((1.20*Reval)+(0.23*ag)-10.8)
        fatty= round(fatty, 1)
        Label(bmi,text=f"{fatty}",font="arial 30 bold").place(x=200,y=350)
        C.execute("update account set BodyFat = {} where acc_name = \"{}\"".format(fatty,cookie))

        
        mydb.commit()

        threading.Timer(5, lambda:bmi.destroy()).start()

    weight=Label(bmi, text="Weight(in kgs)", font="arial 15",fg="white",bg="black")
    height=Label(bmi, text="Height(in cm)", font="arial 15",fg="white",bg="black")
    gender=Label(bmi, text="Gender(M or F)" ,font="arial 15",fg="white",bg="black")
    age=Label(bmi, text="Age", font="arial 15",fg="white",bg="black")

    weight.place(x=50,y=20)
    height.place(x=50,y=90)
    gender.place(x=50,y=160)
    age.place(x=50, y=230)

    Reval=Label(bmi,text="BMI:",font="arial 15",fg="white",bg="black")
    Reval.place(x=50,y=300)
    
    fatty=Label(bmi,text="BODY FAT %:",font="arial 15",fg="white",bg="black")
    fatty.place(x=50,y=350)
    
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
    bmi.config(background="black")
    bmi.mainloop()
def nextday():
    C.execute("select day from cell_day")
    dz=C.fetchone()
    dayz=int(dz[0])
    if dayz==31:
        C.execute("update cell_day set day= 1")
        mydb.commit()
    else:
        dayz=dayz+1
        C.execute("update cell_day set day={}".format(dayz))
        mydb.commit()
def bmiwi():
    def stepstocal():
        def Calculate():
            C=mydb.cursor()
            C.execute("select BMI from FITNESS.account where acc_name= \"{}\"".format(cookie))
            abx=C.fetchone()
            bmii=float(abx[0])
            #heigh = int(heightentry.get())
            ste = int(stepsentry.get())
            ag = int(ageentry.get())
            cals = ((ste*(4/100)*bmii)/ag)
            cals = round(cals, 2)
            C.execute("select day from cell_day")
            mk=C.fetchone()
            daz='Day'+str(mk[0])
            C.execute("update steps set {} = {} where acc_name = \"{}\"".format(daz,ste,cookie))
            C.execute("update steps_calories set {} = {} where acc_name = \"{}\"".format(daz,cals,cookie))
            mydb.commit()
            Label(root, text=f"{cals}", font="arial 30 bold").place(x=200, y=220)


        root = Tk()
        root.title("Steps Calorie Calculator")
        root.geometry("600x400")

        #weight = Label(root, text="Weight(in kgs)", font="arial 15")
        #height = Label(root, text="Height(in cm)", font="arial 15")
        steps = Label(root, text="Steps Walked:", font="arial 15",bg="black",fg="white")
        age = Label(root, text="Age:", font="arial 15",bg="black",fg="white")

        #weight.place(x=50, y=20)
        #height.place(x=50, y=90)
        steps.place(x=50, y=20)
        age.place(x=70, y=80)

        cals = Label(root, text="Calories Burnt:", font="arial 15",fg="white",bg="black")
        cals.place(x=50, y=220)

        #weightvalue = StringVar()
        #heightvalue = StringVar()
        stepsvalue = StringVar()
        agevalue = StringVar()

        #weightentry = Entry(root, textvariable=weightvalue, font="arial 20", width=8)
        #heightentry = Entry(root, textvariable=heightvalue, font="arial 20", width=8)
        stepsentry = Entry(root, textvariable=stepsvalue, font="arial 20",width=8)
        ageentry = Entry(root, textvariable=agevalue, font="arial 20",width=8)

        #weightentry.place(x=200, y=20)
        #heightentry.place(x=200, y=90)
        stepsentry.place(x=200, y=20)
        ageentry.place(x=200,y= 80 )

        Button(root, text="Calculate", font="arial 15", command=Calculate,fg="yellow",bg="green").place(x=350, y=20)
        Button(root, text="Exit", command=lambda: root.destroy(), font="arial 15", width=8,fg="red",bg="black").place(x=350, y=80)
        root.config(background="black")
        root.mainloop() 
    bmiwind=Tk()
    bmiwind.geometry("1920x1080")

    label=Label(bmiwind,
                text="FITNESS TRACKER MENU",
                font=('Arial',29,'bold'),
                fg='yellow',
                bg='black',
                padx=10,
                pady=10,
                compound='top').pack()
    Label(bmiwind, text="",bg="black").pack()
    Label(bmiwind, text="",bg="black").pack()
    steptocal_button = Button(bmiwind, text="CALORIES BURNT", font=("Arial", 16, 'bold'), fg="red", bg='black',activeforeground='#5291ff',
                    activebackground='black', compound='top', command = stepstocal).pack()
    Label(bmiwind, text="",bg="black").pack()
    Label(bmiwind, text="",bg="black").pack()
    caloriegraph=Button(bmiwind,text="CAL GRAPH", font=("Arial",16,'bold'),fg="blue", bg='black',activeforeground='#5291ff',
                    activebackground='black', compound='top',command=graphcal).pack()
    Label(bmiwind, text="",bg="black").pack()
    Label(bmiwind, text="",bg="black").pack()
    stepgraph=Button(bmiwind,text="STEPS GRAPH", font=("Arial",16,'bold'),fg="BLUE", bg='black',activeforeground='#5291ff',
                    activebackground='black', compound='top',command=graphstep).pack()
    Label(bmiwind, text="",bg="black").pack()
    Label(bmiwind, text="",bg="black").pack()
    
    caloriesbutton = Button(bmiwind, text="CALORIE CAL", font=("Arial", 16, 'bold'), fg="red", bg='black',activeforeground='#5291ff',
                    activebackground='black', compound='top', command = NutrientCalculator).pack()
    
    Label(bmiwind, text="",bg="black").pack()
    Label(bmiwind, text="",bg="black").pack()

    Bmirevaluate = Button(bmiwind, text="Re-Evaluate your BMI", font=("Arial", 16, 'bold'), fg="red", bg='black',activeforeground='#5291ff',
                activebackground='black', compound='top', command = BMIREEVAl).pack()
    Label(bmiwind, text="",bg="black").pack()
    Label(bmiwind, text="",bg="black").pack()
    nextday_button=Button(bmiwind,text="NEXT DAY", font=("Arial",16,'bold'),fg="green", bg='black',activeforeground='#5291ff',
        activebackground='black', compound='top', command=nextday).pack()
    Label(bmiwind, text="",bg="black").pack()
    Label(bmiwind, text="",bg="black").pack()
    sendzastepsemail=Button(bmiwind,text="Send me a report on my steps count and general health.", font=("Arial",16,'bold'),fg="green", bg='black',activeforeground='#5291ff',
        activebackground='black', compound='top', command=sendmailsteps).pack()
    Label(bmiwind, text="",bg="black").pack()
    Label(bmiwind, text="",bg="black").pack()
    sendzacalemail=Button(bmiwind,text="Send me a report on my calorie intake and general health.", font=("Arial",16,'bold'),fg="green", bg='black',activeforeground='#5291ff',
        activebackground='black', compound='top', command=sendmailcal).pack()

    bmiwind.config(background="black")

    bmiwind.mainloop()

def check_pass():
    global cookie
    C.execute("select * from account where acc_name='"+usernameB.get()+"' and password='"+passwordB.get()+"'")
    k = C.fetchone()
    if k:
        cookie = usernameB.get()
        messagebox.showinfo("Succesful Login", "You have successfully logged in.")    
        bmiwi()
    else:
        messagebox.showwarning("Incorrect Details","Your username or password is incorrect.")


def forgot():
    global Change
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
            if str(verco.get())== str(rando):
                cpa()
                break
            else:
                messagebox.showwarning("Incorrect Verification Code"," Please enter the correct verification code.")
                break
    def cpa():
        global passnew
        global cp
        cp = Tk()
        cp.geometry("600x400")
        Label(cp, text="").pack()
        Label(cp, text="").pack()
        Label(cp, text="Enter new password: ", bg="Azure").pack()
        Label(cp, text="").pack()
        Label(cp, text="").pack()
        passnew = Entry(cp)
        passnew.pack()
        Label(cp, text="").pack()
        Label(cp, text="").pack()
        Button(cp, text="Change", width=30, height=5, bg="Aquamarine", command = cp1).pack()
        cp.mainloop()
    def cp1():
        while True:
            p = passnew.get()
            while True:
                pass_strength(p)
                break
            if passwordstrength == 100:
                break
            else:
                return
        C.execute("update account set password='"+passnew.get()+"' where email='"+emailo.get()+"'")
        mydb.commit()
        cp.destroy()
        Change.destroy()
        reset.destroy()
    def fga():
        global reset
        global verco
        msg = "You have requested to change your password.\nHere is your verification code:\n"+str(rando)+"\nEnter this code to reset your password\n\n\n\Didn't request to change your password? Someone else might be attempting to access your account."
        mail(emailo.get(),"Recovering your password",msg)
        messagebox.showinfo("Verification Code", "A verification code has been sent to your inbox.")    
        reset = Tk()
        reset.title("Make Your Account")
        reset.geometry("429x265")
        Label(reset, text="Enter verification code: ", bg="cyan").pack()
        Label(reset, text="").pack()
        verco = Entry(reset)
        verco.pack()
        Label(reset, text="").pack()
        Button(reset, text="OK", width=10, height=1, bg="red", command = confirm).pack()
        Label(reset, text="").pack()
        reset.mainloop()
    rando = random.randint(10000,99999)
    Change = Tk()
    Change.geometry("800x600")
    Change.config(bg = "black")

    Label(Change, text="Enter the email adress associated with your account.", bg="blue").pack()
    Label(Change, text="",bg = "black").pack()
    Label(Change, text="",bg = "black").pack()
    emailo = Entry(Change)
    emailo.pack()
    Label(Change, text="",bg = "black").pack()
    Label(Change, text="",bg = "black").pack()
    Button(Change, text="Submit", width=30, height=5, bg="lime", command = fga).pack()
    Label(Change, text="",bg = "black").pack()
    Label(Change, text="",bg = "black").pack()
    Change.mainloop()







windows=Tk()
a="1600x1000"
a = PhotoImage(file="download.png")
backImg = Label(image=a).place(x=1600,y=1000)
canvas= Canvas(windows,width= 1600, height= 1000)
canvas.pack(expand=True, fill= BOTH)
canvas.create_image(0,0,image=a, anchor="nw")
windows.geometry("1600x1000")
windows.title("FITNESS TRACKER 20")
usernameB=Entry(windows)
usernameB.place(x=750,y=220)
label=Label(windows,
            text="FITNESS TRACKER",
            font=('Arial',20,'bold'),
            fg='yellow',
            bg='black',
            compound='top').place(x=650,y=160)
username=Label(windows,
            text="username",
            font=('Arial',9,'bold'),
            fg='white',bg='black')
password=Label(windows,text="password",font=('Arial',9,'bold'),fg='white',bg='black').place(x=675,y=250)
new_user=Label(windows,text="if a new user click here",font=('Arial',9,'bold'),fg='#e60202',bg="black").place(x=645,y=320)
submit=Button(windows,text="Create Account",command=register,font=("Calibri",9),
              fg="white",bg='black',activeforeground='#5291ff',
              activebackground='black',
              compound='top').place(x=790,y=320)
passwordB=Entry(windows,show="*")
passwordB.place(x=750,y=250)
username.place(x=675,y=220)


button=Button(windows,text="login",command=check_pass,font=("commic sans",10),
              fg="#5291ff",bg='black',activeforeground='#5291ff',
              activebackground='black',
              compound='top')
forgotpass=Button(windows, text="FORGOT PASSWORD", font=('comic sans', 10),fg="#5291ff",bg='black',activeforeground='#5291ff',
              activebackground='black', command= forgot).place(x=710,y=350)             
button.place(x=750,y=280)

windows.config(background="black")

windows.mainloop()
