from abc import abstractmethod

try:
    lista = [1, 2, 3]
    lista[6]
except IndexError as e:
    print(e)


class Chef: # clasa parinte


    def make_salad(self):
        print('salad')
    def make_fries(self):
        print('fries')

    # clasa copil care mosteneste clasa Chef (se trece intre paranteze numele clasei parinte)
class JapaneseChef(Chef):
    def make_sushi(self):
        print('sushi')
class ItalianChef(Chef):
    def make_pizza(self):
        print('pizza')


# polimorfism with class methods
class Romania():
    def language(self):
        print('Romania')
class USA():
    def language(self):
        print('English')
obj_ro = Romania()
obj_usa = USA()
for country in (obj_usa, obj_ro):
    country.language()


# user polymorphic function

def add(x, y, z=0):
    return x + y + z

print(add(2,3))
print(add(2, 3, 4))

# ex de built in polymorphic function

print(len("abc"))
print(len([1, 2, 3, 4]))

class Animal(ABC):

    @abstractmethod
    def sound(self):
        raise NotImplementedError

    @abstractmethod
    def sleep(self):
        raise  NotImplementedError

class Dog(Animal):

    def sound(self):
        print('Ham Ham!')

    def sleep(self):
        print('ZZZZZZ')

class Cat(Animal):
    def sound(self):
        print('Miau Miau')
    def sleep(self):
        print('prrr')

# incapsulare
calss Car:
    __color = 'gray'

    def get_color(self): # folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoarea_dorita): # folosim setter ca sa setam o alta culoare
        self.__color = culoarea_dorita
    def hidden(self):
        pass