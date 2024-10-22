class Account():
    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.balance=0

accounts={}

def createAccount():
    user=input("Enter username: ")
    passW=input("Enter password: ")
    accounts[f"acc{len(accounts)+1}"]=Account(user, passW)
    print(f"\nacc{len(accounts)} created")

    homeScreen()

def login():
    loginisTrue=False
    user=input("Enter username: ")
    passW=input("Enter password: ")
    for i in accounts:
        if user == accounts[i].username:
            if passW == accounts[i].password:
                loginisTrue=True
                userScreen(i)
                break
    if loginisTrue is False:
        print("Incorrect Username or Password")
        homeScreen()

def homeScreen():
    print("**Select a service**")
    print("1. Create an Account")
    print("2. Login")
    choice=input("Enter your choice: ")

    match choice:
        case "1":
            createAccount()
        case "2":
            login()
        case _:
            print("Invalid choice")
            homeScreen()

def deposit(acc):
    amount=int(input("Enter amount to be deposited"))
    if amount>0:
        accounts[acc].balance+=amount
        print("Amount successfully deposited: ")
        userScreen(acc)
    else:
        print("Invalid amount")
        deposit(acc)

def withdraw(acc):
    amount=int(input("Enter amount to be withdrawn: "))
    if amount>0:
        accounts[acc].balance-=amount
        print("Amount successfully withdrawn")
        userScreen(acc)
    else:
        print("Invalid amount")
        withdraw(acc)

def userScreen(acc):
    print(f"\n**Hi {accounts[acc].username}**")
    print("Enter your choice: \n")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Log out")
    choice=input("Enter your choice: ")
    match choice:
        case "1":
            deposit(acc)
        case "2":
            withdraw(acc)
        case "3":
            print(f"\nBalance: {accounts[acc].balance}\n")
            userScreen(acc)
        case "4":
            print("\nYou have logged out\n")
            homeScreen()
        case _:
            print("Invalid choice")
            userScreen(acc)

homeScreen()