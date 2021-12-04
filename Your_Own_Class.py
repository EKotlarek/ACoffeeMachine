# Emma Kotlarek
# Assignment 10.1: Your Own Class
# Requires: 1 class variable, 2 data variable, 2 get-set methods, 2 other methods

class CoffeeMachine():

    running = False

    def __init__(self, water, milk, coffee_beans, cups):
        # initialize the item quantities the machine already has
        self.water = water
        self.milk = milk
        self.beans = coffee_beans
        self.cups = cups

        # if the machine is not running, then start running
        if not CoffeeMachine.running:
            self.start()

    # if the machine is running, then prepare to make a drink
    def start(self):
        self.running = True
        self.action = input("Do you want to [make] a drink or [exit]?")
        if self.action == "make":
            self.make()
        if self.action() == "exit":
            exit()

    def return_to_beginning(self):
        print()
        self.start()

    # retrieve the current quantity of the supplies
    def get_water(self):
        return self.water

    def get_milk(self):
        return self.milk

    def get_coffee_beans(self):
        return self.beans

    def get_cups(self):
        return self.cups

    # set methods for when the class uses a supply
    def set_water(self, quantity):
        return self.water - quantity

    def set_milk(self, quantity):
        return self.milk - quantity

    def set_coffee_beans(self, quantity):
        return self.beans - quantity

    def set_cups(self, quantity):
        return self.cups - quantity

    # checks whether the chosen drink can be made with the current supplies by checking whether the supplies go below zero after the necessary supplies are deducted
    def supply_check(self):
        self.__not_available = ""

        if self.get_water() < 0:
            self.__not_available = "water"

        elif self.get_milk() < 0:
            self.__not_available = "milk"

        elif self.get_coffee_beans() < 0:
            self.__not_available = "coffee beans"

        elif self.get_cups() < 0:
            self.__not_available = "cups"

        # If something is below zero after being deducted tell the user there is not enough
        if self.not_available != "":
            print(f"Sorry, not enough {self.__not_available}!")
            return False
        # if there are enough supplies tell the user their coffee is being made
        else:
            print("The machine is fully stocked, now making your coffee!")
            return True

    def make(self):
        self.__choice = input("What do you want? 1 - espresso, 2 - latte, 3 - cappuccino\n")
        # checks which option they want and whether there are supplies to make it
        if self.__choice == '1' & self.supply_check == True: 
            # set the quantities of supplies to what is needed to make an espresso
            self.set_water(250)
            self.set_milk(0)
            self.set_coffee_beans(16)
            self.set_cups(1)
            print("Here's your espresso!")

        # checks which option they want and whether there are supplies to make it
        elif self.__choice == '2' & self.supply_check == True:
            # set the quantities of supplies to what is needed to make a latte
            self.set_water(350)
            self.set_milk(75)
            self.set_coffee_beans(20)
            self.set_cups(1)
            print("Here's your latte!")

        # checks which option they want and whether there are supplies to make it
        elif self.__choice == '3' & self.supply_check == True:
            # set the quantities of supplies to what is needed to make a cappuccino
            self.set_water(200)
            self.set_milk(100)
            self.set_coffee_beans(12)
            self.set_cups(1)
            print("Here's your cappuccino!")

        # turn off the coffee machine after making a drink
        self.return_to_beginning()

def main():
    # initialize a CoffeeMachine object with 400ml of water, 540ml of milk, 120g of coffee beans, and 9 cups
    machine1 = CoffeeMachine(400, 540, 120, 9)
    print(f"The remaining supplies are: water - {machine1.get_water()}, milk - {machine1.get_milk()}, coffee beans - {machine1.get_coffee_beans()}, and cups - {machine1.get_cups()}")

if __name__ == "__main__":
    main()
