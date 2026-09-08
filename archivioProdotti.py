from prodotto import Prodotto
import json
class ArchivioProdotti:
    def __init__(self,listaProdotti):
        if not listaProdotti:
            self.__listaProdotti = []
            return

        for p in listaProdotti:
            if not isinstance(p, Prodotto):
                raise TypeError("La lista deve contenere solo oggetti Prodotti")

        self.__listaProdotti = listaProdotti


    def aggiungi_prodotto(self,prodotto):
        if isinstance(prodotto,Prodotto):
            self.__listaProdotti.append(prodotto)
        else:
            raise TypeError("Non é un prodotto")

    def rimuovere_prodotto(self,nome):
        if not isinstance(nome,str):
            raise TypeError("Il nome deve essere una stringa")

        if self.__listaProdotti == []:
            raise ValueError("Nessun prodotto esiste ancora")

        for p in self.__listaProdotti:
            if p.get_nome() == nome:
                self.__listaProdotti.remove(p)
                return

        raise ValueError("Prodotto non trovato")

    def prezzo_max_tra_prodotti(self):
        prezzo_max = self.__listaProdotti[0].get_prezzo()

        for p in self.__listaProdotti:
            if p.get_prezzo() > prezzo_max:
                prezzo_max = p.get_prezzo()

        return prezzo_max

    def valore_magazzino(self):
        valore_magazzino_list =  [p.valore_totale() for p in self.__listaProdotti ]
        return sum(valore_magazzino_list)

    def salva_json(self):
        lista_prodotti = [p.to_dict() for p in self.__listaProdotti]

        with open('data/lista_prodotti.json', 'w') as json_file:
            json.dump(lista_prodotti, json_file, indent=4)

    def carica_json(self):
        with open('data/lista_prodotti.json', 'r') as json_file:
            lista_prodotti = json.load(json_file)

            for d in lista_prodotti:
                p = Prodotto(
                    d["nome"],
                    d["categoria"],
                    d["prezzo"],
                    d["quantity"]
                )
                self.__listaProdotti.append(p)

    def get_prodotti(self):
        return self.__listaProdotti


















