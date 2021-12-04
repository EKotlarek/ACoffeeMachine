Github link: https://github.com/EKotlarek/ACoffeeMachine

The class CoffeeMachine allows the user to choose a drink they want to make. Then, it deducts the necessary supplies from the machine. If the machine does not have enough supplies to make the drink, it will print a message that tells the user what supply the machine ran out of. After the drink has been chosen, whether it was able to make the drink or not, the machine turns off.

-------Variables-------

The running variable is a boolean that controls whether the machine is on or not. The machine will turn on when the program starts, and turns off when the drink has been made or there are not enough supplies to make a drink.

In the __init__ method of CoffeeMachine, the variables water, milk, beans, and cups are initialized. The water variable is an integer that stores how much water is in the machine. The milk variable is an integer that stores how much milk is in the machine. The beans variable is an integer that stores how many coffee beans are in the machine. The cups variable is an integer that stores how many cups are available.

The action variable is a string that stores the user's input. If the input is "make" then the machine makes a drink, and if the input is "exit", the program stops.

The __not_available variable is a string that stores a supply that is below zero. When __not_available has the name of a supply stored in it, the machine is out of that supply.

The __choice variable is a string that keeps track of which drink the user wants to make. When the drink is chosen, then the machine can calculate how many supplies it will take to make it.

-------Methods-------

The __init__ method initializes the supplies the machine already has and starts the machine. It takes the arguments self, water, milk, coffee_beans, and cups.

The start method turns the machine on and initiates the method that will ask the user which drink they want. It does not take any arguments nor return anything.

The return_to_beginning method prints a new line and continues the program from the start method. It takes self as an argument and doesn't return anything.

The get_water method retrieves the current water amount. It takes only the self argument and returns self.water.

The get_milk method retrieves the current milk amount. It takes only the self argument and returns self.milk.

The get_coffee_beans method retrieves the current coffee bean amount. It takes only the self argument and returns self.beans.

The get_cups method retrieves the current cup amount. It takes only the self argument and returns self.cups.

The set_water method subtracts an amount from the total water amount and returns the result. It takes self and quantity as arguments.

The set_milk method subtracts an amount from the total milk amount and returns the result. It takes self and quantity as arguments.

The set_coffee_beans method subtracts an amount from the total coffee bean amount and returns the result. It takes self and quantity as arguments.

The set_cups method subtracts an amount from the total cup amount and returns the result. It takes self and quantity as arguments.

The supply_check method checks whether the coffee machine is out of any of the supplies. It takes self as an argument. It returns True if the machine is fully stocked and returns False if the machine is out of something.

The make method makes the drink for the user. It takes self as an argument and doesn't return anything. It removes the necessary quantities of supplies from the machine and prints a statement if the drink was able to be made.

-------Demo Program-------

Description:
In the demo program, a Coffeemachine object is created with the initial values of 400ml of water, 540ml of milk, 120g of coffee beans, and 9 cups. Then, it runs through the Coffeemachine class until the user chooses to exit. At the end of the program, it will print out the values of the supplies.

Instructions:
Run Your_Own_Class.py in the command line and input necessary information when prompted.
