def EsMultiplo(numero1, numero2):
  """
  Función que comprueba si un número es múltiplo de otro.

  Parámetros:
    numero1 (int): El primer número.
    numero2 (int): El segundo número.

  Retorno:
    True si el primer número es múltiplo del segundo, False en caso contrario.
  """
  return numero1 % numero2 == 0

# Pedir dos números al usuario
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Comprobar si alguno de los dos números es múltiplo del otro
if EsMultiplo(numero1, numero2):
  print(f"{numero1} es múltiplo de {numero2}")
elif EsMultiplo(numero2, numero1):
  print(f"{numero2} es múltiplo de {numero1}")
else:
  print(f"{numero1} no es múltiplo de {numero2}")
  print(f"{numero2} no es múltiplo de {numero1}")
