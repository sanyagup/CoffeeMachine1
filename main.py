import decimal

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
    n = .05
    d = .10
    p = .01
    money = q * quarters + n * nickels + d * dimes + p * pennies
    return money


def check(resources, MENU, choice, user_money):
    two_places = decimal.Decimal(10) ** -2
    milk1 = 0
    water1 = 0
    coffee1 = 0
    change = 0
    cost1 = 0
    choice1 = " "
    counter = 0

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

    if water < water1:
        print("Sorry there is not enough water left. ")
        counter += 1
    elif user_money >= 0:
        resources["water"] = water - water1
    if milk < milk1:
        print("Sorry there is not enough milk left. ")
        counter += 1
    elif user_money >= 0:
        resources["milk"] = milk - milk1
    if coffee < coffee1:
        print("Sorry there is not enough coffee left. ")
        counter += 1
    elif user_money >= 0:
        resources["coffee"] = coffee - coffee1
    if counter > 0:
        choice1 = input(f"Would you like to purchase something else besides {choice}? y or n: ")
        if choice1 == "n":
            return "n"
        if choice1 == "y":
            return "y"
    else:
        return resources


cup_counter = 0
user_money = 0
total_money = 0.0
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]
espresso_price = MENU["espresso"]["cost"]
two_places = decimal.Decimal(10) ** -2
buy = True

while cup_counter >= 0:
    user_money = 0
    price = 0.0
    change = 0
    cost1 = 0
    print(f"Latte price: {latte_price}, Cappuccino price: {cappuccino_price}, Espresso price: {espresso_price}")
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        for x in resources:
            print(f"{x}: {resources[x]}")
        print(f"Money: ${total_money}")

    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if choice == "espresso":
            cost1 = MENU["espresso"]["cost"]
        if choice == "latte":
            cost1 = MENU["latte"]["cost"]
        if choice == "cappuccino":
            cost1 = MENU["cappuccino"]["cost"]

        user_money = calculations()
        if user_money < cost1:
            user_money = 0.0
            print("You do not have enough money to purchase this. ")
            choice1 = input(f"Would you like to purchase something else besides {choice}? y or n: ")
            if choice1 == "n":
                break
            if choice1 == "y":
                user_money = 0.0
                choice = " "

        used_resources = check(resources, MENU, choice, user_money)
        if used_resources == "n":
            break
        if used_resources == "y":
            buy = False

    if buy is True:
        if user_money > cost1 or user_money == cost1:
            change = decimal.Decimal(user_money - cost1).quantize(two_places)
            user_money -= cost1
            print(f"Thank you for purchasing {choice}. Have a great day!!")
            print(f"Your change is {change}")
            if choice == "espresso":
                price = MENU["espresso"]["cost"]
                total_money += price
                total_money = decimal.Decimal(total_money).quantize(two_places)
            if choice == "latte":
                price = decimal.Decimal(MENU["latte"]["cost"]).quantize(two_places)
                total_money += price
                total_money = decimal.Decimal(total_money).quantize(two_places)
            if choice == "cappuccino":
                price = MENU["cappuccino"]["cost"]
                total_money = decimal.Decimal(total_money).quantize(two_places)
                total_money += decimal.Decimal(price).quantize(two_places)
            cup_counter += 1
    if choice == "off":
        cup_counter = -1

