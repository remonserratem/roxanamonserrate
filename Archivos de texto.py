# ==============================================================
# TAREA: Trabajo con Archivos de Texto en Python
# ASIGNATURA: Fundamentos de Programación
# DOCENTE: Ing. Edwin Gustavo Fernández Sánchez, Mgs.
# ==============================================================
# OBJETIVO:
# Practicar las operaciones básicas de lectura y escritura
# de archivos en Python, según el tema 4.2.2 del material docente.
# ==============================================================

# -----------------------------
# 1. ESCRITURA DE ARCHIVO
# -----------------------------
# 1. ESCRITURA DE ARCHIVO
archivo = open("my_notes.txt", "w", encoding="utf-8")

archivo.write("1️⃣ Hoy aprendí cómo crear y manejar archivos en Python.\n")
archivo.write("2️⃣ Es importante cerrar los archivos después de usarlos.\n")
archivo.write("3️⃣ La función open() se usa para abrir archivos en diferentes modos.\n")

archivo.close()
print("✅ Archivo 'my_notes.txt' creado y escrito correctamente.\n")

# 2. LECTURA DE ARCHIVO
archivo = open("my_notes.txt", "r", encoding="utf-8")
linea = archivo.readline()

while linea:
    print(linea.strip())
    linea = archivo.readline()

archivo.close()
print("\n🔒 ¿El archivo está cerrado?", archivo.closed)
