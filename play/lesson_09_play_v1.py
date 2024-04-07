class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)


class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu

    def update_menu(self, new_coffee):
        add_new = input("Hi Barista, Would you like to add a new type of coffee to the menu? (yes/no) ")
        already_printed = False
        if add_new == "yes":
            new_coffee = input("That's great! What new type of coffee would you like to add to the menu? ")
            self.coffee_menu.append(new_coffee)
        elif add_new == "no":
            if not already_printed:
                print("Thank you, no new coffees have been added to the menu.")
                already_printed = True
        else:
            print("Sorry, I do not understand your input. Please enter 'yes' or 'no'.") 



    def make_coffee(self, coffee_type):
        while True:
            coffee_type = input("Hello Uncle Monty's Cafe customer, what type of coffee would you like to order? ")
            if coffee_type in self.coffee_menu:
                print("Excellent choice! I will make your " + coffee_type + " now.")
                break
            else:
                print("Oh no!, we don't have your coffee. These are the coffees on our menu: ")
                for item in self.coffee_menu:
                    print("- " + item)
                    input("Please select a coffee from the above menu.")    




my_coffee_machine = SmartCoffeeMachine(12334254, 'Ragdoll')
my_coffee_machine.report()
my_coffee_machine.update_menu('latte')
my_coffee_machine.update_menu('hazelnut latte')
my_coffee_machine.make_coffee('hazelnut latte')
my_coffee_machine.make_coffee('salted caramel latte')

