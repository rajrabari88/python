accounts = {}

def create_account(account_number, balance, pin):
    if account_number in accounts:
        print("Account already exists")
        return False
    accounts[account_number] = {
        "balance": balance,
        "pin": pin
    }
    print("Account created successfully")
    return True

def view_customer(account_number):
    account = accounts.get(account_number)
    if account:
        print(f"Account Number: {account_number}")
        print(f"Balance: {account['balance']}")
        return True
    print("Account not found")
    return False

def search_customer(account_number):
    return view_customer(account_number)

def view_all_customers():
    if not accounts:
        print("No customers in the bank")
        return
    for account_number, details in accounts.items():
        print(f"Account Number: {account_number}, Balance: {details['balance']}")

def total_amount_in_bank():
    total = sum(account["balance"] for account in accounts.values())
    print(f"Total amount in the bank: {total}")

def login(account_number, pin):
    account = accounts.get(account_number)
    if account and account["pin"] == pin:
        return account
    return None

def deposit(account_number, pin, amount):
    account = login(account_number, pin)
    if account:
        account['balance'] += amount
        print("Deposit successful")
    else:
        print("Invalid account number or pin")

def withdraw(account_number, pin, amount):
    account = login(account_number, pin)
    if account:
        if account["balance"] >= amount:
            account["balance"] -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient funds")
    else:
        print("Invalid account number or pin")

def get_balance(account_number, pin):
    account = login(account_number, pin)
    if account:
        return account['balance']
    return None

def main():
    while True:
        print("Welcome to Python Bank Management System")
        print("1) Banker")
        print("2) Customer")
        print("3) Exit")

        choice = input("Choose your role (1/2/3): ")

        if choice == '1':
            print("Banker Menu")
            print("1) Create new account")
            print("2) View customer")
            print("3) Search customer")
            print("4) View all customers")
            print("5) Total amount in bank")
            print("6) Exit")

            banker_choice = input("Choose your action (1/2/3/4/5/6): ")

            if banker_choice == "1":
                account_number = int(input("Enter account number: "))
                balance = float(input("Enter initial balance: "))
                pin = int(input("Enter pin: "))
                create_account(account_number, balance, pin)

            elif banker_choice == "2":
                account_number = int(input("Enter account number: "))
                view_customer(account_number)

            elif banker_choice == "3":
                account_number = int(input("Enter account number: "))
                search_customer(account_number)

            elif banker_choice == "4":
                view_all_customers()

            elif banker_choice == "5":
                total_amount_in_bank()

            elif banker_choice == "6":
                continue

        elif choice == "2":
            print("Customer Menu")
            print("1) Login")
            print("2) Exit")

            customer_choice = input("Choose your action (1/2): ")

            if customer_choice == "1":
                account_number = int(input("Enter account number: "))
                pin = int(input("Enter pin: "))

                account = login(account_number, pin)

                if account:
                    print("Login successful")
                    while True:
                        print("1) Deposit")
                        print("2) Withdraw")
                        print("3) Get balance")
                        print("4) Exit")

                        customer_action = input("Choose your action (1/2/3/4): ")

                        if customer_action == "1":
                            amount = float(input("Enter amount to deposit: "))
                            deposit(account_number, pin, amount)
                        elif customer_action == "2":
                            amount = float(input("Enter amount to withdraw: "))
                            withdraw(account_number, pin, amount)
                        elif customer_action == "3":
                            balance = get_balance(account_number, pin)
                            if balance is not None:
                                print("Your balance is:", balance)
                        elif customer_action == "4":
                            break
                        else:
                            print("Invalid action")
                else:
                    print("Invalid account number or pin")

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
