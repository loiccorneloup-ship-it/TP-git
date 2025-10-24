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

if __name__ == "__main__":
    print("Addition :", addition(2, 3))
    print("Soustraction :", soustraction(5, 2))
    print("Multiplication :", multiplication(3, 4))
    print("Division :", division(10, 2))

    #Exemple 