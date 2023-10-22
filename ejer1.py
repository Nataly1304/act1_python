
#Cree una lista vacía  denominada aprendices y edades, llénelas solicitando los datos por teclado
aprendices=[]
edades=[]

for i in range(31):
    aprendiz=input("ingresa tu nobre: ") 
    edad=int(input("ingresa tu edad: "))
    
aprendices.append(aprendiz) # aca la funcion append nos sirve para agregar elementos 
edades.append(edad)

# Imprimir las listas
print("Lista de Aprendices:")
for lista in range(len(aprendices)):
    print(f"Nombre: {aprendices[lista]}, Edad: {edades[lista]}") 

# aprendiz con la mayor edad
aprendizMayorEdad = edades.index(max(edades))
print(f"Aprendiz con la mayor edad: {aprendices[aprendizMayorEdad]} ({max(edades)} años)")

# ingresar el nombre de la instructora en la posición 1
instructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, instructora) #la funcion insert es para insertar un elemento ej: el nombre de la instrutora

# Contar cuántos aprendices tienen 18 años
aprendices18Años = edades.count(18) # la funcion "count" nos permite contar los aprendices de 18 años 
print(f"Número de aprendices con 18 años: {aprendices18Años}")

# Agregar un aprendiz al final de la lista
aprendiz = input("Ingrese el nombre de un aprendiz X: ")
aprendices.append(aprendiz)

# Borrar el nombre de la instructora de la lista
if instructora in aprendices:
    aprendices.remove(instructora) #la  funcion "remove" es el que nos permite borar solo el 1 de la lista 

# Indicar un dato a buscar en la lista de aprendices
datoBuscar = input("Ingrese un nombre a buscar en la lista de aprendices: ")
if datoBuscar in aprendices:
    print(f"{datoBuscar} se encuentra en la lista de aprendices.")
else:
    print(f"{datoBuscar} no se encuentra en la lista de aprendices.")

# Mostrar los primeros 10 aprendices de la lista
print("Primeros 10 aprendices:")
for i in range(10):
    if i < len(aprendices): #la funcion "len" se utiliza para obtener la longitud o el número de elementos de un objeto iterable
        print(aprendices[i])

# Mostrar los 10 últimos aprendices de la lista
print("Últimos 10 aprendices:")
for i in range(len(aprendices) - 10, len(aprendices)): # len(aprendices) devuelve la longitud de la lista.
    if i >= 0: 
        print(aprendices[i])

#obtener del elemento 10 al elemento 20
print("Elementos del 10 al 20:")
for elemento in range(9, 19):
    if i < len(aprendices):
        print(aprendices[elemento])


