productList = {}


def file_open():
    """Opens the file, adds data into dict"""
    with open("Products.txt") as file:
        for row in file:
            if not row:
                continue
            else:
                product, values = row.split(',')
                productList[product] = values


def result(product, gram):
    """Calculates the nutritional values and returns result"""
    kcalValue = 0
    #check if user products are in the file
    if product in productList:
        kcal = productList[product]
        #calculating the nutritional values
        kcalValue += gram / 100 *int(kcal)
        outcome = "Your product provided you with %d kcal, "%(kcalValue)
    else:
        outcome = "Sorry, but we don't have this product in our database: %s, but you can add it! :)"% (product)
    return outcome











