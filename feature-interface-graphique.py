import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Calculatrice graphique")
fenetre.geometry("300x300")

label = tk.Label(fenetre, text="Bienvenue dans la calculatrice graphique")
label.pack(pady=20)

fenetre.mainloop()
