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


# TODO 6. Function to check the type of coffee chose and money needed.
def coffee_price(choice_answer):
    return MENU[choice_answer]['cost']


# TODO 5. Check to get the details of the coffee the user chose.
def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True


# TODO 7. Function to Make coffee
def make_coffee(order_ingredient):
    for item in order_ingredient:
        resources[item] = resources[item] - order_ingredient[item]


# TODO 4. Function to calculate money input.
def money_input(quarters_input, dimes_input, nickles_input, pennies_input):
    money_sum = (quarters_input * 0.25) + (dimes_input * 0.1) + (nickles_input * 0.05) + (pennies_input * 0.01)
    return money_sum


money = 0

# TODO: 1. Ask the user to choose what they want.
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    # TODO: 2. print the report if report is called.
    elif choice == 'report':
        print(f" Water: {resources['water']} \n Milk: {resources['milk']} \n Coffee: {resources['coffee']} \n "
              f"Money: ${money}")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            # TODO: 3. Please insert coins
            print("Please insert coins.")
            quarters = float(input("how many quarters?: "))
            dimes = float(input("how many dimes?: "))
            nickles = float(input("how many nickles?: "))
            pennies = float(input("how many pennies?: "))
            coffee_cost = coffee_price(choice)
            user_money = money_input(quarters, dimes, nickles, pennies)
            if user_money >= coffee_cost:
                change = round(user_money - coffee_cost, 2)
                money += coffee_cost
                make_coffee(drink['ingredients'])
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.”")
    else:
        print("Drink doesn't exist. Please try again")