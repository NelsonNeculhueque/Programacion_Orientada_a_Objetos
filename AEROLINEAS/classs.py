class Avion:
    def __init__(self, Modelo, Numero_A):
        self.Modelo = Modelo
        self.Numero_A = Numero_A

Avion_1 = Avion("Airbus A320", 223)
Avion_2 = Avion("Embraer E195", 132)
Avion_3 = Avion("Boeing 737", 220)

class Vuelo:
    def __init__(self, Numero_Vuelo, Origen, Destino, Fecha_Hora, Avion_Asig, reservaciones):
        self.Numero_Vuelo = Numero_Vuelo
        self.Origen = Origen
        self.Destino = Destino
        self.Fecha_Hora = Fecha_Hora
        self.Avion_Asig = Avion_Asig
        self.reservaciones = reservaciones
