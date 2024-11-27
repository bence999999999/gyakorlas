import tkinter as tk
from tkinter import messagebox
import plotly.graph_objects as go
from FB_szotar_kezelese import FB_szotar_kezelese


class SzotanuloApp:
    def __init__(self, root):
        self.szotar = FB_szotar_kezelese()
        self.helyes_valaszok = 0
        self.helytelen_valaszok = 0
        self.root = root
        self.root.title("App")

        self.kerdes_cimke = tk.Label(root, text="Mi az angol szó jelentése?", font=("Arial", 14))
        self.kerdes_cimke.pack(pady=20)

        self.valasz_entry = tk.Entry(root, font=("Arial", 12))
        self.valasz_entry.pack(pady=10)

        self.ellenoriz_gomb = tk.Button(root, text="Ellenőriz", command=self.ellenoriz)
        self.ellenoriz_gomb.pack(pady=10)

        self.eredmeny_label = tk.Label(root, text="", font=("Arial", 12))
        self.eredmeny_label.pack(pady=10)

        self.kovetkezo_gomb = tk.Button(root, text="Következő kérdés", command=self.kov_kerdes, state="disabled")
        self.kovetkezo_gomb.pack(pady=10)

        self.veglegesit_gomb = tk.Button(root, text="Eredmény megjelenítése", command=self.eredmeny)
        self.veglegesit_gomb.pack(pady=10)

        self.kov_kerdes()

    def kov_kerdes(self):
        result = self.szotar.FB_valasztas()
        if result:
            self.angol, self.magyar = result
            self.kerdes_cimke.config(text=f"Mi a(z) '{self.angol}' szó magyar megfelelője?")
            self.valasz_entry.delete(0, tk.END)
            self.eredmeny_label.config(text="")
            self.kovetkezo_gomb.config(state="disabled")
        else:
            self.kerdes_cimke.config(text="Nincsenek szavak az adatbázisban.")
            self.valasz_entry.config(state="disabled")
            self.ellenoriz_gomb.config(state="disabled")
            self.kovetkezo_gomb.config(state="disabled")

    def ellenoriz(self):
        user_answer = self.valasz_entry.get().strip().lower()
        if user_answer == self.magyar.lower():
            self.eredmeny_label.config(text="Helyes!", fg="green")
            self.helyes_valaszok += 1
        else:
            self.eredmeny_label.config(text=f"Helytelen! A helyes válasz: {self.magyar}", fg="red")
            self.helytelen_valaszok += 1
        self.kovetkezo_gomb.config(state="normal")

    def eredmeny(self):
        # Eredmények megjelenítése kördiagram formájában
        felirat = ['Helyes válaszok', 'Helytelen válaszok']
        ertekek = [self.helyes_valaszok, self.helytelen_valaszok]

        fig = go.Figure(data=[go.Pie(labels=felirat, values=ertekek, hole=0.3)])
        fig.update_traces(textinfo='percent+label', pull=[0.1, 0])
        fig.update_layout(title_text="Válaszok helyessége")

        fig.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = SzotanuloApp(root)
    root.mainloop()