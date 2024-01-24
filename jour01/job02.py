class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

"""Instanciation de la classe avec les valeurs par défaut"""
operation_instance = Operation(12, 3)

"""Impression de l'objet en console"""
print("Objet Operation instancié avec les valeurs par défaut :")
print("Nombre1:", operation_instance.nombre1)
print("Nombre2:", operation_instance.nombre2)
