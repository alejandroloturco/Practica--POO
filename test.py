from Clase4_V3 import *

while True:
    x= int(input(":"))
    if x  == 1:
        pac = Paciente()
        pac.asignarCedula(12345)
        pac.asignarGenero("M")
        pac.asignarNombre("Alejo loturco")
        pac.asignarServicio("Cardiologo")

        sis = Sistema()
        sis.ingresarPaciente(pac)
    elif x==2:
        pacs = sis.verDatosPaciente("alejo") 
        if pacs != None:
                for p in pacs:
                    print("Nombre: " + p.verNombre()) 
                    print("Cedula: " + str(p.verCedula())) 
                    print("Genero: " + p.verGenero()) 
                    print("Servicio: " + p.verServicio())
       
    elif x==3:
        break

