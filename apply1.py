class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_deplacer(self):
        return f"{self.nom} se déplace."


class Chien(Animal):
    def aboyer(self):
        return f"{self.nom} aboie."

a1 = Chien("Rex", 5)

print(a1.se_deplacer())
print(a1.aboyer())