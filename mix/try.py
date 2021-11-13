import tkinter
from tkinter import ttk
from tkinter import *
import mysql.connector as my
import csv
mydb= my.connect(host='localhost',user='root',database='food',password="password")
C=mydb.cursor()
choice = ''
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

def Nutcal():
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
    calnut.geometry('1920x1080')
    label = Label(calnut, text ="Enter a product that you ate.", bg = "black", fg = "white")
    label.pack()
    # user input, product
    label2 = Label(calnut, text = "Name: ", bg = "black", fg = "white")
    label2.pack()
    entry = Entry(calnut)
    entry.pack()
    entry.bind('<KeyRelease>', on_keyrelease)
    listbox = Listbox(calnut)
    listbox.pack()
    listbox.bind('<Double-Button-1>', on_select)
    listbox.bind('<<ListboxSelect>>', on_select)
    listbox_update(food)
    label3 = Label(calnut, text = "Amount: ", bg = "black", fg = "white")
    label3.pack()
    entryGram = Entry(calnut, width = 20, bg = "white")
    entryGram.pack()
    # submit
    submit = Button(calnut, text = "Submit", width = 8, command = calcheck)
    submit.pack(padx = 10, pady = 10)
    # output
    label4 = Label(calnut, text = "These are the nutrinion values:", bg = "black", fg = "white")
    label4.pack()
    output = Text(calnut, width = 20, height = 6, wrap = WORD, bg = "white")
    output.pack()
    #going back to menu
    button = Button(calnut, text = "Back", width = 8, command = lambda:calnut.destroy())
    button.pack(padx = 10, pady = 10)
    calnut.mainloop()
def improve():
    global nameEntry
    global kcalEntry

    add= Tk()
    label = Label(add, text ="Enter the product name and its nutritional "\
    "values per serving", bg = "black", fg = "white")
    label.pack()
    label1 = Label(add, text = "Name:", bg = "black", fg = "white")
    label1.pack()
    nameEntry = Entry(add, width = 20, bg = "white")
    nameEntry.pack()
    a = nameEntry.get()
    label2 = Label(add, text = "Calories:", bg = "black", fg = "white")
    label2.pack()
    kcalEntry = Entry(add, width = 20, bg = "white")
    kcalEntry.pack()
    b = kcalEntry.get()
    submit = Button(add, text = "Submit", width = 8, command = inserttable)
    submit.pack(padx = 10, pady = 10)
    button3 = Button(add, text = "Back", width = 20, command = lambda: add.destroy())
    button3.pack(padx = 10, pady = 10)
    add.mainloop()
def inserttable():
    C.execute("insert into food values('"+nameEntry.get()+"','"+str(kcalEntry.get())+"')")
    mydb.commit()
def calcheck(): 
    C.execute("select calorie from food where food = '{}'".format(choice))
    K = C.fetchone()
    L = K[0]
    Product = int(L)*int(entryGram.get())
    statement = "You have gained "+str(Product)+" calories."
    output.insert(END, statement)

Nutcal()