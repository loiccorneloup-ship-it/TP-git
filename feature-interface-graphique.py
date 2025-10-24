import tkinter as tk
from tkinter import messagebox

def addition(a, b): return a + b
def soustraction(a, b): return a - b
def multiplication(a, b): return a * b
def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

def calculer(op):
    try:
        a = float(entree1.get())
        b = float(entree2.get())
        if op == "+": res = addition(a, b)
        elif op == "-": res = soustraction(a, b)
        elif op == "*": res = multiplication(a, b)
        elif op == "/": res = division(a, b)
        label_resultat.config(text=f"Résultat : {res}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")

fenetre = tk.Tk()
fenetre.title("Calculatrice graphique")
fenetre.geometry("320x240")
fenetre.resizable(False, False)

frame = tk.Frame(fenetre, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Nombre 1").grid(row=0, column=0)
entree1 = tk.Entry(frame)
entree1.grid(row=0, column=1)

tk.Label(frame, text="Nombre 2").grid(row=1, column=0)
entree2 = tk.Entry(frame)
entree2.grid(row=1, column=1)

tk.Button(frame, text="+", width=5, command=lambda: calculer("+")).grid(row=2, column=0, pady=5)
tk.Button(frame, text="-", width=5, command=lambda: calculer("-")).grid(row=2, column=1, pady=5)
tk.Button(frame, text="*", width=5, command=lambda: calculer("*")).grid(row=3, column=0, pady=5)
tk.Button(frame, text="/", width=5, command=lambda: calculer("/")).grid(row=3, column=1, pady=5)

label_resultat = tk.Label(fenetre, text="Résultat : ")
label_resultat.pack(pady=8)

fenetre.mainloop()
