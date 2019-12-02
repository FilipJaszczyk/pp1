class Uniersity:
    def __init__(self,name,fullname):
        self.name = name
        self.fullname = fullname

    def print_name(self):
        print("Skrót: {}".format(self.name))
    def print_fullname(self):
        print("Pełna nazwa: {}".format(self.fullname))

    def set_fullname(self,new_fullname):
        self.fullname = new_fullname    
    def set_name(self,new_name):
        self.name = new_name

Uczelnia = Uniersity("Uek","Uniwersytet Ekonomiczny w Krakowie")

Uczelnia.print_name()
Uczelnia.print_fullname()

Uczelnia.set_name("AGH")
Uczelnia.set_fullname("Akademia Góniczo Huntnicza")

Uczelnia.print_name()
Uczelnia.print_fullname()