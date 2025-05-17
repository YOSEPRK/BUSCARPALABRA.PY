x = open("ruta del archivo")
mostrar = False
for linea in x:
    if linea.strip().lower().startswith("palabra especifica"):
        mostrar = True
    if mostrar:
        print(linea, end="")
