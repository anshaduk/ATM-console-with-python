def create_pin():
    while True:
        print("******************************************")
        pin = input("Create a 4-digit PIN: ")
        print("******************************************")
        if pin.isdigit() and len(pin) == 4:
            print("******************************************")
            print("PIN successfully created!")
            print("******************************************")
            return pin
        print("*******************************************")
        print("Invalid PIN; enter exactly 4 digits.")
        print("*******************************************")

def login(pin):
    password_inputing_chances = 3
    while password_inputing_chances !=0:
        print("*********************************************")
        entered_pin = input("Enter your 4-digit PIN: ")
        print("*********************************************")
        if entered_pin == pin:
            print("Login successfull!")
            return True
        password_inputing_chances -=1
        print(f"{password_inputing_chances} attempts left")
    print("Account locked due to too many failed attempts.")
    return False

def show_user_balance(balance):
    print(f"Your balance is ${balance}")
