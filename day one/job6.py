class Animal:
    def __init__ (self):
        self.age = 0
        self.prenom = ""
    def vieillir (self):
        self.age = self.age +1

    def nommer (self, nouveau_prenom):
        self.prenom = nouveau_prenom

mon_Animal = Animal()

print ("l'age de l'animal ", mon_Animal.age, "ans" )

mon_Animal.vieillir ()
print ("lage de l'animal:" , mon_Animal.age, "ans")

mon_Animal.nommer("luna")
print("l'animal se nomme", mon_Animal.prenom)








    
    