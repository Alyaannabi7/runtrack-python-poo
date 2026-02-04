class Point: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def afficherLesPoints(self):
        print("Les coordonnées du point sont: (", self.x, ",", self.y, ")")

    def afficherX (self):
        print("la coordonnée x est " , self.x)
    
    def afficherY (self):
        print("les coordonée de Y est :", self.y)
    
    def changerX ( self, new_x):
        self.x = new_x
    
    def changerY (self , new_y ):
        self.y= new_y

point_instance = Point(5, 10)
point_instance.afficherLesPoints()
