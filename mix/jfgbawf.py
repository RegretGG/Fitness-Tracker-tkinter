import csv
import mysql
import mysql.connector as my
mydb= my.connect(host='localhost',user='root',database='food',password="password")
C=mydb.cursor()

# open the file in read mode
filename = open('test.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
food =[]
 
# iterating over each row and append
# values to empty list
for col in file:
    food.append(col["Food"].strip())
print(food)
C.executemany("""INSERT INTO food (food) VALUES (%s)""",zip(food))
mydb.commit()
