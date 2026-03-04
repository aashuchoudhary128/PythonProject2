balance = 0.0
def display_balance():
    print("Current Balance:", balance)
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Amount deposited successfully.")
    else:
        print("Invalid amount.")
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Amount withdrawn successfully.")
while True:
    print("\n----- BANK MENU -----")
    print("1)Display Balance")
    print("2)Deposit Amount")
    print("3)Withdraw Amount")
    print("4)Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        display_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using the Bank Program.")
        break
    else:
        print("Invalid choice. Please try again.")