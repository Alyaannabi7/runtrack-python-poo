class addition :
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

addition_instance = addition()

print("le nombre1 est:", addition_instance.nombre1)
print("le nombre2 est:", addition_instance.nombre2)
print("le resultat est:", addition_instance.nombre1 + addition_instance.nombre2)

