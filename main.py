from utils import *
from person import Person

def main():
    people = []  # List to store all Person objects

    while True:
        # Display menu
        print("Choose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        choice = input().strip()

        # Option 1: Add a new person
        if choice == "1":
            persona = person_data()
            people.append(persona)

        # Option 2: Add an account to an existing person
        elif choice == "2":
            nombre = input("Enter the person's name:")
            for persona in people:
                if persona.name == nombre:
                    cuenta = int(input("Enter a 4-digit account number:"))
                    balance = float(input("Enter the initial balance:"))
                    cuenta = BankAccount(cuenta, balance)
                    persona.add_account(cuenta)
                    break
            else: 
                print("Person not found.")

        # Option 3: Show all balances
        elif choice == "3":
            if len(people) == 0:
                print("No data to show.")
            else:
                balance_summary(people)

        # Option 4: Quit
        elif choice == "4":
            print("Goodbye!")
            break

        # Invalid input
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

