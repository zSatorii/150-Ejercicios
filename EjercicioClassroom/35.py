from collections import Counter
import heapq
class NodoHuffman:
    """Nodo para el árbol de codificación Huffman"""
def __init__(self, char, freq, left=None, right=None):
    self.char = char
    self.freq = freq
    self.left = left
    self.right = right
def __lt__(self, other):
    return self.freq < other.freq
def comprimir_repeticion_simple(texto):
    """
    Compresión simple: reemplaza secuencias repetidas
    Ejemplo: "aaaa" -> "4a"
    """
    print(".")