from math import *
 
class Point():
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y

    def afficher(self):
        print("Point({},{}) ".format(self.x, self.y))

    def __str__(self):
        return "( %d, %d )" %( self.x, self.y )

class Circle(Point):
    def __init__(self, x = 0, y = 0, radiusValue = 0.0 ):
        Point.__init__(self,x,y)
        self.radius = float( radiusValue )
    def __str__(self):    
        return "Center = %s Radius = %f" %(Point.__str__( circle ), self.radius )

    def getPerimetre(self):
        perimetre = 2*pi*(self.radius)
        print("le perimetre du cercle est : {}".format(perimetre))

    def getSurface(self):
        surface = pi*(self.radius)**2
        return surface
    
    def afficher(self):
        print("CERCLE ({},{},{})".format(self.x, self.y, self.radius) )

    def formEquation(self, a, b):      
        return (a-self.x)**2 + (b-self.y)**2 -self.radius**2

    def appartient(self, a, b):
        if(self.formEquation(a,b)==0):
            print("le point p({},{}) appartient au cercle C".format(a,b))
        else:
            print("le point p({},{}) n'appartient pas au cercle C".format(a,b))
    

class Cylindre(Circle):
    def __init__(self,x,y,radius,hauteur):
        Circle.__init__(self,x,y,radius)
        self.hauteur = float(hauteur)

    def __str__(self):    
         return "( %d, %f, %s )" %(Point.__str__( circle ), self.radius, self.hauteur )

    def getVolume(self):
        result = self.getSurface() * self.hauteur
        return result


point1 = Point(2,4)

point1.afficher()

circle = Circle(1,2,1)

circle.getPerimetre()
print("la surface du cercle est : {}".format(circle.getSurface())) 
circle.afficher()
circle.appartient(1,1)


cylindre1 = Cylindre(4,4,4,4)
print("le volume du cylindre est: {}".format(cylindre1.getVolume()))
