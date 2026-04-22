import math as m

class Point3D:
    
    Npts = 0
    mx = None
    my = None
    mz = None
    
    def __init__(self, x, y, z):
        # attributs privés
        self.__x = x
        self.__y = y
        self.__z = z

        Point3D.Npts += 1

        
        if Point3D.mx is None or x > Point3D.mx:
            Point3D.mx = x

        if Point3D.my is None or y > Point3D.my:
            Point3D.my = y

        if Point3D.mz is None or z > Point3D.mz:
            Point3D.mz = z


    @classmethod
    def getNpts(cls):
        return cls.Npts

    @classmethod
    def getMaxX(cls):
        return cls.mx

    @classmethod
    def getMaxY(cls):
        return cls.my

    @classmethod
    def getMaxZ(cls):
        return cls.mz

    
    def afficher_coord(self):
        print(f"Coordonnées : {self.__x}, {self.__y}, {self.__z}")

    def deplacer(self, dx, dy, dz):
        self.__x += dx
        self.__y += dy
        self.__z += dz
        print(f"Après déplacement : {self.__x}, {self.__y}, {self.__z}")

    def calculer_distance(self, p):
        return m.sqrt(
            (p.__x - self.__x) ** 2 +
            (p.__y - self.__y) ** 2 +
            (p.__z - self.__z) ** 2
        )

    def sur_diagonale(self):
        return self.__x == self.__y == self.__z

    
    def __repr__(self):
        return f'Point3D({self.__x}, {self.__y}, {self.__z})'

    def __str__(self):
        return f'Point({self.__x}, {self.__y}, {self.__z})'

    
    @staticmethod
    def est_diagonale(x, y, z):
        return x == y == z
p=Point3D(5, 8, 10)
print(repr(p))
print(str(p))
p.afficher_coord()
p.deplacer(2, 3, 2)