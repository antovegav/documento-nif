from email.errors import FirstHeaderLineIsContinuationDefect
from turtle import clearscreen, clearstamp
import numpy as np
'''
import time
#time.sleep()
time.sleep(2)
clearscreen
'''
nif = []
validacionNif = []
listaNombre = []
listaEdad = []
verifNif = "99999999-RTX"
verifNif = len(verifNif)
verifNombre = "A234567X"
verifNombre = len(verifNombre)
datoNombre = "A234568X"
conyuge = ['Soltero']
fecNac = 2022
menu = 6
#Menu
try:
    while menu == 6:
        menu = int(input("1)\tRegistrar Datos \n2)\tBuscar Datos \n3)\tImprimir Certificados \n4)\tSalir\n"))
    #OPCION 1
        if menu == 1:
            nifPersona = str(input("Ingrese su NIF con la siguiente estructura:\n99999999-RTX\n03034567-XXY\n12312345-CCU\n00000001-03F\n"))
            if nifPersona == int:
                print("\t\tERROR")
                print("Vuelva a Ingresar su NIF: ")
                nifPersona = input()
                break
            validacionNif.append(nifPersona)
            nifPersona = len(nifPersona)
            nif.append(nifPersona)
            while nifPersona != verifNif:
                print("\t\tERROR")
                print("Vuelva a ingresar su NIF:")
                nifPersona = input()
            validacionNif.append(nifPersona)
            validacionNif.remove(12)
    #nif guarda el len
    #validacionNif GUARDA EL NIF

            nombre = input("Ingrese su nombre (minimo 8 caracteres):\n")
            datoNombre = len(nombre)
            while datoNombre < verifNombre:
                print("\t\tERROR")
                nombre = input("Vuelva a ingresar un nombre mayor a 8 caracteres:\n")
            listaNombre.append(nombre)
            edad = int(input("Ingrese su edad:\n"))
            while edad < 0 or edad >= 100:
                print("\t\tERROR")
                edad = int(input("Vuelva a ingresar una edad valida:\n"))
            listaEdad.append(edad)
            listaMaestra = nif + listaNombre + listaEdad
            menu = 6

    #OPCION 2
        if menu == 2:
            print("Ingrese su NIF\n")
            nifPersona = input()
            if nifPersona in validacionNif:
                print("\t\tDatos")
                print("NIF:\t",nifPersona,"\nNombre:\t",listaNombre,"\nEdad:\t",listaEdad)
            else:
                print("\t\tERROR")
                print("Su NIF es incorrecto o no pertenece a la Union Europea")
            menu = 6
    #OPCION 3
        if menu == 3:
            print("Certificado")
            print("ESTADO CONYUGAL:\t",conyuge)
            print("FECHA DE NACIMIENTO:\t",(fecNac - edad))
            print("NIF:\t",nif)
            print("NOMBRE:\t",listaNombre)
            print("EDAD:\t",listaEdad)
            menu = 6
            
        if menu > 4 or menu < 0:
            print("vuelva a ingresar una opcion:\n")
            menu = 6


        if menu == 4:
            print("¡Hasta la proxima!")
            menu = 0
    print("Antonio Vega - v01.00")
except NameError:
    print("Nombre no definido")
except TypeError:
    print("Tipo no definido")
except:
    print("Dato no valido")