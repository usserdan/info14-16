class Paciente(): 
    def __init__(self):  
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def verServicio(self):
        return self.__servicio 

    def asignarNombre(self,n):
        self.__nombre = n
    def asignarCedula(self,c):
        self.__cedula = c
    def asignarGenero(self,g):
        self.__genero = g
    def asignarServicio(self,s):
        self.__servicio = s 

class Sistema():
    def __init__(self):
        # self.__lista_pacientes = {} #Manejar los pacientes en lista, objeto tipo diccionario
        self.__lista_pacientes = [] #Manejar los pacientes en lista, objeto tipo lista.
        #La siguiente variable siempre dependera del tamaño de la lista, por lo cual no se podra modificar
        # con un método de asignar
        self.__numero_pacientes = len(self.__lista_pacientes)

    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)

    def verNumeroPacientes(self):
        return self.__numero_pacientes

    def verDatosPacientes(self, ced):
        for paciente in self.__lista_pacientes:
            if ced == paciente.verCedula():
                return paciente



def main():

    sistema = Sistema()

    while True:
        
        menu = int(input('''
                    *** SELECCIONE UNA OPCION DEL MENU***
                    1. Ingresar paciente.
                    2. Datos de paciente.
                    3. Numero de pacientes.
                    4. Salir.
                    ----> '''))
        
        if menu == 1:
            
            print("A continuación se solicitan los datos...")
            
            nombre = input("Ingrese el Nombre: ")
            cedula = int(input("Ingrese la Cédula: "))
            genero = input("Ingrese el Género: ")
            servicio = input("Ingrese el Servicio: ")

            paciente = Paciente()
            paciente.asignarNombre(nombre)
            paciente.asignarCedula(cedula)
            paciente.asignarGenero(genero)
            paciente.asignarServicio(servicio)

            sistema.ingresarPaciente(paciente)

        
        elif menu == 2:

            ced = int(input("Ingrese la cedula del paciente: "))

            pac = sistema.verDatosPacientes(ced)
            print("Nombre: " + pac.verNombre())
            print("Cédula: " + str(pac.verCedula()))
            print("Género: " + pac.verGenero())
            print("Servicio: " + pac.verServicio())           
        
        elif menu == 3:
            print("Número total de pacientes: " + str(sistema.verNumeroPacientes()))
        
        elif menu == 4:
            break
        
        else:
            print('<<Opcion no valida>>')