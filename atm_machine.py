import getpass # built-in package to enter input without echo
import os
import account

def create_user_accounts():
    """
     Function will create a user account dictionary,
     where, key = user account id,
            value = account object
    :return: user_dictionary : <class 'dict'>
    """
    user_dictionary = {user_id: account.Account(user_id) for user_id in range(1000, 10000)}

    return user_dictionary


def main():

    """
    Assumption:
    1. There will always be a valid user
    2. Inserting card is detected by integer value 1
    2. User PIN is unique and same as user id
    3. User is 4-digit long
    4. User only has one account type
    5. While depositing or withdrawing amount, if user does not confirm amount, then they have to start process again
    6. User can withdraw all the amount. I.e. at the given time user can have minimum of $0 in the account

    """
    user_accounts = create_user_accounts()

    # ATM Process
    while True:
        # Step 1: Wait for user to Insert Card. Since, we assume a valid user we skip validation step
        insert_card = getpass.getpass("")

        if insert_card == '1':
            os.system('cls')
            print("Welcome!\n")
            # Step 2 : Next, Ask user to enter 4-digit PIN.
            pin = int(getpass.getpass(f"Enter 4-digit PIN: "))

            # Step 3: check if pin is valid or not
            while not 1000 <= pin <= 9999:
                pin = int(getpass.getpass(f"Invalid PIN! Please re-enter: "))

            # Step 4: Start user account session
            while True:

                # Step 5: Get user account
                user_account = user_accounts[pin]

                # Step 6: Display action items for user
                print(f"Please select from following action: \n")
                print(f"1. Check Balance \t 2. Deposit Amount\n3. Withdraw Amount \t 4. Exit Session\n")

                # Step 7: Ask user to select from above action
                action = int(input(f"Select action: "))

                # Display Available Balance
                if action == 1:
                    print(f"\nCurrent balance: ${user_account.get_balance()} \n")
                    continue

                # Deposit amount
                if action == 2:
                    amount = int(input(f"\nEnter amount to be deposited: $"))

                    confirm = input(f"Is this correct amount (Y or N) ? ${amount} ")

                    while confirm.lower() not in "yn":
                        confirm = input(f"Please enter 'Y' or 'N': ")

                    if confirm.lower() == "y":
                        prev_balance = user_account.get_balance()
                        user_account.deposit(amount)

                        print(f"\nPrevious balance: ${prev_balance}")
                        print(f"Amount deposited: ${amount} ")
                        # print updated balance
                        print(f"Updated balance: ${user_account.get_balance()} \n")
                        continue
                    else:
                        # start process again
                        break

                # withdraw amount
                if action == 3:
                    prev_balance = user_account.get_balance()

                    if prev_balance == 0:
                        print(f"\nInsufficient balance ${prev_balance}!!! \n")
                        break

                    amount = int(input(f"\nEnter amount to be withdrawn [Note: Cannot withdraw more than ${prev_balance}]: \n"))

                    confirm = input(f"Is this correct amount (Y or N) ? ${amount} ")

                    while confirm.lower() not in "yn":
                        confirm = input(f"Please enter 'Y' or 'N': \n")

                    if confirm.lower() == "y":
                        user_account.withdraw(amount)

                        print(f"\nPrevious balance: ${prev_balance} ")
                        print(f"Amount deposited: ${amount} ")
                        # print updated balance
                        print(f"Updated balance: ${user_account.get_balance()} \n")
                        continue
                    else:
                        # start process again
                        break

                # Exit
                if action == 4:
                    print(f"\nThank you! Have a great day! \n")
                    break

        if insert_card == "q":
            # close the system
            break


if __name__ == "__main__":
    main()

