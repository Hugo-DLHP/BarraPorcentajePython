import time

limite = 40
def barraPorcentaje(segmento, total, longitud):
        porcentaje = segmento / total
        completado =int (porcentaje * longitud)
        restante = longitud - completado
        barra = f"[{'#' * completado}{'-' * restante}{':'}{round(porcentaje * 100)}{'%'}]"
        return barra

for i in range(limite + 1):
    time.sleep(0.07)
    print(barraPorcentaje(i, limite, 40), end = "\r")

print("\n")