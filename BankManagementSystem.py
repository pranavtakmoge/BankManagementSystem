import random

def generate_account_number():
    while True:
        account_number=str(random.randint(1000,9999))

        if account_number not in accounts:
            return account_number

accounts={}

def create_account():
    account_number=generate_account_number()

    if account_number in accounts:
        print("Account already exists")
        return

    name=input("Enter account holder name: ")
    pin=input("Create your 4-digit pin: ")
    balance=float(input("Enter initial deposit: "))

    if balance < 1000:
        print("Minimum initial deposit is ₹1,000")
        print("Failed creating account!")
        return

    if balance > 50000:
        print("Maximum account balance is ₹50,000")
        print("Failed creating account!")
        return
    accounts[account_number]={
        'name':name,
        'pin':pin,
        'balance':balance,
        'transactions':[f"Account created with balance ₹{balance:.2f}"]
    }

    print("Account created successfully")
    print("Your account number is: ",account_number)

# Loan Menu
def loan_menu(account_number):
    while True:
        print("\n========== LOAN SERVICES ==========")
        print("1. Gold Loan")
        print("2. Home Loan")
        print("3. Personal Loan")
        print("4. Education Loan")
        print("5. Vehicle Loan")
        print("6. Business Loan")
        print("7. Back")

        choice = int(input("Enter your choice: "))

        if choice == 7:
            break

        elif choice == 1:
            loan_type = "Gold Loan"
            interest = 9
            max_years = 5

        elif choice == 2:
            loan_type = "Home Loan"
            interest = 8.5
            max_years = 30

        elif choice == 3:
            loan_type = "Personal Loan"
            interest = 12
            max_years = 7

        elif choice == 4:
            loan_type = "Education Loan"
            interest = 7.5
            max_years = 15

        elif choice == 5:
            loan_type = "Vehicle Loan"
            interest = 9.5
            max_years = 7

        elif choice == 6:
            loan_type = "Business Loan"
            interest = 11
            max_years = 10

        else:
            print("Invalid choice")
            continue

        print("\n==========", loan_type, "==========")

        amount = float(input("Enter loan amount: "))
        years = int(input("Enter loan tenure in years: "))

        if amount <= 0:
            print("Invalid loan amount")
            continue

        if years <= 0 or years > max_years:
            print("Invalid loan tenure")
            print("Maximum tenure:", max_years, "years")
            continue

        # EMI calculation

        monthly_rate = interest / (12 * 100)
        months = years * 12

        emi = (amount*monthly_rate*(1+monthly_rate)**months) / ((1+monthly_rate)**months-1)

        total_payment = emi * months
        total_interest = total_payment - amount

        print("\n---------- LOAN DETAILS ----------")
        print("Loan Type      :", loan_type)
        print("Loan Amount    : ₹", amount)
        print("Interest Rate  :", interest, "%")
        print("Tenure         :", years, "years")
        print("Monthly EMI    : ₹", round(emi, 2))
        print("Total Interest : ₹", round(total_interest, 2))
        print("Total Payment  : ₹", round(total_payment, 2))

        confirm = input("\nApply for loan? (yes/no): ")

        if confirm.lower() == "yes":

            accounts[account_number]['transactions'].append(
                f"{loan_type} applied for ₹{amount}"
            )

            print("Loan applied successfully!")

        else:
            print("Loan application cancelled")

# Card Details
def card_menu(account_number):

    while True:
        print("\n========== CARD SERVICES ==========")
        print("1. Debit Card")
        print("2. Credit Card")
        print("3. Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\n========== DEBIT CARD ==========")
            if 'debit_card' not in accounts[account_number]:
                card_number = str(random.randint(1000000000000000, 9999999999999999))
                cvv = str(random.randint(100, 999))

                accounts[account_number]['debit_card'] = {
                    'card_number': card_number,
                    'cvv': cvv,
                    'status': 'Active'
                }

                print("Debit Card created successfully!")

            card = accounts[account_number]['debit_card']

            print("\nCard Number :", card['card_number'])
            print("CVV         :", card['cvv'])
            print("Status      :", card['status'])

        elif choice == 2:

            print("\n========== CREDIT CARD ==========")

            if 'credit_card' not in accounts[account_number]:

                card_number = str(random.randint(1000000000000000, 9999999999999999))
                cvv = str(random.randint(100, 999))

                accounts[account_number]['credit_card'] = {
                    'card_number': card_number,
                    'cvv': cvv,
                    'credit_limit': 50000,
                    'used_credit': 0,
                    'status': 'Active'
                }

                print("Credit Card created successfully!")

            card = accounts[account_number]['credit_card']

            print("\nCard Number  :", card['card_number'])
            print("CVV          :", card['cvv'])
            print("Credit Limit : ₹", card['credit_limit'])
            print("Used Credit  : ₹", card['used_credit'])
            print("Available    : ₹",
                  card['credit_limit'] - card['used_credit'])
            print("Status       :", card['status'])

        elif choice == 3:
            break

        else:
            print("Invalid choice")

def login():
    account_number=input("Enter your account number: ")
    pin=input("Enter your pin: ")

    if account_number not in accounts:
        print("Account does not exist")
        return

    if accounts[account_number]['pin']!=pin:
        print("Account not found")
        return

    print(f"Welcome {accounts[account_number]['name']}!")

    while True:
        print("\n--Account menu")
        print("1. check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction history")
        print("5. Loan services")
        print("6. Card services")
        print("7. Logout")

        choice=int(input("Enter your choice: "))

        if choice==1:
            print(f"Account balance:₹{accounts[account_number]['balance']:.2f}")

        elif choice==2:
            amount=float(input("Enter your amount: "))

            if amount<=0:
                print("Enter a valid amount")

            elif accounts[account_number]['balance']+amount>50000:
                print("can't deposit due to max limit")

            else:
                accounts[account_number]['balance']+=amount
                accounts[account_number]['transactions'].append(f"Deposited ₹{amount}")
                print("Money Deposited Successfully")


        elif choice==3:
            amount=float(input("Enter withdrawl amount: "))
            if amount<=0:
                print("Enter a valid amount")

            elif accounts[account_number]['balance']-amount<1000:
                print("Can't Withdraw due to min limit")

            else:
                accounts[account_number]['balance']-=amount
                accounts[account_number]['transactions'].append(f'Withdrawn ₹{amount}')
                print("Money Withdrawn Successfully")


        elif choice==4:
            print("--Transaction history--")

            for transaction in accounts[account_number]['transactions']:
                print(transaction)

        elif choice == 5:
            loan_menu(account_number)

        elif choice == 6:
            card_menu(account_number)

        elif choice == 7:
            print("Logged out successfully")
            break

        else:
            print("Invalid choice")

def main():
    while True:
        print("\n==============================")
        print("    BANK MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if choice==1:
            create_account()

        elif choice==2:
            login()

        elif choice==3:
            print("Thank you for using our service! We Hope you liked it ☺️!")
            break

        else:
            print("Invalid choice")

main()