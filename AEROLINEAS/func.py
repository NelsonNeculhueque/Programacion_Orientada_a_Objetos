def agregar_reservacion(self, pasajero):
        if len(self.reservaciones) < self.Avion_Asig.Numero_A:
            num_reservacion = len(self.reservaciones) + 1
            reservacion = Reservacion(num_reservacion, pasajero, self)  
            pasajero.vuelos_reservados.append(reservacion) 
            self.reservaciones.append(reservacion)  
            print(f"Reservación exitosa para el vuelo {self.Numero_Vuelo}.")
        else:
            print("No hay asientos disponibles en este vuelo.")



def reservar_vuelo(self, vuelo):
        if vuelo not in self.vuelos_reservados:
            vuelo.agregar_reservacion(self)
        else:
            print("Ya tienes una reservación para este vuelo.")  


def cancelar(self):
        self.estado = "cancelado"
        print(f"Reservación {self.num_reservacion} cancelada.")

