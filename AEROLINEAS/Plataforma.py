import os

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

    def agregar_reservacion(self, pasajero):
        if len(self.reservaciones) < self.Avion_Asig.Numero_A:
            num_reservacion = len(self.reservaciones) + 1
            reservacion = Reservacion(num_reservacion, pasajero, self)  
            pasajero.vuelos_reservados.append(reservacion) 
            self.reservaciones.append(reservacion)  
            print(f"Reservación exitosa para el vuelo {self.Numero_Vuelo}.")
        else:
            print("No hay asientos disponibles en este vuelo.")


Vuelo_1 = Vuelo("AR 1240", "Chile", "New York", "12-08-2023 14:00", Avion_1,[])
Vuelo_2 = Vuelo("LA 1311", "Peru", "China", "08-04-2023 13:30", Avion_2,[])
Vuelo_3 = Vuelo("AK 4200", "Colombia", "España", "01-12-2023 16:00", Avion_3,[])


class Pasajero:
    def __init__(self, nombre, num_pasaporte):
        self.nombre = nombre
        self.num_pasaporte = num_pasaporte
        self.vuelos_reservados = []

    def reservar_vuelo(self, vuelo):
        if vuelo not in self.vuelos_reservados:
            vuelo.agregar_reservacion(self)
        else:
            print("Ya tienes una reservación para este vuelo.")



class Reservacion:
    def __init__(self, num_reservacion, pasajero, vuelo):
        self.num_reservacion = num_reservacion
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = "reservado"
        pasajero.vuelos_reservados.append(self)

    def cancelar(self):
        self.estado = "cancelado"
        print(f"Reservación {self.num_reservacion} cancelada.")



class PlataformaReservaciones:


    def __init__(self):
        self.vuelos_disponibles = [Vuelo_1,Vuelo_2,Vuelo_3]
        self.pasajeros = []

    def mostrar_vuelos_disponibles(self):
        os.system('cls')
        print(f'''                          -VUELOS DISPONIBLES-''' '\n' '\n')
        for vuelo in self.vuelos_disponibles:
            print('\n' "Número de Vuelo:", vuelo.Numero_Vuelo)
            print("Origen:", vuelo.Origen)
            print("Destino:", vuelo.Destino)
            print("Fecha y Hora:", vuelo.Fecha_Hora)
            print("Avión Asignado:", vuelo.Avion_Asig.Modelo)
            print("Reservaciones:")
            for reservacion in vuelo.reservaciones:
                print('\n'f"- Número de Reservación: {reservacion.num_reservacion}, Pasajero: {reservacion.pasajero.nombre}, Estado: {reservacion.estado}")
            print()
        input("Enter para continuar")


    def reservar_vuelo(self):
        os.system('cls')
        print(f'''          -INGRESE SUS DATOS PARA RESERVAR-''' '\n' '\n')
        nombre = input('\n'"Ingrese su nombre: ")
        num_pasaporte = input('\n'"Ingrese su número de pasaporte: ")
        os.system('cls')
        pasajero = Pasajero(nombre, num_pasaporte)
        self.pasajeros.append(pasajero)
        print(f'''          -INGRESE SU VUELO PARA RESERVAR-''' '\n')

        print('\n'"Seleccione un vuelo para reservar:")
        for num, vuelo in enumerate(self.vuelos_disponibles):
            print(f"{num + 1}. {vuelo.Numero_Vuelo} - {vuelo.Origen} a {vuelo.Destino}")
        seleccion = int(input('\n' "Ingrese el número de vuelo deseado: "))

        if 1 <= seleccion <= len(self.vuelos_disponibles):
            vuelo_seleccionado = self.vuelos_disponibles[seleccion - 1]

            if len(vuelo_seleccionado.reservaciones) < vuelo_seleccionado.Avion_Asig.Numero_A:
                for pasajero_existente in self.pasajeros:
                    if pasajero_existente.num_pasaporte == num_pasaporte:
                        for reservacion in pasajero_existente.vuelos_reservados:
                            if reservacion.vuelo == vuelo_seleccionado:
                                print("Ya tienes una reservación para este vuelo.")
                                input("Enter para continuar")
                                return

                pasajero.reservar_vuelo(vuelo_seleccionado)
                numero_reservacion = pasajero.vuelos_reservados[-1].num_reservacion
                print('\n'f"Reservación exitosa para el vuelo {vuelo_seleccionado.Numero_Vuelo}. Número de Reservación: {numero_reservacion}"'\n' '\n')
            else:
                print("No hay asientos disponibles en este vuelo.")
        else:
            print('\n'"Selección de vuelo no válida.")
        input("Enter para continuar")




    def mostrar_reservaciones_pasajero(self):
        os.system('cls')
        print(f'''          -RESERVACIONES DE PASAJERO-''' '\n' '\n')
        num_pasaporte = input('\n'"Ingrese el número de pasaporte del pasajero: ")
        pasajero_encontrado = None
        for pasajero in self.pasajeros:
            if pasajero.num_pasaporte == num_pasaporte:
                pasajero_encontrado = pasajero
                break

        if pasajero_encontrado:
            print(f"Reservaciones de {pasajero_encontrado.nombre}:")
            vuelos_imprimidos = set()  
            for reservacion in pasajero_encontrado.vuelos_reservados:
                vuelo = reservacion.vuelo
                if vuelo.Numero_Vuelo not in vuelos_imprimidos:
                    print("Número de Vuelo:", vuelo.Numero_Vuelo)
                    print("Origen:", vuelo.Origen)
                    print("Destino:", vuelo.Destino)
                    print("Fecha y Hora:", vuelo.Fecha_Hora)
                    print("Avión Asignado:", vuelo.Avion_Asig.Modelo)
                    print()
                    vuelos_imprimidos.add(vuelo.Numero_Vuelo)
            input("Enter para continuar")
        else:
            print("Pasajero no encontrado.")

            input("Enter para continuar")



    def cancelar_reservacion(self):
        os.system('cls')
        print(f'''          -CANCELAR RESERVACION-''' '\n' '\n')
        num_reservacion = int(input('\n'"Ingrese el número de reservación a cancelar: "))
    
        for vuelo in self.vuelos_disponibles:
            for reservacion in vuelo.reservaciones:
                if reservacion.num_reservacion == num_reservacion:
                    reservacion.cancelar()
                    return
    
        print("Reservación no encontrada.")
        input("Enter para continuar")



    def mostrar_pasajeros_vuelo(self):
        os.system('cls')
        print(f'''          -MOSTRAR RESERVACIONES DE VUELO-''' '\n' '\n')
        numero_vuelo = input('\n'"Ingrese el número de vuelo: ")
        vuelo_encontrado = None
        for vuelo in self.vuelos_disponibles:
            if vuelo.Numero_Vuelo == numero_vuelo:
                vuelo_encontrado = vuelo
                break

        if vuelo_encontrado:
            print('\n'f"Lista de pasajeros del vuelo {vuelo_encontrado.Numero_Vuelo}:")
            for reservacion in vuelo_encontrado.reservaciones:
                print("Nombre del pasajero:", reservacion.pasajero.nombre)
                print("Número de pasaporte:", reservacion.pasajero.num_pasaporte)
                print("Estado de la Reservación:", reservacion.estado)
                input("Enter para continuar")
        else:
            print("Vuelo no encontrado.")

            input("Enter para continuar")



def main():
    plataforma = PlataformaReservaciones()

    while True:
        os.system('cls')
        print(f'''          -BIENVENIDO A LA PLATAFORMA DE RESERVACIONES DE VUELO-''' '\n' '\n')
        print("Menu Incial")
        print("1. Mostrar vuelos disponibles")
        print("2. Reservar vuelo")
        print("3. Mostrar reservaciones de un pasajero")
        print("4. Cancelar reservación")
        print("5. Mostrar lista de pasajeros de un vuelo")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            plataforma.mostrar_vuelos_disponibles()

        elif opcion == "2":
            plataforma.reservar_vuelo()

        elif opcion == "3":
            plataforma.mostrar_reservaciones_pasajero()

        elif opcion == "4":
            plataforma.cancelar_reservacion()

        elif opcion == "5":
            plataforma.mostrar_pasajeros_vuelo()

        elif opcion == "6":
            print("¡Gracias por usar nuestra plataforma!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()