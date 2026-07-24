def procesar(datos):
    if not datos:
        raise ValueError("datos vacios")
    datos = limpiar(datos)
    datos = normalizar(datos)
    return datos
