from bank_account import BankAccount
from person import Person

def person_data():
    nombre = input("Enter the person's name:")
    ncuenta = input("Enter a 4-digit account number:")
    saldoini = input("Enter the initial balance:")
    persona = Person(nombre)
    cuenta = BankAccount(ncuenta, saldoini)
    persona.add_account(cuenta)

    cuentas = input("Are you done adding accounts? (yes/no):")
    while cuentas != "yes":
        ncuenta = input("Enter a 4-digit account number:")
        saldoini = input("Enter the initial balance:")
        cuenta = BankAccount(ncuenta, saldoini)
        persona.add_account(cuenta)
        cuentas = input("Are you done adding accounts? (yes/no):")
    return persona

def balance_summary(person_list):
    for persona in person_list:
        total = 0
        for account in persona.accounts:
            total += account.balance
        print(f"{persona.name} : {total:.2f}")