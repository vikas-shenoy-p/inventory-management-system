import ProductInventory as Pi


def main():
    i = Pi.inventory()
    while True:
        print("1. To insert\n2. To delete\n3. Display\n4. Calculate sum")
        ch = int(input("Enter your choice"))

        if ch == 1:
            name = input("Enter product name")
            price = int(input("Enter price"))
            quantity = int(input("Enter quantity"))
            i.addProduct(name, price, quantity)

        elif ch == 2:
            id = int(input("Enter product id"))
            i.delProduct(id)

        elif ch == 3:
            i.display()

        elif ch == 4:
            print(i.sumValue(),"\n")

        else:
            print("Enter valid choice")

if __name__ == '__main__':
    main()