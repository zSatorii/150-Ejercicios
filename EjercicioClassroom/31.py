import random
class Animal:
def __init__(self, nombre, tipo, energia=100, posicion_x=0, posicion_y=0):
self.nombre = nombre
self.tipo = tipo # "herbívoro", "carnívoro"
self.energia = energia
self.posicion_x = posicion_x
self.posicion_y = posicion_y
self.vivo = True

def mover(self):
"""Mueve el animal aleatoriamente"""
if self.vivo:
self.posicion_x += random.randint(-1, 1)
self.posicion_y += random.randint(-1, 1)
self.energia -= 5 # Moverse cuesta energía
if self.energia <= 0:
self.vivo = False
print(f"