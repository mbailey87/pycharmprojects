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
        "water": 3000,
        "milk": 2000,
        "coffee": 1000,
        "money": 0
    }
    while on:
        order = input("Choose your coffee 'espresso', 'latte', or 'cappuccino':\n").lower()

        if order == "off":
            break

        elif order == "report":
            print(f"Water remaining: {resources['water']} ml\n"
                  f"Milk remaining: {resources['milk']} ml\n"
                  f"Coffee remaining: {resources['coffee']} g\n"
                  f"Money: ${resources['money']}")
            continue  # Go back to the start of the loop

        elif order not in MENU:
            print("That wasn't a valid order. Please choose again.")
            continue  # Re-prompt the user

        order_ingredients = MENU[order]["ingredients"]

        for ingredient in order_ingredients:
            if resources[ingredient] < order_ingredients[ingredient]:
                print(f"Sorry, there is not enough {ingredient} to make your order.")
                break
        else:  # Only execute if the for loop completes without breaking
            # Payment process
            pennies = int(input("How many pennies will you be using to pay? \n"))
            nickels = int(input("How many nickels will you be using to pay? \n"))
            dimes = int(input("How many dimes will you be using to pay? \n"))
            quarters = int(input("How many quarters will you be using to pay? \n"))

            payment = float(pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25)
            payment_cost = MENU[order]["cost"]

            if payment >= payment_cost:
                change = round(payment - payment_cost, 2)
                if change > 0:
                    print(f"Your change is ${change}")
                print("Thank you for your purchase!")

                resources["money"] += payment_cost
                for ingredient in order_ingredients:
                    resources[ingredient] -= order_ingredients[ingredient]

            else:
                print(f"That is not enough money. Here is your refund: ${payment}")

start()
