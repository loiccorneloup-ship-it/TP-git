# calculatrice.py

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

def menu():
    print("\n=== Calculatrice ===")
    print("1 - Addition")
    print("2 - Soustraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Quitter")
    return input("Choisissez une opération : ")

if __name__ == "__main__":
    print("Addition :", addition(2, 3))
    print("Soustraction :", soustraction(5, 2))
    print("Multiplication :", multiplication(3, 4))
    print("Division :", division(10, 2))

    #Exemple 
    while True:
        choix = menu()

        if choix == "5":
            print("Au revoir 👋")
            break

        try:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Entrée invalide. Recommencez.")
            continue

        if choix == "1":
            print("Résultat :", addition(a, b))
        elif choix == "2":
            print("Résultat :", soustraction(a, b))
        elif choix == "3":
            print("Résultat :", multiplication(a, b))
        elif choix == "4":
            print("Résultat :", division(a, b))
        else:
            print("Choix invalide.")

####

#encore rien