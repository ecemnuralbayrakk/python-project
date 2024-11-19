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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def result_resources(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def enaugh_money(order, sum):
    if sum < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if is_resource_sufficient(MENU[order]["ingredients"]):
            print(f"Here is ${sum - MENU[order]['cost']} in change.")
            print(f"Here is your {order} ☕️. Enjoy!")
            result_resources(MENU[order]["ingredients"])

        else:
            print("Sorry there is not enough resources.")


def money_order():
    print("Please insert coins.")
    quarters_custom = int(input("how many quarters?: "))
    dimes_custom = int(input("how many dimes?: "))
    nickles_custom = int(input("how many nickles?: "))
    pennies_custom = int(input("how many pennies?: "))
    sum_custom = (
        quarters_custom * quarters
        + dimes_custom * dimes
        + nickles_custom * nickles
        + pennies_custom * pennies
    )
    return sum_custom


def result():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


def order():
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "report":
        result()
    else:
        sum = money_order()
        enaugh_money(order, sum)


while True:
    order()
