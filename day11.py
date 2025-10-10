import os
import json

DATA_FILE = "atm_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {"pin": "1001", "balance": 100000000000.0}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def atm():
    data = load_data()
    clear_screen()
    print(" Welcome to the ATM Simulator Mr.Nijan")

    pin = input("Enter your PIN: ")
    if pin != data['pin']:
        print(" Invalid PIN!")
        return

    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print(f"Your balance: ₹{data['balance']}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            data['balance'] += amount
            save_data(data)
            print("Amount deposited successfully")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= data['balance']:
                data['balance'] -= amount
                save_data(data)
                print(" Please collect your cash.")
            else:
                print(" Insufficient balance.")
        elif choice == '4':
            print("Thank you for using the ATM Mr.Nijan!")
            break
        else:
            print("Invalid option!")

        input("\nPress Enter to continue...")
        clear_screen()

atm()
