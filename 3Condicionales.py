#metemos un valor por teclado
sueldo = int(input("Introduce el sueldo:"))

#condicional if
if sueldo>3000: #operador de comparación
    print("El usuario debe pagar un porcentaje en impuestos.")

if sueldo<=3000: #operador de comparación
    print("El usuario esta exento de declarar su renta.")

if sueldo>6000 and sueldo<10000: #operador lógico se tiene que cumplir las dos condiciones
    print("El usuario tiene que pagar una bonificación de 1000 euros.")

if sueldo==20000 or sueldo==30000: #operador lógico se tiene que cumplir una de las dos condiciones
    print("El usuario paga un 10 por ciento de su sueldo.")


#Ej.Sueldo if else

sueldo2 = int(input("Introduce el sueldo 2: "))
sueldo3 = int(input("Introduce el sueldo 3: "))

if sueldo2>sueldo3:
    print("El sueldo 2 ", (sueldo2), " es mayor que el sueldo 3 ", (sueldo3))
else:
    print("El sueldo 3 " +str(sueldo3) + " es mayor que el sueldo 2 " +str(sueldo2))
    