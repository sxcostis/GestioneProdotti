import customtkinter as ctk
from archivioProdotti import ArchivioProdotti
from prodotto import Prodotto

###In caso il prodotto é stato creato va scritto che é stato creato, se invece i valori sono stati inseriti male allora
###va detto che il prodotto non é stato creato.

###In caso il prodotto é stato cancellato va detto e se non é stato cancellato per problemi va scritto perché

def mostra_messaggio_temporaneo(testo_label, messaggio):
    testo_label.configure(text=messaggio)
    app.after(1000, lambda: testo_label.configure(text=""))

def aggiorna_lista():
    Lista_box.configure(state="normal")
    Lista_box.delete("1.0", "end")

    for p in archivio.get_prodotti():
        Lista_box.insert("end", f"{p}\n\n")

    Lista_box.configure(state="disabled")


def salva_json():
    archivio.salva_json()

    testo_messaggio = ctk.CTkLabel(
        frame_sinistra,
        text="",
        font=("Bahnschrift", 20, "bold"),
        state="disabled"
    )
    testo_messaggio.grid(
        row=5,
        column=0,
        pady=20
    )
    mostra_messaggio_temporaneo(testo_messaggio, "Salvataggio Eseguito")



def carica_json():
    archivio.carica_json()
    aggiorna_lista()

    testo_messaggio = ctk.CTkLabel(
        frame_sinistra,
        text="",
        font=("Bahnschrift", 20, "bold"),
        state="disabled"
    )
    testo_messaggio.grid(
        row=5,
        column=0,
        pady=20
    )
    mostra_messaggio_temporaneo(testo_messaggio, "Caricamento Eseguito")

def vai_ad_info_magazino():
    but_carica.grid_remove()
    but_salva.grid_remove()
    but_rimuovi_prodotto.grid_remove()
    but_info_magazzino.grid_remove()
    but_aggiungi_prodotti.grid_remove()


    def info_magazzino_torna_indietro():
        but_carica.grid()
        but_salva.grid()
        but_rimuovi_prodotto.grid()
        but_info_magazzino.grid()
        but_aggiungi_prodotti.grid()

        text_prezzo_max.grid_remove()
        text_valore_magazino.grid_remove()
        but_info_torna_indietro.grid_remove()

        testo.configure(text="Gestione Prodotti")

#Testi
    testo.configure(text="Info Magazino")

    text_prezzo_max = ctk.CTkLabel(
        frame_sinistra,
        text=f"Prodotto piú costoso: {archivio.prezzo_max_tra_prodotti()}",
        font=("Bahnschrift", 20, "bold")
    )
    text_prezzo_max.grid(
        row=1,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"
    )

    text_valore_magazino = ctk.CTkLabel(
        frame_sinistra,
        text=f"Valore Magazzino: {archivio.valore_magazzino()}",
        font=("Bahnschrift", 20, "bold")
    )
    text_valore_magazino.grid(
        row=2,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"
    )
#Bottini
    but_info_torna_indietro = ctk.CTkButton(
        frame_sinistra,
        text="Torna Indietro",
        font=("Bahnschrift", 24, "bold"),
        width=200,
        height=75,
        command=info_magazzino_torna_indietro
    )
    but_info_torna_indietro.grid(
        row=3,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"
    )


def vai_ad_rimuovi_prodotto():
    but_carica.grid_remove()
    but_salva.grid_remove()
    but_rimuovi_prodotto.grid_remove()
    but_info_magazzino.grid_remove()
    but_aggiungi_prodotti.grid_remove()

    def rimuovi_prodotto():
        nome = entry_rimuovi_prodotto.get().strip().capitalize()

        if nome != "":
            try:
                archivio.rimuovere_prodotto(nome)
            except ValueError as e:
                print(e)

        entry_rimuovi_prodotto.delete(0, "end")
        aggiorna_lista()

    def rimuovi_torna_indietro():
        but_carica.grid()
        but_salva.grid()
        but_rimuovi_prodotto.grid()
        but_info_magazzino.grid()
        but_aggiungi_prodotti.grid()

        text_rimuovi_prodotto.grid_remove()
        entry_rimuovi_prodotto.grid_remove()
        but_rimuovi_prodotto_esistente.grid_remove()
        but_rimuovi_torna_indietro.grid_remove()

        testo.configure(text="Gestione Prodotti")


#Testi
    testo.configure(text="Rimuovi Prodotto")

    text_rimuovi_prodotto = ctk.CTkLabel(
        frame_sinistra,
        text="Inserisci Nome",
        font=("Bahnschrift", 20, "bold")
    )
    text_rimuovi_prodotto.grid(
        row=1,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"
    )

#Entry
    entry_rimuovi_prodotto = ctk.CTkEntry(
        frame_sinistra,
        width=175,
        height=38,
        border_color="black"
    )
    entry_rimuovi_prodotto.grid(
        row=1
    )

#Bottoni
    but_rimuovi_prodotto_esistente = ctk.CTkButton(
        frame_sinistra,
        text="Rimuovi",
        font=("Bahnschrift", 24, "bold"),
        width=200,
        height=75,
        command=rimuovi_prodotto
    )
    but_rimuovi_prodotto_esistente.grid(
        row=2,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"
    )

    but_rimuovi_torna_indietro = ctk.CTkButton(
        frame_sinistra,
        text="Torna Indietro",
        font=("Bahnschrift", 24, "bold"),
        width=200,
        height=75,
         command=rimuovi_torna_indietro
    )
    but_rimuovi_torna_indietro.grid(
        row=3,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"
    )


def vai_ad_aggiungi():
    but_carica.grid_remove()
    but_salva.grid_remove()
    but_rimuovi_prodotto.grid_remove()
    but_info_magazzino.grid_remove()
    but_aggiungi_prodotti.grid_remove()

    def aggiungi_prodotto():
        nome = entry_aggiungi.get().strip().capitalize()
        categoria = entry_aggiungi2.get().strip().capitalize()
        prezzo = entry_aggiungi3.get()
        quantita = entry_aggiungi4.get()

        try:
            prezzo = float(prezzo)
            quantita = int(quantita)
            prodotto = Prodotto(nome, categoria, prezzo, quantita)
            archivio.aggiungi_prodotto(prodotto)
        except ValueError as e:
            print(e)

        entry_aggiungi.delete(0, "end")
        entry_aggiungi2.delete(0, "end")
        entry_aggiungi3.delete(0, "end")
        entry_aggiungi4.delete(0, "end")
        aggiorna_lista()

    def torna_indietro():
        but_carica.grid()
        but_salva.grid()
        but_rimuovi_prodotto.grid()
        but_info_magazzino.grid()
        but_aggiungi_prodotti.grid()


        entry_aggiungi.grid_remove()
        entry_aggiungi2.grid_remove()
        entry_aggiungi3.grid_remove()
        entry_aggiungi4.grid_remove()

        text_aggiungi.grid_remove()
        text_aggiungi2.grid_remove()
        text_aggiungi3.grid_remove()
        text_aggiungi4.grid_remove()

        but_menu_aggiungi.grid_remove()
        but_aggiungi.grid_remove()

        testo.configure(text="Gestione Prodotti")


#Testi
    testo.configure(text="Aggiungi Prodotto")

    text_aggiungi = ctk.CTkLabel(
        frame_sinistra,
        text="Inserisci Nome",
        font=("Bahnschrift", 20, "bold")
    )
    text_aggiungi.grid(
        row=1,
        column=0,
        pady=20,
        padx=(50,0),
        sticky="w"

    )

    text_aggiungi2 = ctk.CTkLabel(
        frame_sinistra,
        text="Inserisci Categoria",
        font=("Bahnschrift", 20, "bold")
    )
    text_aggiungi2.grid(
        row=2,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"

    )

    text_aggiungi3 = ctk.CTkLabel(
        frame_sinistra,
        text="Inserisci Prezzo",
        font=("Bahnschrift", 20, "bold")
    )
    text_aggiungi3.grid(
        row=3,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"

    )

    text_aggiungi4 = ctk.CTkLabel(
        frame_sinistra,
        text="Inserisci Quantitá",
        font=("Bahnschrift", 20, "bold")
    )
    text_aggiungi4.grid(
        row=4,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"

    )


#Entry
    entry_aggiungi = ctk.CTkEntry(
        frame_sinistra,
        width=175,
        height=38,
        border_color="black"
    )
    entry_aggiungi.grid(
        row=1,
        column=0,
        pady=20,
        padx=(50, 0),
    )

    entry_aggiungi2 = ctk.CTkEntry(
        frame_sinistra,
        width=175,
        height=38,
        border_color="black"
    )
    entry_aggiungi2.grid(
        row=2,
        column=0,
        pady=20,
        padx=(50, 0),
    )

    entry_aggiungi3 = ctk.CTkEntry(
        frame_sinistra,
        width=175,
        height=38,
        border_color="black"
    )
    entry_aggiungi3.grid(
        row=3,
        column=0,
        pady=20,
        padx=(50, 0),
    )

    entry_aggiungi4 = ctk.CTkEntry(
        frame_sinistra,
        width=175,
        height=38,
        border_color="black"
    )
    entry_aggiungi4.grid(
        row=4,
        column=0,
        pady=20,
        padx=(50, 0),
    )


#Bottoni
    but_aggiungi = ctk.CTkButton(
        frame_sinistra,
        text="Aggiungi",
        font=("Bahnschrift", 24, "bold"),
        width=200,
        height=75,
        command=aggiungi_prodotto
    )
    but_aggiungi.grid(
        row=5,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"
    )

    but_menu_aggiungi = ctk.CTkButton(
        frame_sinistra,
        text="Torna Indietro",
        font=("Bahnschrift", 24, "bold"),
        width=200,
        height=75,
        command=torna_indietro
    )
    but_menu_aggiungi.grid(
        row=6,
        column=0,
        pady=20,
        padx=(50, 0),
        sticky="w"
    )


#Creazione App
app = ctk.CTk()
app.geometry("1280x920")
app.resizable(False, False)
app.title("Gestione Prodotti Offline")

#Archivio
archivio = ArchivioProdotti([])

#Griglia principale
app.grid_columnconfigure(0, weight=0, minsize=640)
app.grid_columnconfigure(1, weight=0, minsize=640)
app.grid_rowconfigure(0, weight=0, minsize=920)

#Frame
frame_sinistra = ctk.CTkFrame(app, corner_radius=0, fg_color="#FFFFFF")
frame_sinistra.grid(row=0, column=0, sticky="nsew")
frame_destra = ctk.CTkFrame(app, corner_radius=0, fg_color="#E6E6E6")
frame_destra.grid(row=0, column=1, sticky="nsew")

#Frame sinistro
frame_sinistra.grid_columnconfigure(0, weight=0, minsize=640)
#Titolo
frame_sinistra.grid_rowconfigure(0, weight=0, minsize=150)
#Righe successive
for i in range(1, 8):
    frame_sinistra.grid_rowconfigure(i, weight=0, minsize=100)

#Titolo
testo = ctk.CTkLabel(
    frame_sinistra,
    text="Gestione Prodotti",
    font=("Bahnschrift", 42, "bold")
)
testo.grid(
    row=0,
    column=0,
    pady=20,
    sticky="n"
)

#Bottoni principali
but_aggiungi_prodotti = ctk.CTkButton(
    frame_sinistra,
    text="Aggiungi prodotto",
    height=80,
    corner_radius=10,
    font=("Bahnschrift", 24, "bold"),
    command=vai_ad_aggiungi
)
but_aggiungi_prodotti.grid(
    row=1,
    column=0,
    padx=80,
    pady=10,
    sticky="ew"
)

but_rimuovi_prodotto = ctk.CTkButton(
    frame_sinistra,
    text="Rimuovi Prodotto",
    height=80,
    corner_radius=10,
    font=("Bahnschrift", 24, "bold"),
    command=vai_ad_rimuovi_prodotto
)
but_rimuovi_prodotto.grid(
    row=2,
    column=0,
    padx=80,
    pady=10,
    sticky="ew",
)

but_info_magazzino = ctk.CTkButton(
    frame_sinistra,
    text="Info Sul Magazzino",
    height=80,
    corner_radius=10,
    font=("Bahnschrift", 24, "bold"),
    command=vai_ad_info_magazino
)
but_info_magazzino.grid(
    row=3,
    column=0,
    padx=80,
    pady=10,
    sticky="ew"
)

#Frame interno per bottoni
frame_sinistra_interno = ctk.CTkFrame(frame_sinistra, corner_radius=0, fg_color="#FFFFFF")
frame_sinistra_interno.grid(row=4, column=0, pady=40, sticky="ew")

frame_sinistra_interno.grid_columnconfigure(0, weight=0, minsize=300)
frame_sinistra_interno.grid_columnconfigure(1, weight=0, minsize=300)

but_salva = ctk.CTkButton(
    frame_sinistra_interno,
    text="Salva",
    height=60,
    corner_radius=10,
    font=("Bahnschrift", 20, "bold"),
    fg_color="#D9D9D9",
    text_color="black",
    command=salva_json
)
but_salva.grid(
    row=0,
    column=0,
    padx=(40, 20),
    pady=10,
    sticky="ew"
)

but_carica = ctk.CTkButton(
    frame_sinistra_interno,
    text="Carica",
    height=60,
    corner_radius=10,
    font=("Bahnschrift", 20, "bold"),
    fg_color="#D9D9D9",
    text_color="black",
    command=carica_json
)
but_carica.grid(
    row=0,
    column=1,
    padx=(20, 40),
    pady=10,
    sticky="ew"
)

#Frame destra textbox
Lista_box = ctk.CTkTextbox(
    frame_destra,
    width=600,
    height=800,
    border_width=4,
    corner_radius=10,
    font=("Bahnschrift", 18)
)
Lista_box.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20)

Lista_box.configure(state="disabled")


app.mainloop()
