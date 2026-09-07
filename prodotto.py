class Prodotto:
    def __init__(self,nome,categoria,prezzo,quantity):
        self.set_nome(nome)
        self.set_categoria(categoria)
        self.set_prezzo(prezzo)
        self.set_quantity(quantity)

    def __str__(self):
        return f"Nome: {self.__nome}    Categoria: {self.__categoria}      Prezzo: {self.__prezzo}     Quantitá: {self._quantity}"

    def set_nome(self,nome):
        if isinstance(nome,str) and nome != "":
            self.__nome = nome.capitalize()
        else:
            raise TypeError("Nome non valido")

    def get_nome(self):
        return self.__nome

    def set_categoria(self,categoria):
        if isinstance(categoria,str) and categoria != "":
            self.__categoria = categoria.capitalize()
        else:
            raise TypeError("Categoria non valida")

    def set_prezzo(self,prezzo):
        if prezzo > 0:
            self.__prezzo = prezzo
        else:
            raise TypeError("Prezzo non valido")

    def get_prezzo(self):
        return self.__prezzo

    def set_quantity(self,quantity):
        if quantity > 0:
            self._quantity = quantity
        else:
            raise TypeError("Quantitá non valida")

    def valore_totale(self):
        return self.__prezzo*self._quantity

    def to_dict(self):
        return {
                "nome":self.__nome,
                "categoria":self.__categoria,
                "prezzo":self.__prezzo,
                "quantity":self._quantity
                }