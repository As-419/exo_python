class Rectangle:
    Nrect=0
    MaxSurface=None
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
        Rectangle.Nrect += 1
        surface = self.area()
        if Rectangle.MaxSurface is None or surface > Rectangle.MaxSurface:
            Rectangle.MaxSurface = surface

    @classmethod
    def getNrect(cls):
        return cls.Nrect

    @classmethod
    def getMaxSurface(cls):
        return cls.MaxSurface
    def __repr__(self):
        return f"Rectangle(largeur={self.__largeur}, hauteur={self.__hauteur})"
    def __str__(self):
        return f"Rectangle de largeur {self.__largeur} et de hauteur {self.__hauteur}"
    @staticmethod
    def plus_grand(rect1, rect2):
        return rect1 if rect1.surface() > rect2.surface() else rect2
