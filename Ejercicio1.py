#Ejercicios de Física Movimiento 

print("Este programa esta diseñado para realizar calculos de Física sobre el objetivo de MRU\n\nRecuerda que para que funcione las unidades correspondientes deben estar reflejadas de la siguiente forma:")
print("La velocidad en metros sobre segundos(m/sg)\nLa distancia en metros(m)\nEl tiempo en segundos(sg)\nSi no es tu caso, consulta las conversiones de las unidades y transformalas antes de introducir los datos")
variable = int(input('\nSeleccione la opción correcta según el caso:\n 1. Calcular la velocidad \n 2. Calcular la distancia \n 3. Calcular el tiempo\nIntroduce tu opción--->'))
#Declaramos las variables a utilizar

distancia = 0,
velocidad = 0,
tiempo = 0,

if(variable == 1):
    distancia = float(input("Ingrese el valor de la distancia: "));
    tiempo = float(input("Ingrese el valor del tiempo: "));
    resultado = distancia/tiempo;
    print(f"El resultado de la velocidad es: {resultado}m/sg")
elif(variable == 2):
    velocidad = float(input("Ingrese el valor de la velocidad: "));
    tiempo = float(input("Ingrese el valor del tiempo: "));
    resultado = velocidad*tiempo;
    print(f"El resultado de la velocidad es: {resultado}m")
elif(variable == 2):
    velocidad = float(input("Ingrese el valor de la velocidad: "));
    distancia = float(input("Ingrese el valor del distancia: "));
    resultado = distancia/velocidad;
    print(f"El resultado de la velocidad es: {resultado}sg")
else:
    print("La opción ingresada no es correcta")
    
#distancia = float(input("Ingrese el valor de a: "))
#velocidad = float(input("Ingrese el valor de b: "))
#tiempo = float(input("Ingrese el valor de c: "))

#Si el calculo es para velocidad