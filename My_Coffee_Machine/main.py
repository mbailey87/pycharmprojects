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

def start():
    on = True
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }

    def make_drink(drink):
        nonlocal resources
        for ingredient_name in drink:
            resources[ingredient_name] -= drink[ingredient_name]
        return resources
    while on:

        # TODO: order
        order = input("Choose your coffee 'espresso', 'latte', or 'cappuccino':\n").lower()

        if order == "off":
            on = False

        elif order == "report":
            # TODO: 1. print report of drink resources
            print(f"Water remaining: {resources["water"]} ml\n"
                  f"Milk remaining: {resources["milk"]} ml\n"
                  f"Coffee remaining: {resources["coffee"]} g\n"
                  f"Money: {resources["money"]}")
            continue

        elif order not in ['espresso', 'latte', 'cappuccino']:
            print("That wasn't a valid order. Please choose again.")
            continue
        else:
            # TODO: manage payment and subtract resources
            order_ingredients = MENU[order]["ingredients"]

            for ingredient in order_ingredients:
                if resources[ingredient] > order_ingredients[ingredient]:
                    # TODO: how will you pay
                    quarters = int(input("How many quarters will you be using to pay? \n"))
                    dimes = int(input("How many dimes will you be using to pay? \n"))
                    nickles = int(input("How many nickles will you be using to pay? \n"))
                    pennies = int(input("How many pennies will you be using to pay? \n"))

                    payment = float(pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25)

                    payment_cost = MENU[order]["cost"]

                    if payment >= payment_cost:
                        print(f"your {order} and change is ${round(payment - payment_cost, 2)}")
                        resources["money"] += payment_cost
                        make_drink(order_ingredients)
                        break

                    else:
                        print(f"that is not enough for your {order} here is your money back ${round(payment, 2)}")
                        break

                elif resources[ingredient] < order_ingredients[ingredient]:
                    print(f"Sorry there is not enough {ingredient} to make your order")
                    break

start()
