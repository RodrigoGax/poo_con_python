class Personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
#Variable del constructor vacío de la clase
mi_personaje = Personaje()
#Modificando valores de atributos de la clase
mi_personaje.nombre = "Mr. Beast"
mi_personaje.fuerza = 100
#Imprimir variables concatenando texto y el valor de la variable
print("El nombre del jugador es", mi_personaje.nombre)
print("La fuerza del jugador es", mi_personaje.fuerza)