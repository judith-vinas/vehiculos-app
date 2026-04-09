from vehiculo.base import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    # def descripcion(self):
    #    return f"{super().descripcion()} - {self.puertas} puertas"

    def descripcion(self):
        return f"[COCHE] Marca: {self.marca} | Modelo: {self.modelo} | Puertas: {self.num_puertas}"





