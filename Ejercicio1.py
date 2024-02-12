def EscribirCentrado(texto):
  """
  Función que escribe un texto centrado en pantalla, suponiendo una anchura de 80 columnas.

  Parámetros:
    texto (str): El texto que se desea escribir centrado.

  Retorno:
    None.
  """
  longitud_texto = len(texto)
  espacios_izquierda = int((80 - longitud_texto) / 2)
  print("=" * 80)
  print("{}{}".format(" " * espacios_izquierda, texto))
  print("=" * 80)

# Ejemplo de uso
EscribirCentrado("Hola Mundo!")
EscribirCentrado("Este es un texto más largo")