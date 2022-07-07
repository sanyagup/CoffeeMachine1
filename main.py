MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def calculations():
    quarters = int(input("How many quarters?: "))
    nickels = int(input("How many nickels?: "))
    dimes = int(input("How many dimes?: "))
    pennies = int(input("How many pennies: "))
    q = .25
    n = .5
    d = .10
    p = .01
    money = q * quarters + n * nickels + d * dimes + p * pennies
    return money


def check(resources, MENU, choice, user_money):

    milk1 = 0
    water1 = 0
    coffee1 = 0
    change = 0
    cost1 = 0

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    if choice == "espresso":
        water1 = MENU["espresso"]["ingredients"]["water"]
        coffee1 = MENU["espresso"]["ingredients"]["coffee"]
        cost1 = MENU["espresso"]["cost"]
    if choice == "latte":
        water1 = MENU["latte"]["ingredients"]["water"]
        coffee1 = MENU["latte"]["ingredients"]["coffee"]
        milk1 = MENU["latte"]["ingredients"]["milk"]
        cost1 = MENU["latte"]["cost"]
    if choice == "cappuccino":
        water1 = MENU["cappuccino"]["ingredients"]["water"]
        coffee1 = MENU["cappuccino"]["ingredients"]["coffee"]
        milk1 = MENU["cappuccino"]["ingredients"]["milk"]
        cost1 = MENU["cappuccino"]["cost"]

    print(cost1)
    if water < water1:
        print("Sorry there is not enough water left. ")
        return -1
    if milk < milk1:
        print("Sorry there is not enough milk left. ")
        return -1
    if coffee < coffee1:
        print("Sorry there is not enough coffee left. ")
        return -1
    if user_money < cost1:
        print("You do not have enough money to purchase this. ")
        return -1
    if user_money > cost1:
        change = cost1 - user_money
        user_money -= cost1
        return change


cup_counter = 0
user_money = 0
total_money = 0
while cup_counter >= 0:
    user_money = 0
    print(f"cup_counter {cup_counter}")
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        for x in resources:
            print(f"{x}: {resources[x]}")
        print(f"Money: ${total_money}")
    if choice == "espresso":
        user_money = calculations()
        user_change = check(resources, MENU, choice, user_money)
        if user_change == -1:
            choice1 = input(f"Would you like to purchase something else besides {choice}? y or n: ")
            if choice1 == "n":
                cup_counter = -1
        else:
            print(f"Your change is {user_change}")
            cup_counter += 1
    if choice == "off":
        cup_counter = -1

