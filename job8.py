import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return self.rayon * 2

    def afficherInfos(self):
        print(f"Rayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aire()}")

cercle1 = Cercle(4)
cercle2 = Cercle(7)

print(" Informations Cercle 1 ")
cercle1.afficherInfos()

print("\n Informations Cercle 2 ")
cercle2.afficherInfos()