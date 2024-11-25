# Funkcija za zbrajanje dva broja i zaokruživanje rezultata
def add(a, b):
    return round(a + b)

# Funkcija za oduzimanje dva broja i zaokruživanje rezultata
def subtract(a, b):
    return round(a - b)

# Funkcija za množenje dva broja i zaokruživanje rezultata
def multiply(a, b):
    return round(a * b)

# Funkcija za dijeljenje dva broja i zaokruživanje rezultata
# Uključuje provjeru dijeljenja s nulom
def divide(a, b):
    if b != 0:
        return round(a / b)
    else:
        return "Error: Division by zero!"

# Glavna funkcija kalkulatora koja upravlja korisničkim sučeljem
def calculator():
    # Ispis početne poruke i dostupnih operacija
    print("Welcome to the calculator!")
    print("Choose an operation:")
    print("1: Addition")
    print("2: Subtraktion")
    print("3: Multiplikation")
    print("4: Division")
    print("5: Beenden")

    # Beskonačna petlja za kontinuirani rad kalkulatora
    while True:
        # Korisnički unos željene operacije
        choice = input("Enter the number of the operation: ")

        # Provjera za izlaz iz programa
        if choice == '5':
            print("Calculator is finished. Goodbye!")
            break

        # Provjera valjanosti odabrane operacije
        if choice in ['1', '2', '3', '4']:
            try:
                # Unos brojeva s provjerom ispravnosti unosa
                num1 = float(input("Enter the first number:"))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                # Rukovanje neispravnim unosom
                print("Error: Please enter a valid number.")
                continue

            # Izvršavanje odabrane matematičke operacije
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        else:
            # Poruka o neispravnom unosu operacije
            print("Ungültige Eingabe. Bitte wähle eine Nummer von 1 bis 5.")

# Pokretanje kalkulatora
calculator()
