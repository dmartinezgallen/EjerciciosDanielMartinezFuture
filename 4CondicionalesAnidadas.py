#cuarta clase, condicionales anidadas, vamos a coger cuatro notas pedidas por teclado
#y vamos a calcular la media, luego con if else decimos la nota ("sobresaliente, notable, insuficiente")

nota1=int(input("Introduce la nota 1:"))
nota2=int(input("Introduce la nota 2:"))
nota3=int(input("introduce la nota 3:"))

promedio=(nota1+nota2+nota3)/3

if promedio<=10 and promedio>=9:
    print("Enhorabuena, la media de tus notas es " +str(promedio)+ ", tienes un sobresaliente")
else:

    if promedio<9 and promedio>=7:
        print("Bien hecho, la media de tus notas es " +str(promedio)+ ", por lo que tienes un notable.")
    else:
        if promedio<7 and promedio>=6:
            print("No está mal, la media de tus notas es " +str(promedio)+ ", por lo que tienes un bien")
        else: 
            if promedio<6 and promedio>=5:
                print("Por lo pelos, tu media es de " +str(promedio)+ ", por lo que tienes un suficiente, hay que mejorar.")
            else:
                if promedio<5 and promedio>=0:
                    print("Desgraciadamente estás suspenso, tu media es de " +str(promedio))       
                else:
                    print("Media erronea, revisa las notas y asegurate que son entre 0 y 10")