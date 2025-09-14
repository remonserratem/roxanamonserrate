def calcular_promedio(ciudades, nombres_ciudades):
    for i, ciudad in enumerate(ciudades):
        for j, semana in enumerate(ciudad, start=1):
            suma = sum(dia['temp'] for dia in semana)
            promedio = suma / len(semana)
            print(f"{nombres_ciudades[i]} - Semana {j}: Promedio = {promedio:.2f} °C")

temperaturas = [
    [
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
    [
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
    [
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

nombres_ciudades = ["Guayaquil", "Salitre", "Quito"]

calcular_promedio(temperaturas, nombres_ciudades)
