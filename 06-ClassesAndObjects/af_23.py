class Kontakt ():

    def __init__(self,nazwa, email, telefon):
        self.nazwa = nazwa
        self.email = email
        self.telefon = telefon
    def __repr__(self):
        return f'Name: {self.nazwa} Email: {self.email} Telefon: {self.telefon}'

class ListaKontakt():
    
    arrOfKontakt = []
    @classmethod
    def add_kontakt(cls,kontakt):
        cls.arrOfKontakt.append(kontakt)
    @classmethod
    def show_kontakt_list(cls):
        return print(cls.arrOfKontakt)


k1 = Kontakt('Kowalski Jan', 'jank@onet.pl', '555234000')
ListaKontakt.add_kontakt(k1)
ListaKontakt.show_kontakt_list()
k2 = Kontakt('Borek Patrycja', 'bp@o2.pl', '232000199')
ListaKontakt.add_kontakt(k2)
ListaKontakt.show_kontakt_list()


