from tkinter import *

def openNewWindow():
    def Calculate():
        weigh = int(weightentry.get())
        heigh = int(heightentry.get())
        gende = str(genderentry.get())
        ag = int(ageentry.get())
        BMI = (weigh / ((heigh * heigh) / 10000))
        BMI = round(BMI, 1)
        Label(root, text=f"{BMI}", font="arial 30 bold").place(x=200, y=290)



    root = Tk()
    root.title("BMI Calculator")
    root.geometry("1000x600")
    weight = Label(root, text="Weight(in kgs)", font="arial 15")
    height = Label(root, text="Height(in cm)", font="arial 15")
    gender = Label(root, text="Gender(M or F)", font="arial 15")
    age = Label(root, text="Age", font="arial 15")

    weight.place(x=50, y=20)
    height.place(x=50, y=90)
    gender.place(x=50, y=160)
    age.place(x=50, y=230)

    BMI = Label(root, text="BMI:", font="arial 15")
    BMI.place(x=50, y=300)

    weightvalue = StringVar()
    heightvalue = StringVar()
    gendervalue = StringVar()
    agevalue = StringVar()

    weightentry = Entry(root, textvariable=weightvalue, font="arial 20", width=8)
    heightentry = Entry(root, textvariable=heightvalue, font="arial 20", width=8)
    genderentry = Entry(root, textvariable=gendervalue, font="arial 20", width=8)
    ageentry = Entry(root, textvariable=agevalue, font="arial 20", width=8)

    weightentry.place(x=200, y=20)
    heightentry.place(x=200, y=90)
    genderentry.place(x=200, y=160)
    ageentry.place(x=200, y=230)

    Button(root, text="Calculate", font="arial 15", command=Calculate).place(x=350, y=20)
    Button(root, text="Exit", command=lambda: exit(), font="arial 15", width=8).place(x=350, y=90)

    root.mainloop()
def stepper():
    def stepsbutton():
        weigh = int(weightentry.get())
        heigh = int(heightentry.get())
        ste = int(stepsentry.get())
        ag = int(ageentry.get())
        cals = ((ste * (4 / 100) * (weigh / ((heigh * heigh) / 10000))) / ag)
        cals = round(cals, 2)
        Label(root, text=f"{cals}", font="arial 30 bold").place(x=200, y=290)


    root = Tk()
    root.title("Steps Calorie Calculator")
    root.geometry("1000x600")
    weight = Label(root, text="Weight(in kgs)", font="arial 15")
    height = Label(root, text="Height(in cm)", font="arial 15")
    steps = Label(root, text="Steps Walked", font="arial 15")
    age = Label(root, text="Age", font="arial 15")

    weight.place(x=50, y=20)
    height.place(x=50, y=90)
    steps.place(x=50, y=160)
    age.place(x=50, y=230)

    cals = Label(root, text="Calories Burnt:", font="arial 15")
    cals.place(x=50, y=300)

    weightvalue = StringVar()
    heightvalue = StringVar()
    stepsvalue = StringVar()
    agevalue = StringVar()

    weightentry = Entry(root, textvariable=weightvalue, font="arial 20", width=8)
    heightentry = Entry(root, textvariable=heightvalue, font="arial 20", width=8)
    stepsentry = Entry(root, textvariable=stepsvalue, font="arial 20", width=8)
    ageentry = Entry(root, textvariable=agevalue, font="arial 20", width=8)

    weightentry.place(x=200, y=20)
    heightentry.place(x=200, y=90)
    stepsentry.place(x=200, y=160)
    ageentry.place(x=200, y=230)

    Button(root, text="Calculate", font="arial 15", command=Calculate).place(x=350, y=20)
    Button(root, text="Exit", command=lambda: exit(), font="arial 15", width=8).place(x=350, y=90)

    root.mainloop()




def bmiwi():
    bmiwind=Tk()
    bmiwind.geometry("420x420")

    label=Label(bmiwind,
                text="FITNESS TRACKER",
                font=('Arial',12,'bold'),
                fg='black',
                bg='#5291ff',
                padx=10,
                pady=10,
                compound='top').place(x=110,y=0)
    caloriecal=Label(bmiwind,text="calculate calorie",font=('Arial',9,'bold'),fg='black',bg='#5291ff').place(x=75,y=200)
    steps=Label(bmiwind,text="no of steps",font=('Arial',9,'bold'),fg='black',bg='#5291ff').place(x=75,y=170)
    bmigo=Label(bmiwind,text="want to go to bmi",font=('Arial',9,'bold'),fg='black',bg='#5291ff').place(x=75,y=130)


    submit=Button(bmiwind,text="go to bmi",command=openNewWindow,font=("Arial",8,'bold'),fg="white",bg='black',activeforeground='#5291ff',
                  activebackground='black',compound='top').place(x=180,y=130)

    caloriesbutton = Button(bmiwind, text="calorie cal", command=stepper, font=("Arial", 8, 'bold'), fg="white", bg='black',activeforeground='#5291ff',
                    activebackground='black', compound='top').place(x=190,y=200)

    entry1=Entry(bmiwind,).place(x=150,y=170)
    bmiwind.config(background="#5291ff")

    bmiwind.mainloop()

windows=Tk()
a="420x420"
windows.geometry(a)
windows.title("FITNESS TRACKER")
entry=Entry(windows,).place(x=150,y=170)
pic=PhotoImage(file='Hnet.com-image (1).png')
pic1=PhotoImage(file='Hnet.com-image (3).png')
label=Label(windows,
            text="FITNESS TRACKER",
            font=('Arial',12,'bold'),
            fg='black',
            bg='#66c9ff',
            padx=20,
            pady=20,
            compound='top')
username=Label(windows,
            text="username",
            font=('Arial',9,'bold'),
            fg='black',bg='#5291ff')
password=Label(windows,text="password",font=('Arial',9,'bold'),fg='black',bg='#5291ff').place(x=80,y=190)
new_user=Label(windows,text="if a new user click here",font=('Arial',9,'bold'),fg='#e60202',bg="#5291ff").place(x=15,y=270)
submit=Button(windows,text="submit",command=openNewWindow,font=("Calibri",9),
              fg="white",bg='black',activeforeground='#5291ff',
              activebackground='black',
              compound='top').place(x=175,y=270)
entry1=Entry(windows,).place(x=150,y=190)
username.place(x=80,y=170)

label_2=Label(windows,image=pic)
label_2.place(x=150,y=65)
button=Button(windows,text="login",command=bmiwi,font=("commic sans",10),
              fg="#5291ff",bg='black',activeforeground='#5291ff',
              activebackground='black',
              compound='top')
button.place(x=175,y=220)
label.place(x=100,y=0)
icon=PhotoImage(file='download.png')
windows.iconphoto(True,icon)#icon of the tkinter on the top bar
windows.config(background="#5291ff")

windows.mainloop()