# Tarea: Uso de diccionarios en Python
# Nombre: Roxana Monserrate
# Curso: Primer semestre
# Fecha: 27/09/2025

# 1. Crear un diccionario con mis datos personales
informacion_personal = {
    "nombre": "Roxana Monserrate",
    "edad": 25,
    "ciudad": "Salitre",
    "profesion": "Tecnologías de la Información"
}

# 2. Cambiar el valor de la ciudad
ciudad_anterior = informacion_personal["ciudad"]   # guardo la ciudad antes
informacion_personal["ciudad"] = "Guayaquil"       # cambio a otra ciudad

# 3. Agregar una nueva clave con la ocupación
informacion_personal["ocupacion_actual"] = "Estudiante universitaria"

# 4. Revisar si existe la clave "telefono", y si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "59381211999"

# 5. Eliminar la clave "edad" porque no hace falta
del informacion_personal["edad"]

# 6. Imprimir el resultado final
print("Ciudad anterior:", ciudad_anterior)
print("Diccionario final:", informacion_personal)
