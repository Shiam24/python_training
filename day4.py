CORRECT_PIN = "2001"
MAX_ATTEMPTS = 3
attempts = 0
while attempts < MAX_ATTEMPTS:
    pin = input("Enter your 4-digit PIN: ")

    if pin == CORRECT_PIN:
        print("Access granted. Welcome to your account.")
        print("===welcome Shiam===")
        print("select your transaction")
        print("select your account type")
        print("===current or saving===")
        print("cash deposit or withdrawl")
        input("current or saving account:")
        input("Enter your amount:")
        input("Are you want to check balance:")
        input("Rs:50,000")
        print("Please take your card and money")
        print("Thank you have a nice day")
        break
    else:
        attempts += 1
        print(f"Invalid PIN. Attempts remaining: {MAX_ATTEMPTS - attempts}")

if attempts == MAX_ATTEMPTS:
    print("Too many incorrect attempts. Card blocked.")
