from aircraft import Aircraft

modelo = input("Enter aircraft model: ")
air = Aircraft(modelo)
while True:
    comando = input("Enter command (A for ascent, D for descent, X to exit): ")
    if comando == "X":
        break
    elif "A" in comando:
        comando_s = comando.split()
        pies = int(comando_s[1])
        altitud = air.climb(pies)

    elif "D" in comando:
        comando_s = comando.split()
        pies = int(comando_s[1])
        altitud = air.descend(pies)

print(f"Final altitude: {altitud} feet")
