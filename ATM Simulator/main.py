accounts = {}  

def main_menu():
    while True:
        print("\n--- Welcome to ATM ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thanks for coming!")
            break
        else:
            print("Invalid option, try again.")

def create_account():
    email = input("Enter email: ")
    if email in accounts:
        print("Account already exists! Try login.")
        return
    
    password = input("Enter password: ")
    accounts[email] = {"password": password, "balance": 0}
    print("Account created successfully!")

    proceed = input("Would you like to proceed? (yes/no): ").lower()
    if proceed == "yes":
        login()
    else:
        print("Thanks for coming!")

def login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email in accounts and accounts[email]["password"] == password:
        print(f"Welcome {email} to the ATM!")
        atm_menu(email)
    else:
        print("Invalid credentials or account doesn’t exist. Please create account first.")

def atm_menu(email):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            print(f"Your balance: {accounts[email]['balance']}")

        elif choice == "2":  
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    accounts[email]["balance"] += amount
                    print("Deposit successful!")
                else:
                    print("Enter a positive amount!")
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == "3":  
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount > 0:
                    if amount <= accounts[email]["balance"]:
                        accounts[email]["balance"] -= amount
                        print("Withdrawal successful!")
                    else:
                        print("Insufficient balance!")
                else:
                    print("Enter a positive amount!")
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == "4":
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid option, try again.")

# Run program
main_menu()
