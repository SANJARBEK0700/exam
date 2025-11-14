import json
import os
import re
users = {
    "4242 3800 5455 7788":{
        "name": "Sanjarbek",
        "lastname": "Turgunboev",
        "card_number": "4242 3800 5455 7788",
        "PIN": "0700",
        "balance": 3000,
        "number": "+998332005676"
    },
    "5454 6500 3739 2639":{
        "name": "Jahongir",
        "lastname": "Qurbonov",
        "card_number": "5454 6500 3739 2639",
        "PIN": "0209",
        "balance": 10000,
        "number": "+998331420209"
    }
}


if not os.path.exists("bank_database.json"):
    with open("bank_database.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def add_card(d:dict):
    name = input("Enter Your name: ")
    lastname = input("Enter Your Last name: ")
    card_number = input("Enter card number: ")
    PIN = input("Enter PIN: ")
    user = {
        card_number:{
            "name": name,
            "lastname": lastname,
            "card_number": card_number,
            "PIN": PIN,
            "balance": 6700

        }
    }
    def add_database(new_user: dict):
        try:
            with open('bank_database.json', 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        data.update(new_user)
        with open('bank_database.json', 'w') as f:
            json.dump(data, f, indent=4)
    print("Card successfully added")
    add_database(user)
    d.update(user)
    bankomat_manager(users)


def view_balance(d:dict):
    try:
        with open('bank_database.json', 'r', encoding='utf-8') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No bankomat database")
        return

    card_number = input("Enter card number: ").strip()
    PIN = input("Enter PIN: ").strip()

    if card_number in users:
        if users[card_number]['PIN'] == PIN:
            balance = users[card_number]['balance']
            print(f"Your balance is: {balance} zlots")
        else:
            print("Incorrect PIN")
    else:("Incorrect card number")

    bankomat_manager(d)



def add_funds(d:dict):
    card_number = input("Enter card number: ")
    PIN = input("Enter PIN: ")
    with open('bank_database.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    if card_number in data:
        if data[card_number]['PIN'] == PIN:
            valus = input("How much money you want to add: ")
            new_valus = float(valus) + float(data[card_number]['balance'])
            data[card_number]['balance'] = new_valus
            with open('bank_database.json', 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Your new balance is {new_valus}")
            d.update(d)
    bankomat_manager(d)


def withdrawal(d:dict):
    card_number = input("Enter card number: ")
    PIN = input("Enter PIN: ")
    with open('bank_database.json', 'r') as f:
        data = json.load(f)
    if card_number in data:
        if data[card_number]['PIN'] == PIN:
            amount = int(input("Enter amount to withdraw: "))
            if amount < data[card_number]['balance']:
                new_amount = data[card_number]['balance'] - amount
                data[card_number]['balance'] = new_amount
                with open('bank_database.json', 'w') as f:
                    json.dump(data, f, indent=4)
                print(f"Your new balance is {new_amount}")
            else:
                print("You don't have enough money")



def connect_sms(d:dict):
    card_number = input("Enter card number: ")
    PIN = input("Enter PIN: ")
    with open('bank_database.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
    if card_number in data:
        if data[card_number]['PIN'] == PIN:
            men = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
            sms = input("Enter sms number: ")
            if re.match(men, sms):
                data[card_number]['number'] = sms
                with open('bank_database.json', 'w', encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                print("SMS number successfully added")
            else:
                print("Incorrect phone number")
        else:
            print("Incorrect PIN")
    else:
        print("Incorrect card number")
    bankomat_manager(d)



def disconnect_sms(d:dict):
    card_number = input("Enter card number: ")
    PIN = input("Enter PIN: ")
    with open('bank_database.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
    if card_number in data:
        if data[card_number]['PIN'] == PIN:
            data[card_number]['number'] = ""
            with open('bank_database.json', 'w', encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        else:
            print("Incorrect PIN")
    else:
        print("Incorrect card number")

    bankomat_manager(d)


def bankomat_manager(d:dict):
    while True:
        kod = input("1. Cash deposit\n2. Cahs Withdraw\n3. Balance\n4. Connecting SMS service\n5. Disconnecting SMS service\n6. Adding new card\n 7. Exit")
        if kod == "1":
            add_funds(d)
        elif kod == "2":
            withdrawal(d)
        elif kod == "3":
            view_balance(d)
        elif kod == "4":
            connect_sms(d)
        elif kod == "5":
            disconnect_sms(d)
        elif kod == "6":
            add_card(d)
        elif kod == "7":
            break

bankomat_manager(users)