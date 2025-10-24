import tkinter as tk
from tkinter import messagebox

def addition(a, b): return a + b
def soustraction(a, b): return a - b
def multiplication(a, b): return a * b
def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

def calculer(operation):
    try:
        a = float(entree1.get())
        b = float(entree2.get())
        if operation == "addition":
            res = addition(a, b)
        elif operation == "soustraction":
            res = soustraction(a, b)
        elif operation == "multiplication":
            res = multiplication(a, b)
        elif operation == "division":
            res = division(a, b)
        label_resultat.config(text=f"Résultat : {res}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")

fenetre = tk.Tk()
fenetre.title("Calculatrice graphique")
fenetre.geometry("300x300")

entree1 = tk.Entry(fenetre)
entree2 = tk.Entry(fenetre)
entree1.pack(pady=5)
entree2.pack(pady=5)

tk.Button(fenetre, text="+", command=lambda: calculer("addition")).pack(pady=2)
tk.Button(fenetre, text="-", command=lambda: calculer("soustraction")).pack(pady=2)
tk.Button(fenetre, text="×", command=lambda: calculer("multiplication")).pack(pady=2)
tk.Button(fenetre, text="÷", command=lambda: calculer("division")).pack(pady=2)

label_resultat = tk.Label(fenetre, text="Résultat : ")
label_resultat.pack(pady=10)

fenetre.mainloop()
