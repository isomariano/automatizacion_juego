import pyautogui
import time

def esperar(imagen, tiempo):
	time.sleep(tiempo)
	while True:
		time.sleep(1)
		objetivo = pyautogui.locateCenterOnScreen(imagen, confidence=0.8)

		if objetivo is None:
			return

def imgError(imagen_ok, imagen_error):
	while True:
		ok = pyautogui.locateCenterOnScreen(imagen_ok, confidence=0.8)
		error = pyautogui.locateCenterOnScreen(imagen_error, confidence=0.8)

		if ok is not None:
			return True
		elif error is not None:
			return False

		time.sleep(2)

def buscar_una_vez(imagen):
	objetivo = pyautogui.locateCenterOnScreen(imagen, confidence=0.8)

	if objetivo is not None:
		return True
	else:
		return False

def buscar(imagen):
	for intento in range(5):
		objetivo = pyautogui.locateCenterOnScreen(imagen, confidence=0.8)

		if objetivo is not None:
			return True
		
		time.sleep(3)

	return False

def obtener_objetivo(imagen):
	while True:
		time.sleep(0.5)
		objetivo = pyautogui.locateCenterOnScreen(imagen, confidence=0.8)

		if objetivo is not None:
			return objetivo
		else:
			print (imagen + ' object is not present on screen yet')
			time.sleep(3)

def obtener_doble(imagen, imagen2):
	for intento in range(10):
		objetivo = pyautogui.locateCenterOnScreen(imagen, confidence=0.8)
		objetivo2 = pyautogui.locateCenterOnScreen(imagen2, confidence=0.8)

		if objetivo is not None:
			return objetivo
		elif objetivo2 is not None:
			return objetivo2

		print (imagen + " and " + imagen2 + ' objects are not present on screen yet')
		time.sleep(2)

def click(imagen):
	objetivo = obtener_objetivo(imagen)
	pyautogui.click(objetivo)

def click_dos_imagenes(imagen, imagen2):
	objetivo = obtener_doble(imagen, imagen2)
	pyautogui.click(objetivo)

def doble_click(imagen):
	objetivo = obtener_objetivo(imagen)
	pyautogui.doubleClick(objetivo)

def click_derecho(imagen):
	objetivo = obtener_objetivo(imagen)
	pyautogui.rightClick(objetivo)

def escribir(texto):
	pyautogui.write(texto)

def presionar(tecla):
	pyautogui.press(tecla)