import customtkinter as Ctk
from customtkinter import CTkLabel, CTkEntry, CTkButton
from prodotto import Prodotto
from archivioProdotti import ArchivioProdotti

def aggiungi_prodotto():
    nome = Entry1.get()
    categoria = Entry2.get()
    prezzo = Entry3.get()
    quantita = Entry4.get()

    try:
        prodotto = Prodotto(nome, categoria, float(prezzo), int(quantita))
        archivio.aggiungi_prodotto(prodotto)
        aggiorna_lista()
    except Exception as e:
        print(f"Errore: {e}")

    Entry1.delete(0, "end")
    Entry2.delete(0, "end")
    Entry3.delete(0, "end")
    Entry4.delete(0, "end")


def aggiorna_lista():
    Lista_box.configure(state="normal")
    Lista_box.delete("1.0", "end")

    for p in archivio.get_prodotti():
        Lista_box.insert("end", f"{p}\n\n")

    Lista_box.configure(state="disabled")

def cancella_nome():
    nome = Entry5.get().capitalize()
    archivio.rimuovere_prodotto(nome)
    aggiorna_lista()
    Entry5.delete(0, "end")

def salva_json():
    testo_8.configure(text="")

    archivio.salva_json()

    testo_8.configure(text="Salvato")

def carica_json():
    testo_8.configure(text="")

    archivio.carica_json()
    aggiorna_lista()

    testo_8.configure(text="Caricato")





app = Ctk.CTk()
app.title("Registro Elettronico Offline")
app.geometry("1920x1080")
app.resizable(False, False)
archivio = ArchivioProdotti([])

### Frame sinistra
frame_sinistra = Ctk.CTkFrame(app, fg_color="transparent")
frame_sinistra.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
frame_destra = Ctk.CTkFrame(app, fg_color="transparent")
frame_destra.grid(row=0, column=1, sticky="nsew", padx=25, pady=25)

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=3)
app.grid_rowconfigure(0, weight=1)

### Input


riga_nome = Ctk.CTkFrame(frame_sinistra, fg_color="transparent")
riga_nome.pack(anchor="w", pady=30)

testo_1 = CTkLabel(riga_nome, text="Nome:", font=("Bahnschrift", 18))
testo_1.pack(side="left", padx=10)

Entry1 = CTkEntry(riga_nome, width=250)
Entry1.pack(side="left", padx=10)



riga_categoria = Ctk.CTkFrame(frame_sinistra, fg_color="transparent")
riga_categoria.pack(anchor="w", pady=30)

testo_2 = CTkLabel(riga_categoria, text="Categoria:", font=("Bahnschrift", 18))
testo_2.pack(side="left", padx=10)

Entry2 = CTkEntry(riga_categoria, width=250)
Entry2.pack(side="left", padx=10)



riga_prezzo = Ctk.CTkFrame(frame_sinistra, fg_color="transparent")
riga_prezzo.pack(anchor="w", pady=30)

testo_3 = CTkLabel(riga_prezzo, text="Prezzo:", font=("Bahnschrift", 18))
testo_3.pack(side="left", padx=10)

Entry3 = CTkEntry(riga_prezzo, width=250)
Entry3.pack(side="left", padx=10)



riga_quantita = Ctk.CTkFrame(frame_sinistra, fg_color="transparent")
riga_quantita.pack(anchor="w", pady=30)

testo_4 = CTkLabel(riga_quantita, text="Quantità:", font=("Bahnschrift", 18))
testo_4.pack(side="left", padx=10)

Entry4 = CTkEntry(riga_quantita, width=250)
Entry4.pack(side="left", padx=10)



button_1 = CTkButton(frame_sinistra, text="Aggiungi", command=aggiungi_prodotto, font=("Bahnschrift", 18))
button_1.pack(anchor="w", pady=30)



riga_cancella = Ctk.CTkFrame(frame_sinistra, fg_color="transparent")
riga_cancella.pack(anchor="w", pady=30)

testo_7 = CTkLabel(riga_cancella, text="Cancella per nome:", font=("Bahnschrift", 18))
testo_7.pack(side="left", padx=10)

Entry5 = CTkEntry(riga_cancella, width=250)
Entry5.pack(side="left", padx=10)

button_2 = CTkButton(riga_cancella, text="Cancella", font=("Bahnschrift", 18), command=cancella_nome)
button_2.pack(side="left", pady=10)

riga_json = Ctk.CTkFrame(frame_sinistra, fg_color="transparent")
riga_json.pack(anchor="w", pady=30)

button_3 = CTkButton(riga_json, text="Salva",font=("Bahnschrift", 18),command=salva_json)
button_3.pack(side="left", pady=30, padx=30)

button_4 = CTkButton(riga_json, text="Carica",font=("Bahnschrift", 18), command=carica_json)
button_4.pack(side="left", pady=30, padx=30)

testo_8 = CTkLabel(frame_sinistra, fg_color="transparent", text="", font=("Bahnschrift", 32))
testo_8.pack(anchor="nw", padx=10)




### Frame destra

testo_5 = CTkLabel(frame_destra, text="Lista Prodotti", font=("Bahnschrift", 32))
testo_5.pack(anchor="c", pady=5)

Lista_box = Ctk.CTkTextbox(frame_destra, height=400, border_color="black", pady=5)
Lista_box.pack(fill="x", anchor="n", pady=10)
Lista_box.configure(state="disabled")





app.mainloop()
