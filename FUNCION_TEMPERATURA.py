# Definimos la función que calculará los promedios
def calcular_promedio(ciudades, nombres_ciudades):
    # Recorremos cada ciudad (usamos enumerate para tener también el número de índice)
    for i, ciudad in enumerate(ciudades):
        # Recorremos cada semana dentro de esa ciudad
        for j, semana in enumerate(ciudad, start=1):
            # Sumamos todas las temperaturas de la semana
            suma = sum(dia['temp'] for dia in semana)
            # Calculamos el promedio dividiendo la suma para la cantidad de días
            promedio = suma / len(semana)
            # Mostramos el resultado en pantalla con el nombre de la ciudad y semana
            print(f"{nombres_ciudades[i]} - Semana {j}: Promedio = {promedio:.2f} °C")

# Aquí ponemos los datos de las temperaturas de cada ciudad por día
temperaturas = [
    [   # Ciudad 1: Guayaquil
        [
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ]
    ],
    [   # Ciudad 2: Salitre
        [
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 33}
        ]
    ],
    [   # Ciudad 3: Quito
        [
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 20}
        ]
    ]
]

# Lista con los nombres de las ciudades (para imprimir en el resultado)
nombres_ciudades = ["Guayaquil", "Salitre", "Quito"]

# Llamamos a la función para que calcule y muestre los promedios
calcular_promedio(temperaturas, nombres_ciudades)

