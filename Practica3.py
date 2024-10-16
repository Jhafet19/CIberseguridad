cad = "Python"
print(cad[3])
print(cad[1:4])
cad2="Veronica"
print(cad2[2:8:4])

nombre ="Pepe"
edad=25
print("¡Hola,", nombre, "!")
print(f"¡hola,{nombre}!")
#cadenas para darle formato a la impresion sin usar format()

print("Me llamo {} y tengo {} años.".format(nombre,edad))
print(f"Me llamo {nombre} y tengo {edad} años.")

color = input('¿Cual es tu color favorito?')
print(color)
age =input('¿CUal es tu edad?')
print(age)
name = input('¿Como te llamas?')
print(name.lower())
print(name.upper())
print(name.title())


numero =int(input("Escriba un numero positivo:"))
if numero<0:
    print("¡le he dicho que escriba un numero positivo")

print(f"Ha escritoe el numero {numero}")

edad = int(input('¿Cuanto años tienes?'))
if edad<18:
    print("Es usted menor de edad.")
else:
    print("Es usted mayor de edad")


edad2 = int(input("¿Cuantos años tienes?"))
if edad2>=18:
   print("Es usted mayor de edad")
elif edad2<0:
    print("No se puede tener una edad negativa")
else:
    print("Es usted menor de edad")
print("¡Hasta la proxima!")

