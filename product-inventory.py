class product(object):
    """
    A class to represent a product

    .....

    Attributes
    -----------
    id : This is created automatically using in-built function id(), which creates unique id for each object
    name : name of the product
    price(only positive integer) : price of the product in dollars
    quantity(only positive integer) : indicates the quantity of a product

    """
    def __init__(self, name, price, quantity):
        self.id = id(self)
        self.name = name
        self.price = price
        self.quantity = quantity


class inventory(object):
    """
    A class to manage inventory items
    """
    products = {} # dictionary used to store objects of class product

    def __init__(self):
        pass

    def display(self):
        """Displays all the products present in the inventory"""
        for key in self.products.keys():
            print(f"{key}  {self.products[key].name}   ${self.products[key].price} X  {self.products[key].quantity}")

    def sumValue(self):
        """Calculates the total amount by multiplying product s quantity and price"""
        sum = 0
        for key in self.products.keys():
            sum += self.products[key].price * self.products[key].quantity
        return sum

    def addProduct(self, name, price, quantity = 1):
        """Adds product to the dictionary with default quantity as 1"""
        pro = product(name, price, quantity)
        self.products[pro.id] = pro
        print("added\n")

    def delProduct(self, id):
        """ Deletes a product using its id"""
        try:
            del self.products[id]
        except:
            print("wrong id")