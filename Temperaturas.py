# Pronóstico semanal de temperaturas (máximas en °C)
# Ciudades: Guayaquil, Salitre, Quito
# Semana: 1 (Lunes a Domingo)

temperaturas = [
    [   # Ciudad 1: Guayaquil
        [   # Semana 1
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
        [   # Semana 1
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
        [   # Semana 1
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

# Lista de nombres de ciudades
nombres_ciudades = ["Guayaquil", "Salitre", "Quito"]

# Calcular el promedio de temperaturas para cada ciudad
for i, ciudad in enumerate(temperaturas):
    for j, semana in enumerate(ciudad, start=1):
        suma = sum(dia['temp'] for dia in semana)
        promedio = suma / len(semana)
        print(f"{nombres_ciudades[i]} - Semana {j}: Promedio = {promedio:.2f} °C")
