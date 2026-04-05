import customtkinter as ctk

app = ctk.CTk()
app.geometry("600x500")
app.title("Ma Calculatrice")

#creation des frames
frameExpr = ctk.CTkFrame(app,fg_color="white")
frameExpr.pack(pady=20)

lablExp = ctk.CTkLabel(frameExpr, text="", width=300, height=200, font=("Arial",26,"bold"))
lablExp.pack()

# Frame boutons
frameBtn = ctk.CTkFrame(app,fg_color="grey", width=500, height=400)
frameBtn.pack(pady=20)

# creation des Fonction
def cliquer_1():
    lablExp.configure(text=lablExp.cget("text") + "1")
def cliquer_2():
    lablExp.configure(text=lablExp.cget("text") + "2")
def cliquer_3():
    lablExp.configure(text=lablExp.cget("text") + "3")
def cliquer_addition():
    lablExp.configure(text=lablExp.cget("text") + "+")
def cliquer_4():
    lablExp.configure(text=lablExp.cget("text") + "4")
def cliquer_5():
    lablExp.configure(text=lablExp.cget("text") + "5")
def cliquer_6():
    lablExp.configure(text=lablExp.cget("text") + "6")
def cliquer_soustraction():
    lablExp.configure(text=lablExp.cget("text") + "-")
def cliquer_7():
    lablExp.configure(text=lablExp.cget("text") + "7")
def cliquer_8():
    lablExp.configure(text=lablExp.cget("text") + "8")
def cliquer_9():
    lablExp.configure(text=lablExp.cget("text") + "9")
def cliquer_multiplication():
    lablExp.configure(text=lablExp.cget("text") + "*")
def cliquer_suppresion():
    lablExp.configure(text="")
def cliquer_0():
    lablExp.configure(text=lablExp.cget("text") + "0")
def cliquer_egal():                         #tester les conditions et mise en place des execeptions
    try:
        expression=lablExp.cget("text")
        result=eval(expression)
        lablExp.configure(text=result)
    except ZeroDivisionError:
        lablExp.configure(text="erreur")
    except SyntaxError:
        lablExp.configure(text="erreur de syntax")

    #lablExp.configure(text=str(eval(lablExp.cget("text"))))
def cliquer_division():
    lablExp.configure(text=lablExp.cget("text") + "/")


# creation des Boutons
btn_1 = ctk.CTkButton(frameBtn, text="1", width=50, command=cliquer_1)
btn_1.grid(row=0, column=0, padx=5, pady=5)
btn_2 = ctk.CTkButton(frameBtn, text="2", width=50, command=cliquer_2)
btn_2.grid(row=0, column=1, padx=5, pady=5)
btn_3 = ctk.CTkButton(frameBtn, text="3", width=50, command=cliquer_3)
btn_3.grid(row=0, column=2, padx=5, pady=5)
btn_addition = ctk.CTkButton(frameBtn, text="+", width=50, command=cliquer_addition)
btn_addition.grid(row=0, column=3, padx=5, pady=5)
btn_4 = ctk.CTkButton(frameBtn, text="4", width=50, command=cliquer_4)
btn_4.grid(row=1, column=0, padx=5, pady=5)
btn_5 = ctk.CTkButton(frameBtn, text="5", width=50, command=cliquer_5)
btn_5.grid(row=1, column=1, padx=5, pady=5)
btn_6 = ctk.CTkButton(frameBtn, text="6", width=50, command=cliquer_6)
btn_6.grid(row=1, column=2, padx=5, pady=5)
btn_soustraction = ctk.CTkButton(frameBtn, text="-", width=50, command=cliquer_soustraction)
btn_soustraction.grid(row=1, column=3, padx=5, pady=5)
btn_7 = ctk.CTkButton(frameBtn, text="7", width=50, command=cliquer_7)
btn_7.grid(row=2, column=0, padx=5, pady=5)
btn_8 = ctk.CTkButton(frameBtn, text="8", width=50, command=cliquer_8)
btn_8.grid(row=2, column=1, padx=5, pady=5)
btn_9 = ctk.CTkButton(frameBtn, text="9", width=50, command=cliquer_9)
btn_9.grid(row=2, column=2, padx=5, pady=5)
btn_multiplication = ctk.CTkButton(frameBtn, text="*", width=50, command=cliquer_multiplication)
btn_multiplication.grid(row=2, column=3, padx=5, pady=5)
btn_suppression = ctk.CTkButton(frameBtn, text="del", width=50, command=cliquer_suppresion)
btn_suppression.grid(row=3, column=0, padx=5, pady=5)
btn_0 = ctk.CTkButton(frameBtn, text="0", width=50, command=cliquer_0)
btn_0.grid(row=3, column=1, padx=5, pady=5)
btn_egal = ctk.CTkButton(frameBtn, text="=", width=50, command=cliquer_egal)
btn_egal.grid(row=3, column=2, padx=5, pady=5)
btn_division = ctk.CTkButton(frameBtn, text="/", width=50, command=cliquer_division)
btn_division.grid(row=3, column=3, padx=5, pady=5)



app.mainloop()