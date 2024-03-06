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
#Entre la clase paciente y la clase sistema hay composicion         
class Sistema:    
    def __init__(self):
        self.__lista_pacientes = [] 
        staticmethod

    #Metodo que permite verificar si ya existe un paciente almacenado por medio de cedula, nombre y apellido
    def verificarPaciente2(self, d): 
        for p in self.__lista_pacientes:
            names = p.verNombre().split(" ")
            if d == p.verCedula():
                return True 
            elif d.upper() == p.verNombre().upper():
                return True 
            elif d.upper() == names[0].upper():
                return True 
            elif d.upper() == names[1].upper():
                return True             
        return False
        
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
    
    #Metodo que permite retornar los datos del paciente a modo de listas, sin importar si el usuario no se sabe la cedula o nombre y apellido
    def verDatosPaciente(self, d):
        lista1 = []
        if self.verificarPaciente2(d) == False:
            return None
        for p in self.__lista_pacientes:
            try:
                #retorne la cedula y la comparo con la ingresada por teclado
                names = p.verNombre().split(" ")
                #print(type(int(d)),type(p.verCedula()))
                if d.upper() == names[0].upper():
                    lista1.append(p)
                    if len(self.__lista_pacientes) == 1:
                        return lista1
                    continue
                elif d.upper() == names[1].upper():
                    lista1.append(p)
                    if len(self.__lista_pacientes) == 1:
                        return lista1
                    continue
                elif d.upper() == p.verNombre().upper():
                    lista1.append(p)
                    return lista1
                elif d == p.verCedula():
                    lista1.append(p)
                    return lista1
                
            except ValueError:
                continue   
        return lista1 

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
            cedula = input("Ingrese la cedula: ") 
            if sis.verificarPaciente2(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre y apellido: ")) 
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
            c = input("Ingrese la cedula o el nombre a buscar: ") 
            #le pido al sistema que me devuelva en la variable p al paciente que tenga
            #la cedula c en la lista
            pacs = sis.verDatosPaciente(c) 
            #print(pacs)
            #2. si encuentro al paciente imprimo los datos
            if pacs != None:
                for p in pacs:
                    print("Nombre: " + p.verNombre()) 
                    print("Cedula: " + str(p.verCedula())) 
                    print("Genero: " + p.verGenero()) 
                    print("Servicio: " + p.verServicio())

            else:
                print("No existe un paciente con esa cedula") 
                
        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 
        
        
        
        
        
        
        
        
