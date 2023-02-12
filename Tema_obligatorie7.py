# 2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
# împreună).
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’
# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)
# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creeazăun obiect de tip Cerc și joacă-te cu metodele lui

from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplemented

    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, valoare):
        self.latura = valoare

    @latura.deleter
    def latura(self):
        del self.__latura

    def aria(self):
        return self.__latura * self.__latura

    def descrie(self):
        print('Cel mai probabil am colturi')


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(selfself, valoare):
        self.__raza = valoare

    @raza.deleter
    def raza(self):
        del self.__raza

    def aria(self):
        return self.__raza * self.__raza * self.PI

    def descrie(self):
        print('Cel mai probabil NU am colturi')


patrat1 = Patrat(5)
patrat1.descrie()
print(patrat1.aria())


cerc1 = Cerc(7)
cerc1.descrie()
print(cerc1.aria())
