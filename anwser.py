

distancia = float(input("distancia de vuelo en km:"))
print("Nacional(1)-Internacional(2)")
vuelo = int(input("tipo de vuelo:)")
carga=0

while (carga <= 337250) :
    peso = float(input("peso del paquete en Kg:"))
    carga = carga + peso
    if (peso > 10):
        if (carga <= 355000) :
            if (peso > 100 and vuelo ==1) :
                ValorTotal = (peso * 4500 + distancia * 4000) * 0.85
                print("Valor del paquete",ValorTotal)
            elif (peso > 400 and distacia > 8000 and vuelo == 2):
                ValorTotal = (peso * 4500 + distancia * 4000) * 0.9
                print("Valor del paquete",ValorTotal)
            else:
                print("no se puede calcular el valor")
        else:
            print("El paquete no puede ser abordado al avion")
    else:
        print("el peso no es aceptado")