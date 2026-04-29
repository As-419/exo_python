class Employe :
    def __init__(self,nom):
       self.nom=nom
    def travailler(self):
         return f"{self.nom} travailler."
class Instructeur:
    def __init__(self,nom):
        self.nom=nom
    def  enseigner(self):
        return f"{self.nom} enseigne.."
class Formateur( Employe ,Instructeur):
    def  enseigner(self):
        return f"{self.nom} enseigne.."
    def travailler(self):
         return f"{self.nom} travailler."
p1 =Formateur ( "Samba")

print(p1.enseigner())
print(p1.travailler())