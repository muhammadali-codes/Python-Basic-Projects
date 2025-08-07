login = {

}

print("Enter your Email and Password to create your account")

class User:
    def creatingAccount(self, login):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.email = email
        self.password = password
        self.login = login
        login.update({email: password})
        print("✅ Your account is created.")

# Outside the class
login_data = {}               # Dictionary to hold all user accounts
user1 = User()                # Create an object
user1.creatingAccount(login_data)  # Call the method properly

login_data = {}
user2 = User()
user2.creatingAccount(login_data)

class LoginCredentials:
 def login(self, login_data):
        login_attempts = 3

        while True:
            while login_attempts > 0:
                email = input("Enter your email: ")
                password = input("Enter your password: ")

                print()  # Blank line for spacing

                if email in login_data and login_data[email] == password:
                    print(f"✅ Login successful! Welcome {email}\n")
                    exit()

                elif email not in login_data and password not in login_data.values():
                    print("😕 Oops! That didn’t work. Check your Email or Password.")

                elif email not in login_data:
                    print("❌ Incorrect Email!")

                elif password != login_data.get(email):
                    print("❌ Incorrect Password!")

                else:
                    print("⚠️ Something went wrong.")

                login_attempts -= 1
                print(f"🔁 Login Attempts left: {login_attempts}\n")

            # If attempts are 0
            print("🚫 Maximum login attempts reached.")
            tryagain = input("Try again (yes/no): ").lower()

            if tryagain == "no":
                print("👋 Exiting login. Goodbye!")
                exit()
            elif tryagain == "yes":
                login_attempts = 3  # reset attempts
            else:
                print("⚠️ Please type 'yes' or 'no'")


auth = LoginCredentials()
auth.login(login_data)


