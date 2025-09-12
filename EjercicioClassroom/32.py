import re # Regular expressions para patrones avanzados
def analizar_estructura(texto):
    """Analiza la estructura básica del texto"""
    estadisticas = {
    'caracteres_total': len(texto),
    'caracteres_sin_espacios': len(texto.replace(' ', '')),
    'palabras': len(texto.split()),
    'oraciones': len([s for s in texto.split('.') if s.strip()]),
    'párrafos': len([p for p in texto.split('\n\n') if p.strip()])
}
return estadisticas

def encontrar_patrones_email(texto):
    """Encuentra direcciones de email en el texto"""
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(patron_email, texto)
    return emails

def encontrar_patrones_telefono(texto):
    """Encuentra números de teléfono en diferentes formatos"""
    patrones = [
    r'\b\d{3}-\d{3}-\d{4}\b', # 123-456-7890
    r'\b\(\d{3}\)\s?\d{3}-\d{4}\b', # (123) 456-7890
    r'\b\d{10}\b' # 1234567890
    ]
    telefonos = []
    for patron in patrones:
    telefonos.extend(re.findall(patron, texto))
    return telefonos

def analizar_sentimiento_basico(texto):
    """Análisis básico de sentimiento basado en palabras clave"""
    palabras_positivas = [
    'excelente', 'genial', 'fantástico', 'increíble', 'perfecto',
    'bueno', 'feliz', 'contento', 'alegre', 'maravilloso'
    ]
    palabras_negativas = [
    'terrible', 'malo', 'horrible', 'triste', 'enojado',
    'molesto', 'frustrado', 'decepcionado', 'pesimo'
    ]
    texto_lower = texto.lower()
    puntuación_positiva = sum(1 for palabra in palabras_positivas if palabra in texto_lower)
    puntuación_negativa = sum(1 for palabra in palabras_negativas if palabra in texto_lower)
if puntuación_positiva > puntuación_negativa:
    sentimiento = "Positivo"
    elif puntuación_negativa > puntuación_positiva:
        sentimiento = "Negativo"
    else:
    sentimiento = "Neutral"

return {
'sentimiento': sentimiento,
'palabras_positivas_encontradas': puntuación_positiva,
'palabras_negativas_encontradas': puntuación_negativa
}
def encontrar_palabras_repetidas(texto, min_longitud=4):
"""Encuentra palabras que se repiten frecuentemente"""
# Limpiar y dividir el texto
palabras = re.findall(r'\b\w+\b', texto.lower())
palabras_largas = [p for p in palabras if len(p) >= min_longitud]
# Contar frecuencias
frecuencias = {}
for palabra in palabras_largas:
frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
# Filtrar solo las que aparecen más de una vez
repetidas = {palabra: freq for palabra, freq in frecuencias.items() if freq > 1}
return repetidas
def generar_resumen_legible(estadisticas):
"""Convierte estadísticas en texto legible"""
est = estadisticas
promedio_palabras_oracion = est['palabras'] / max(est['oraciones'], 1)
resumen = []
resumen.append(f"Este texto tiene {est['caracteres_total']} caracteres en total")
resumen.append(f"Contiene {est['palabras']} palabras distribuidas en {est['oraciones']} oraciones")
resumen.append(f"El promedio es de {promedio_palabras_oracion:.1f} palabras por oración")
if est['párrafos'] > 1:
resumen.append(f"Está organizado en {est['párrafos']} párrafos")
return resumen

# Función principal de análisis
def analizar_texto_completo(texto):
"""Realiza un análisis completo del texto"""
print("