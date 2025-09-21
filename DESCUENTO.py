# Definición de una función con parámetros y valor predeterminado
def calcular_descuento(monto, descuento=10):
    """
    Calcula el descuento de una compra.
    Parámetros:
        monto (float): monto total de la compra.
        descuento (float): porcentaje de descuento a aplicar (10%).
    Retorna:
        float: valor del descuento calculado.
    """
    return monto * (descuento / 100)


# Llamada a la función con valor predeterminado
monto1 = 200
descuento1 = calcular_descuento(monto1)
print(f"Compra 1: Monto = ${monto1}, Descuento = ${descuento1}, Total a pagar = ${monto1 - descuento1}")


# Llamada a la función indicando el porcentaje de descuento
monto2 = 500
descuento2 = calcular_descuento(monto2, 20)
print(f"Compra 2: Monto = ${monto2}, Descuento = ${descuento2}, Total a pagar = ${monto2 - descuento2}")
