class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}€, TVA: {self.TVA}%, Prix TTC: {self.CalculerPrixTTC()}€"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

produit1 = Produit("Ordinateur", 1000, 20)
produit2 = Produit("Clavier", 50, 20)

print(" État Initial")
print(produit1.afficher())
print(produit2.afficher())

produit1.modifierNom("PC Gamer")
produit1.modifierPrix(1200)

produit2.modifierNom("Clavier Mécanique")
produit2.modifierPrix(80)

print("\n Après Modifications ")
print(f"Nouveau nom produit 1: {produit1.getNom()}")
print(f"Nouveau prix TTC produit 1: {produit1.CalculerPrixTTC()}€")

print(f"Nouveau nom produit 2: {produit2.getNom()}")
print(f"Nouveau prix TTC produit 2: {produit2.CalculerPrixTTC()}€")