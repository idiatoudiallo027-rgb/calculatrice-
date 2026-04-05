import customtkinter as ctk  # [cite: 49]

# --- CONFIGURATION DE L'APPLICATION ---
app = ctk.CTk()  # [cite: 49]
app.geometry("300x450")  # [cite: 50]
app.title('Ma calculatrice')  # [cite: 51]


# --- 1. LES FONCTIONS (LOGIQUE) ---

def cliquer_touche(valeur):
    """Ajoute le chiffre ou l'opérateur à l'affichage actuel."""
    actuel = lablExp.cget("text")
    # Si une erreur était affichée, on efface avant de recommencer
    if actuel == "Erreur" or actuel == "Div par 0":
        actuel = ""
    lablExp.configure(text=actuel + str(valeur))  # [cite: 57, 59]


def effacer():
    """Efface tout l'écran (Bouton Del)."""
    lablExp.configure(text="")


def calculer():
    """Évalue l'expression et affiche le résultat."""
    try:
        expression = lablExp.cget("text")
        # eval() calcule l'expression mathématique
        resultat = eval(expression)
        # On transforme en string pour permettre d'enchaîner d'autres calculs
        lablExp.configure(text=str(resultat))  #
    except ZeroDivisionError:
        lablExp.configure(text="Div par 0")
    except Exception:
        lablExp.configure(text="Erreur")


# --- 2. L'INTERFACE GRAPHIQUE (WIDGETS) ---

# Cadre pour l'affichage (Résultat) [cite: 8, 52]
frameExpr = ctk.CTkFrame(app)
frameExpr.pack(pady=20, padx=20, fill="x")  # [cite: 9, 53]

lablExp = ctk.CTkLabel(frameExpr, text="", font=("Arial", 24))  # [cite: 10, 54]
lablExp.pack(pady=10)

# Cadre pour les boutons [cite: 8, 55]
frameBtn = ctk.CTkFrame(app)
frameBtn.pack(pady=10, padx=10)  # [cite: 9, 55]

# --- 3. CRÉATION DES 16 BOUTONS DANS LA GRILLE ---

# Liste des boutons : (Texte, Ligne, Colonne)
touches = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('Del', 3, 0), ('0', 3, 1), ('=', 3, 2), ('/', 3, 3)
]

for (texte, ligne, col) in touches:
    if texte == "=":
        commande = calculer  # [cite: 60]
    elif texte == "Del":
        commande = effacer
    else:
        # Utilisation de lambda pour passer la valeur spécifique du bouton
        commande = lambda t=texte: cliquer_touche(t)

    # Création du bouton [cite: 62, 63]
    btn = ctk.CTkButton(frameBtn, text=texte, width=60, height=60, command=commande)
    # Placement dans la grille [cite: 11, 62]
    btn.grid(row=ligne, column=col, padx=5, pady=5)

# Lancement de la boucle principale [cite: 13, 64]
app.mainloop()