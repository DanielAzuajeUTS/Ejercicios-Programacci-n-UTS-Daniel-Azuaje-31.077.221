def CalcularTemperaturaMedia(temperatura_maxima, temperatura_minima):
  """
  Función que calcula la temperatura media de un día a partir de la temperatura máxima y mínima.

  Parámetros:
    temperatura_maxima (float): La temperatura máxima del día.
    temperatura_minima (float): La temperatura mínima del día.

  Retorno:
    La temperatura media del día.
  """
  return (temperatura_maxima + temperatura_minima) / 2

def main():
  """
  Programa principal que pide al usuario la temperatura máxima y mínima de cada día y muestra la temperatura media.
  """
  numero_dias = int(input("Introduce el número de días: "))

  for i in range(numero_dias):
    print(f"Día {i + 1}")
    temperatura_maxima = float(input("Introduce la temperatura máxima: "))
    temperatura_minima = float(input("Introduce la temperatura mínima: "))

    temperatura_media = CalcularTemperaturaMedia(temperatura_maxima, temperatura_minima)
    print(f"La temperatura media del día {i + 1} es: {temperatura_media:.2f} °C")

if __name__ == "__main__":
  main()
