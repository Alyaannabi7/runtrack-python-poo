class Personne:
    def __init__(self, personne1, personne2):
        self.personne1 = personne1
        self.personne2 = personne2

personne_instance = Personne("john doe", "jean dupond")
print("je suis ", personne_instance.personne1,".")
print("je suis " , personne_instance.personne2, ".")



