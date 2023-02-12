class FormaGeometrica:
    PI = 3.14

    def descrie(self):
        print("Cel mai probabil am colturi")

    def aria(self):
        pass

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, value):
        self.__latura = value

    @latura.deleter
    def latura(self):
        del self.__latura

    def aria(self):
        return self.latura ** 2

    def descrie(self):
        print("Eu am colturi")

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, value):
        self.__raza = value

    @raza.deleter
    def raza(self):
        del self.__raza

    def aria(self):
        return self.PI * self.raza ** 2

    def descrie(self):
        print("Eu nu am colturi")

p = Patrat(5)
print(p.aria())
p.descrie()

c = Cerc(5)
print(c.aria())
c.descrie()
