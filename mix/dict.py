import csv
 
# open the file in read mode
filename = open('Test.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
food =[]
 
# iterating over each row and append
# values to empty list
for col in file:
    food.append(col["FOOD"])
