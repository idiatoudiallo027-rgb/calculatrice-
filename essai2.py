import customtkinter as ctk

# Fenêtre principale
app = ctk.CTk()
app.geometry("300x350")
app.title("Ma calculatrice")

# =========================
# Frame affichage
# =========================
frameExpr = ctk.CTkFrame(app)
frameExpr.pack(pady=10)

lablExp = ctk.CTkLabel(frameExpr, text="", width=200, height=50)
lablExp.pack()

# =========================
# Frame boutons
# =========================
frameBtn = ctk.CTkFrame(app)
frameBtn.pack(pady=10)

# =========================
# Fonctions chiffres
# =========================
def cliquer_0():
    lablExp.configure(text=lablExp.cget("text") + "0")

def cliquer_1():
    lablExp.configure(text=lablExp.cget("text") + "1")

def cliquer_2():
    lablExp.configure(text=lablExp.cget("text") + "2")

def cliquer_3():
    lablExp.configure(text=lablExp.cget("text") + "3")

def cliquer_4():
    lablExp.configure(text=lablExp.cget("text") + "4")

def cliquer_5():
    lablExp.configure(text=lablExp.cget("text") + "5")

def cliquer_6():
    lablExp.configure(text=lablExp.cget("text") + "6")

def cliquer_7():
    lablExp.configure(text=lablExp.cget("text") + "7")

def cliquer_8():
    lablExp.configure(text=lablExp.cget("text") + "8")

def cliquer_9():
    lablExp.configure(text=lablExp.cget("text") + "9")

# =========================
# Fonctions opérateurs
# =========================
def cliquer_plus():
    lablExp.configure(text=lablExp.cget("text") + "+")

def cliquer_moins():
    lablExp.configure(text=lablExp.cget("text") + "-")

def cliquer_mult():
    lablExp.configure(text=lablExp.cget("text") + "*")

def cliquer_div():
    lablExp.configure(text=lablExp.cget("text") + "/")

# =========================
# Fonction égal
# =========================
def calculer():
    try:
        resultat = eval(lablExp.cget("text"))
        lablExp.configure(text=str(resultat))
    except:
        lablExp.configure(text="Erreur")

# =========================
# Fonction effacer
# =========================
def effacer():
    lablExp.configure(text="")

# =========================
# Boutons (grille 4x4)
# =========================

# Ligne 1
btn_1 = ctk.CTkButton(frameBtn, text="1", width=50, command=cliquer_1)
btn_1.grid(row=0, column=0, padx=5, pady=5)

btn_2 = ctk.CTkButton(frameBtn, text="2", width=50, command=cliquer_2)
btn_2.grid(row=0, column=1, padx=5, pady=5)

btn_3 = ctk.CTkButton(frameBtn, text="3", width=50, command=cliquer_3)
btn_3.grid(row=0, column=2, padx=5, pady=5)

btn_plus = ctk.CTkButton(frameBtn, text="+", width=50, command=cliquer_plus)
btn_plus.grid(row=0, column=3, padx=5, pady=5)

# Ligne 2
btn_4 = ctk.CTkButton(frameBtn, text="4", width=50, command=cliquer_4)
btn_4.grid(row=1, column=0, padx=5, pady=5)

btn_5 = ctk.CTkButton(frameBtn, text="5", width=50, command=cliquer_5)
btn_5.grid(row=1, column=1, padx=5, pady=5)

btn_6 = ctk.CTkButton(frameBtn, text="6", width=50, command=cliquer_6)
btn_6.grid(row=1, column=2, padx=5, pady=5)

btn_moins = ctk.CTkButton(frameBtn, text="-", width=50, command=cliquer_moins)
btn_moins.grid(row=1, column=3, padx=5, pady=5)

# Ligne 3
btn_7 = ctk.CTkButton(frameBtn, text="7", width=50, command=cliquer_7)
btn_7.grid(row=2, column=0, padx=5, pady=5)

btn_8 = ctk.CTkButton(frameBtn, text="8", width=50, command=cliquer_8)
btn_8.grid(row=2, column=1, padx=5, pady=5)

btn_9 = ctk.CTkButton(frameBtn, text="9", width=50, command=cliquer_9)
btn_9.grid(row=2, column=2, padx=5, pady=5)

btn_mult = ctk.CTkButton(frameBtn, text="*", width=50, command=cliquer_mult)
btn_mult.grid(row=2, column=3, padx=5, pady=5)

# Ligne 4
btn_0 = ctk.CTkButton(frameBtn, text="0", width=50, command=cliquer_0)
btn_0.grid(row=3, column=0, padx=5, pady=5)

btn_c = ctk.CTkButton(frameBtn, text="C", width=50, command=effacer)
btn_c.grid(row=3, column=1, padx=5, pady=5)

btn_egal = ctk.CTkButton(frameBtn, text="=", width=50, command=calculer)
btn_egal.grid(row=3, column=2, padx=5, pady=5)

btn_div = ctk.CTkButton(frameBtn, text="/", width=50, command=cliquer_div)
btn_div.grid(row=3, column=3, padx=5, pady=5)

# Lancer l'application
app.mainloop()