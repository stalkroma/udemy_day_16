from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_name = CoffeeMaker()
money = MoneyMachine()
menu_drink = Menu()
machine_on = True

""" TODO 4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough resources
to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not
continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
"""
while machine_on:
    drink = input('What wo  uld you like? (espresso/latte/cappuccino/):').lower()
    if drink == 'off':
        print("Machine off have a nice day")
        machine_on = False

    elif drink == 'report':
        coffee_name.report()
        money.report()
    else:
            if any(item.name == drink for item in menu_drink.menu):
                print("git")
                if coffee_name.is_resource_sufficient(menu_drink.find_drink(drink)) == False:
                    continue
                coffee_name.make_coffee(menu_drink.find_drink(drink))
            else:
                print("nie ma takiego napoju")




    #    print(f"We doesn't have {drink}. You can order only espresso or latte or cappuccino")
