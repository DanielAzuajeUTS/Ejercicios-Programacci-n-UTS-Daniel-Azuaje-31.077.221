def ConvertirEspaciado(texto):
  """
  Función que recibe un texto y devuelve una cadena con un espacio adicional tras cada letra.

  Parámetros:
    texto (str): El texto original.

  Retorno:
    Una cadena con un espacio adicional tras cada letra del texto original.
  """
  nuevo_texto = ""
  for letra in texto:
    nuevo_texto += letra + " "
  return nuevo_texto

def main():
  """
  Programa principal que pide un texto al usuario y muestra el resultado de aplicar la función ConvertirEspaciado.
  """
  texto = input("Introduce un texto: ")
  texto_con_espaciado = ConvertirEspaciado(texto)
  print(f"Texto original: {texto}")
  print(f"Texto con espaciado: {texto_con_espaciado}")

if __name__ == "__main__":
  main()
