from abc import ABC, abstractmethod


class CarModel(ABC):
    @abstractmethod
    def volan(self):
        raise NotImplemented

    @abstractmethod
    def roti(self):
        raise NotImplemented

    @abstractmethod
    def scaune(self):
        raise NotImplemented

    def sistem_audio(self):
        print('Avem sistem audio')


# Mostenirea
class OldCar(CarModel):

    def __pilot_automat(self):
        print('este pe pilot automat') #private methode

    def _valoare_sentimentala(self):
        self.__pilot_automat()
        print('masina de colectie') # protected method

    def scaune(self):
        print('are 4 scaune') # metode publice
    def volan(self):
        print('Masina are volan pe stanga')

    def motor(self):
        print('Are motor diesel')

    def roti(self):
        print('Masina are roti de lemn')


class ModernCar(OldCar):

    def oglinzi(self):
        print('Are 5 oglinzi')

    def roti(self):
        print('Masina are roti de cauciuc')

    def absenabled(self):
        print('Are abs')

    def airbag(self):
        print('Are airbaguri')

    def extra_optiuni(self):
 #       self.__pilot_automat() # metodele private nu pot fi vazute in clasa copil
        self._valoare_sentimentala()


class BritishCar(ModernCar):

    def volan(self):
        print('Volan pe dreapta')

    def gps(self):
        print('Are gps')

class AlienCar(CarModel):

    def volan(self):
        print('Volan verde')

    def roti(self):
        print('are si roata de rezerva')

    def scaune(self):
        print('6 din piele')


dacia = OldCar()
renault = ModernCar()
british_renault = BritishCar()
alien = AlienCar()


dacia.roti()
renault.roti()
british_renault.roti()
british_renault.volan()
renault.volan()
alien.volan()
renault.extra_optiuni()
renault._valoare_sentimentala()

#TODO Cream un packet de python care sa se numeasca Car si fiecare clasa sa fie mutata intr-un fisier nou
# crearea unui mini proiect oop care sa simuleze teste