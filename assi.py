print("WELCOME TO FRUIT MARKET")

fruit_stock = {}

print("(1) Manager\n(2) Customer")
choice1 = int(input("Select your role: "))

if choice1 == 1:
    while True:
        print("\n(1) Add Fruit Stock\n(2) View Fruit Stock\n(3) Update Fruit Stock\n(4) Exit")
        choice2 = int(input("Enter your choice: "))

        if choice2 == 1:  # Add Fruit Stock
            print("ADD FRUIT STOCK")
            fruit = input("Enter the fruit name: ").lower()
            quantity = int(input("Enter the quantity: "))

            if fruit in fruit_stock:
                fruit_stock[fruit] += quantity  # Update existing stock
            else:
                fruit_stock[fruit] = quantity  # Add new fruit to stock

            print(f"{quantity} {fruit}(s) added successfully!\n")

        elif choice2 == 2:  # View Fruit Stock
            if not fruit_stock:
                print("No stock available!\n")
            else:
                print("\nCurrent Fruit Stock:")
                for fruit, quantity in fruit_stock.items():
                    print(f"{fruit.capitalize()}: {quantity}")
                print()

        elif choice2 == 3:  # Update Fruit Stock
            print("UPDATE FRUIT STOCK")
            fruit = input("Enter the fruit name to update: ").lower()

            if fruit in fruit_stock:
                new_quantity = int(input("Enter the new quantity: "))
                fruit_stock[fruit] = new_quantity
                print(f"{fruit.capitalize()} stock updated to {new_quantity}!\n")
            else:
                print(f"{fruit.capitalize()} not found in stock!\n")

        elif choice2 == 4:  # Exit
            print("Exiting Manager Mode...")
            break

        else:
            print("Invalid choice! Please select a valid option.\n")

if choice1 == 2:
    menu={
    'apple':40,
    'orange':60,
    'mango':80,
    'banana':30,
    'watermelon':20,
}
bill=0
print("Welcome To Fruit Market")

for key in menu:
    print(key.ljust(15),"-",menu[key])
    
while True:
    order=input("Enter the item  or type Done to End :")
    order =  order.casefold()
    if order=="done":
        print("Thank You For Visting Fruit Market ")
        break
    elif order in menu:
        quantity=int(input("Enter ther quantity :"))
        bill=bill+(menu[order]*quantity)
    else:
        print("Enter the correct item")
print("Total bill=",bill)


