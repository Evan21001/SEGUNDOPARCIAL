import sys
import math

def principal():
    opcion_elegida = sys.argv[1]
    if opcion_elegida == "ayuda":
        print("Los valores de cada figura deben estar separados por comas y cada figura por |")
    if opcion_elegida == "CIRCULO":
        formula_circulo(sys.argv[2])
    if opcion_elegida == "RECTANGULO":
        formula_rectangulo(sys.argv[2], sys.argv[3])
    if opcion_elegida == "TRIANGULO":
        formula_triangulo(sys.argv[2], sys.argv[3])


def formula_circulo(radio):
    radio = float(radio)
    circulo = 3.14*(math.pow(radio, 2))
    print (circulo)
def formula_rectangulo(largo, ancho):
    largo = float(largo)
    ancho = float(ancho)
    rectangulo = largo * ancho
    print (rectangulo)
    
def formula_triangulo(base, altura):
    base = float(base)
    altura = float(altura)
    triangulo = (base * altura) / 2
    print(triangulo)

principal()