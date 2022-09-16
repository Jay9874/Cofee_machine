
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 12.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 7.5,
    },
    "chai": {
        "ingredients": {
            "water": 50,
            "milk": 100,
            "coffee": 15,
        },
        "cost": 5.0
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 15.0,
    }
}

resources = {
    "water": 350,
    "milk": 500,
    "coffee": 1000,
}


money_bank = 0


def collect_money(purchased_itm):
    given_money = 0
    print(f"Cost for {purchased_itm} is ₹{MENU[purchased_itm]['cost']}")
    print("Please enter coins..")
    print("Accepted coins of ₹5, ₹2, ₹1, ₹0.5\n")
    coin5 = int(input("How many coin of ₹5?: "))
    coin2 = int(input("How many coin of ₹2?: "))
    coin1 = int(input("How many coin  of ₹1?: "))
    coin_pt5 = int(input("How many coin of ₹0.5?: "))
    given_money += coin5*5 + coin1*1 + coin2*2 + coin_pt5*.5
    cup_price = MENU[purchased_itm]["cost"]
    extra_money = given_money - cup_price
    return extra_money


def update_resources(purchased_item):
    req_ingredient = MENU[purchased_item]["ingredients"]
    flag = False
    emp_list = []
    for item in req_ingredient:
        if resources[item] < req_ingredient[item]:
            return False
        else:
            flag = True
            emp_list.append(item)
    if flag:
        for item in emp_list:
            resources[item] -= req_ingredient[item]
        return True


def cooking(purchased_itm):
    enough_resource = update_resources(purchased_itm)
    if enough_resource:
        balance_money = collect_money(purchased_itm)
        if balance_money > 0:
            print("Please wait, Cooking...")
            time.sleep(5)
            print(f"Here is your cup of {purchased_itm} ☕️.\n")
            print(f"{purchased_itm} costs ₹{MENU[purchased_itm]['cost']}\nPlease collect Balance, ₹{balance_money}\n"
                  f"Enjoy Your {purchased_itm}:) \n")
            return MENU[purchased_itm]['cost']
        elif balance_money == 0:
            print("Please wait, Cooking...")
            time.sleep(5)
            print(f"Here is your cup of {purchased_itm} ☕️. Enjoy it :) \n")
            return MENU[purchased_itm]['cost']
        elif balance_money < 0:
            print(f"Sorry, given money isn't sufficient for purchasing {purchased_itm} :( , try other drinks.\n"
                  f"Your money got refunded :( \n")
            return -1
    else:
        print(f"Sorry, for inconvenience, not enough resource to brew {purchased_itm} !), try other drinks.\n")
        return -1


def summary():
    for res in resources:
        if res == 'coffee':
            print(f"{res}: {resources[res]} gm")
        else:
            print(f"{res}: {resources[res]} ml")
    print(f"Total money: ₹{money_bank}")


powerOn = True
while powerOn:
    User_choice = input("What would you like to drink?: (chai, latte, cappuccino, espresso): ").lower()
    if User_choice == "off":
        print("Thank you for using our service :)  Turning off...")
        time.sleep(5)
        powerOn = False
        exit(0)

    elif User_choice == "report":
        summary()

    elif User_choice == "chai" or User_choice == "latte" or User_choice == "cappuccino" or User_choice == "espresso":
        payment_of = cooking(User_choice)
        if not payment_of < 0:
            money_bank += payment_of
    else:
        print("Oops, seems like you selected wrong beverage, try again :(\n")
