import sys
class coffee_Machine:

    c_No = ["1", "2", "3", "4"]
    c_name = ["Cappuccino", "Espresso", "Latte", "Black"]
    c_Price = [1.20, 1.25, 2.00, 0.90]
    c_Origin = ["Italy", "Italy", "Italy", "Sri Lanka"]
    c_Availability = [6, 5, 18, 0]
    coffeeBrewed = 0
    coffeeBalance = 0



class c_menu(coffee_Machine):
    def menu(self):
        print(" ")

        print("<--------WELCOME to Coffee Machine--------->")
        print("<--------(MENU) --------->")
        i = 0
        while i < len(coffee_Machine.c_name):
            print(i + 1, coffee_Machine.c_name[i], coffee_Machine.c_Origin[i],"£{:.2f}".format(coffee_Machine.c_Price[i]))
            i = i + 1
        print(" ")


class userChoice(c_menu):
    def choice(self):
        userInput = input("Operator or Customer? [1 --> OPERATOR] | [2 --> CUSTOMER] : ")
        if userInput == "1":
            print(
                "1. Add Coffee Type\n"
                "2. Modify Coffee Details\n"
                "3. Update Raw Material Stock\n"
                "4. View Coffee  Brewed Status\n"
                "5. Delete Coffee Type\n"
                "6. Exit")

            operator = input("What do you want to do? :")
            if operator == "1":
                name = input("Enter new coffee type :")
                price = float(input("Enter new coffee price :"))
                availability = int(input("Enter the coffee available stock :"))
                origin = input("Enter the coffee origin country :")
                coffee_Machine.c_name.append(name)
                coffee_Machine.c_Price.append(price)
                coffee_Machine.c_Availability.append(availability)
                coffee_Machine.c_Origin.append(origin)
                print("Successfully added the Coffee Type..")

            elif operator == "2":
                while i < len(coffee_Machine.c_name):
                    print(i + 1, coffee_Machine.c_name[i])
                    i = i + 1
                    us_i = int(input("Which coffee you need to modify : "))
                    price = float(input("Enter the new coffee price :"))
                    coffee_Machine.c_Price[us_i - 1] = price
                    print("Coffee Details updated successfully..")

            elif operator == "3":
                i = 0
                while i < len(coffee_Machine.c_name):
                    print(i + 1, coffee_Machine.c_name[i])
                    i = i + 1
                    us_i = int(input("Which coffee's availability you need to update :"))
                    availability = int(input("Enter the new availability stock :"))
                    coffee_Machine.c_Availability[us_i - 1] = availability
                    print("Updated coffee availability..")

            elif operator == "4":
                coffee_Machine.coffeeBalance = sum(coffee_Machine.c_Availability)
                print("\nNumber of Coffees brewed till now : ", coffee_Machine.coffeeBrewed)
                print("]\nNumber of Coffees that available : ", coffee_Machine.coffeeBalance)

            elif operator == "5":
                i = 0
                while i < len(coffee_Machine.c_name):
                    print(i + 1, coffee_Machine.c_name[i])
                    i = i + 1
                    code = int(input("Select the coffee type to be deleted"))
                    coffee_Machine.c_name.pop(code - 1)
                    coffee_Machine.c_Price.pop(code - 1)
                    coffee_Machine.c_Availability.pop(code - 1)
                    coffee_Machine.c_Origin.pop(code - 1)
                    print("Coffee Details Deleted successfully!!!")

            elif operator == "6":
                sys.exit()

        elif userInput == "2":
            served = 0
            while served == 0:
                choice = int(input("1.Cappuccino\t2.Espresso\t3.Latte\t4.Black\n" 
                                   "Which coffee you would like to have : "))
                if coffee_Machine.c_Availability[choice - 1] > 0:
                    coffee_Machine.coffeeBrewed = coffee_Machine.coffeeBrewed + 1
                    print("\n\nCollect & Enjoy Your Coffee..")
                    coffee_Machine.c_Availability[choice - 1] = coffee_Machine.c_Availability[choice - 1] - 1
                    served = 1
                else:
                    print("\nSelected Coffee is Out of Stock.Please try another.. ")



        else:
            print("Invalid input..")


vm = coffee_Machine()
c1 = c_menu()
u1 = userChoice()
while 1:

    userInput1 = input("\n\nWant to On this Coffee Machine?\nPress Y to continue\t:")
    if userInput1 == "Y":
        c1.menu()
        u1.choice()
    else:
        print("Invalid Choice.............")