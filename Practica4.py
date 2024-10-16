nombre= input('¿Cual es tu nombre?')
print(f"¡Hola {nombre}!") 

horas= int(input('¿Cuantas horas has trabajado'))
costo= int(input('¿Cuanto cuesta la hora?'))

print(f"La paga es de {horas*costo}")

edad2 = int(input("¿Cuantos años tienes?"))
if edad2>=18:
   print("Es usted mayor de edad")
elif edad2<0:
    print("No se puede tener una edad negativa")
else:
    print("Es usted menor de edad")


num1 = int(input("¿Introduce un numero como primer divisor"))
num2 = int(input("Introduce un numero"))

if num1/num2==0:
    print(f"ERROOOR")
print(f"El resultado de la dividion de {num1} entre {num2} es {num1/num2}")

conta= input("Escribe una contraseña")
conta2= input("Repite la contraseña")

if conta.lower()==conta2.lower():
    print("La contraseña si coincide")
else:
    print("La contraseña no coincide")
