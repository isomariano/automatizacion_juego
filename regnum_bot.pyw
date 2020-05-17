from desktop_driver import *
import time
import os

def get_config(param):
    path_config=os.path.join(os.getcwd(), "config.txt")
    with open(path_config, "r") as config:
	    texto = config.readlines()
	    for linea in texto:
	        if linea.split('=')[0] == param:
	            return linea.split('=')[1].rstrip()

def loguearse():
	clave=get_config("clave")
	doble_click("img/regnum.png")
	click("img/ro_aceptar.png")
	click("img/ro_clave.png")
	escribir(clave)
	presionar('enter')
	
def ingresar():
	click("img/ro_jugar.png")
	esperar("img/ro_entrando.png", 12)
	click("img/ro_boton_jugar.png")
	esperar("img/ro_entrando.png", 5)

def obtener_recompensa():
	proceso=""
	recompensa = buscar("img/ro_obtener.png")
	
	if recompensa:
		click("img/ro_obtener.png")
		proceso="exito"
	else:
		proceso="fracaso"
	presionar("esc")
	click("img/ro_salir.png")
	return proceso

def registrar_resultado(resultado):
	tiempo= time.ctime(time.time()).split(" ")
	path_registro=get_config("ruta_registro")
	with open(path_registro, "a") as registro:
		registro.write("\n" + tiempo[2] + " " + tiempo[1] + " " + tiempo[3] + " " + resultado)

loguearse()
ingresar()
resultado=obtener_recompensa()
registrar_resultado(resultado)