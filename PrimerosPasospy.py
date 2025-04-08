#Primer programa para meter datos por teclado

print("Datos de la primera persona")

nombre1=input("Ingrese el nombre del producto:")
precio1=int(input("Ingrese el precio del producto:"))
nombre2=input("Ingrese el nombre del segundo producto:")
precio2=int(input("Ingrese el precio:"))

#(los comentarios se hacen con #)
#Esto es una constante 
BONIFICACION = 20

#Ej. Suma dos valores y almacenalos en una variable
precioTotal = precio1 + precio2
print("Precio total:", precioTotal)

#comparar si "precio1"  es mayor que "precio2"
comparar = precio1>=precio2

logico = (precio1 < precio2 and precio1==precio2) #operador logico

cabecera = "resultados del producto {0}. y del producto. {1}:"
#concatenamos las cadenas de texto de varias formas, aquí una con la funcion "format"
print(cabecera.format(nombre1,nombre2))
print("El precio del primer valor es mayor o igual al segundo valor:", comparar)
print("La suma de los dos productos es:" +str(precioTotal))
print("precio1 < precio2 and precio1 ==precio2")
print(logico)

#operador de ASIGNACION son (+=, -=, *=...)
precioTotal += BONIFICACION 
print("Al precio total le sumamos el valor que tiene la constante: " +str(precioTotal))
