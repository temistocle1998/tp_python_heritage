from math import *
    
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher(self):
        print("Point({},{}) ".format(self.x, self.y))

class Cercle():
    def __init__(self,a,b,r):
        #Point.__init__(self,x,y)  # call base-class constructor
        self.a = a
        self.b = b
        self.r = r

    def getPerimetre(self):
        perimetre = 2*pi*(self.r)
        print("le perimetre du cercle est : {}".format(perimetre))

    def getSurface(self):
        surface = pi*(self.r)**2
        print("la surface du cercle est : {}".format(surface)) 

    def formEquation(self, x, y):      
        return (x-self.a)**2 + (y-self.b)**2 -self.r**2

    def appartient(self, x, y):
        if(self.formEquation(x,y)==0):
            print("le point p({},{}) appartient au cercle C".format(x,y))
        else:
            print("le point p({},{}) n'appartient pas au cercle C".format(x,y))
    
    def afficher(self):
        print("CERCLE ({},{},{})".format(self.a, self.b, self.r) )


class Cylindre(Cercle):
    def __init__(self, r, hauteur):
        Cercle.__init__(self, r)
        self.hauteur = hauteur
    
    def getVolume(self):
        return self.getSurface() * self.hauteur

point1 = Point(2,4)
cercle1 = Cercle(1,2,1)

point1.afficher()

cercle1.getPerimetre()
cercle1.getSurface()
cercle1.appartient(1,1)
cercle1.afficher()

cylindre1 = Cylindre(5,7)
print(cylindre1.getVolume())