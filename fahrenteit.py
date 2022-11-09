print("Bienvenidos a mi conversor de Temperatura")

grados_fahrenheit = int(input("¿Grados Fahrenheit? "))
grados_celsius = (grados_fahrenheit - 32)* 5/9

print("El resultado es: {}".format(grados_celsius))
