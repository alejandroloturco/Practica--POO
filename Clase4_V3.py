class Paciente:
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
              
    #metodos get    
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
    # metodos set
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s 
        
class Sistema:    
    def __init__(self):
        self.__lista_pacientes = [] 
        staticmethod
    def verificarPaciente(self,cedula ):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return True 
        return False

    def verificarPaciente2(self,cedula = 0, nombre = "", apellido = "", completo = ""):
        for p in self.__lista_pacientes:
            names = p.vernombre().split(" ")
            if cedula == p.verCedula():
                return True 
            elif completo.upper() == p.vernombre().upper():
                return True 
            elif nombre.upper() == names[0].upper():
                return True 
            elif apellido.upper() == names[1].upper():
                return True             
        return False
        
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self, cc = 0, nombre = "", apellido = ""):
        if self.verificarPaciente2(cc,nombre,apellido) == False:
            return None
        for p in self.__lista_pacientes:
            #retorne la cedula y la comparo con la ingresada por teclado
            names = p.vernombre().split(" ")
            if cc == p.verCedula(cc):
                return p #si encuentro el paciente lo retorno 
            elif nombre == names[0]:
                return p 
            elif apellido == names[1]:
                return p
            
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 

def main():
    sis = Sistema() 
    #probemos lo que llevamos programado
    while True:
        #TAREA HACER EL MENU
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente\n\t--> ")) 
        
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            #1. solicito la cedula que quiero buscar
            while True:
                mini_menu = int(input("""Seleccione el tipo de dato por el que desea buscar al paciente: 
                                    \n1. Cedula
                                    \n2. Nombre
                                    \n3. Apellido
                                    \n4. Nombre Completo"""))
                if mini_menu == 1:
                    if p.verificarPaciente2(cedula):
                        c = int(input("Ingrese la cedula a buscar: ")) 
                        #le pido al sistema que me devuelva en la variable p al paciente que tenga
                        #la cedula c en la lista
                        p = sis.verDatosPaciente(c) 
                        #2. si encuentro al paciente imprimo los datos
                        if p != None:
                            print("Nombre: " + p.verNombre()) 
                            print("Cedula: " + str(p.verCedula())) 
                            print("Genero: " + p.verGenero()) 
                            print("Servicio: " + p.verServicio())

                        else:
                            print("No existe un paciente con esa cedula") 
                elif mini_menu == 2:
                    c = input("Ingres el nombre del paciente: ")
                elif mini_menu == 3:
                    c = input("Ingres el nombre del paciente: ")
                elif mini_menu == 4:
                    c = input("Ingres el nombre del paciente: ")
                else:
                    print("Opcion no valida")
                    continue
        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 
        
        
        
        
        
        
        
        
