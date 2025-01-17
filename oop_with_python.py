class Personaje:
    def __init__(self,nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self):
        print(self.nombre)
        print("-Fuerza:",self.fuerza)
        print("-Inteligencia:",self.inteligencia)
        print("-Defensa:",self.defensa)
        print("-Vida:",self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa    
    
    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    #Daño que recibe nuestro personaje
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa    
        
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()   

#Creando clase "Guerrero" que hereda de su clase padre "Personaje"
class Guerrero(Personaje):
    #Para agregar un atributo más como "Espada", se sobreescribe el constructor
    def __init__(self,nombre, fuerza, inteligencia, defensa, vida, espada):
        #Personaje.__init__(self,nombre, fuerza, inteligencia, defensa, vida)
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        
    #Pedirle al usuario que escoja un arma   
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Lanza, daño 8. (2) Espada de acero, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")
            
    #Sobreescribir el método para imprimir el valor de espada
    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)
    
    #Sobreescribir el método daño para ajustar su valor respecto al uso de la espada    
    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
class Mago(Personaje):

    #Para agregar un atributo más como "libro", se sobreescribe el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    #Sobreescribir el método para imprimir el valor del libro
    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

    #Sobreescribir el método daño para ajustar su valor respecto al uso del libro
    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa    

#Creando el objeto guerrero
#ragnar = Guerrero()
# jackson = Personaje("Michael Jackson",20,15,10,100)
# ragnar = Guerrero("Ragnar Lothbrok",20,15,10,100,5)
# merlin = Mago("Merlin", 20,15,10,100,5)
#Imprimir atributos 
# jackson.atributos()
# ragnar.atributos()
# merlin.atributos()

#Ataques 
# jackson.atacar(ragnar)
# ragnar.atacar(merlin)
# merlin.atacar(jackson)

#Imprimir atributos después del ataque  
# jackson.atributos()
# ragnar.atributos()
# merlin.atributos()

ragnar = Guerrero("Ragnar Lothbrok",20,10,4,100,4)
merlin = Mago("Merlin", 5,15,4,100,3)

def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre,":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre,":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")                     

# combate(ragnar,merlin)

#ARREGLOS DE OBJETOS

# Crear un arreglo (lista) con diferentes personajes
personajes = [
    Guerrero("Ragnar Lothbrok", 20, 10, 4, 100, 4),
    Mago("Merlin", 5, 15, 4, 100, 3),
    Personaje("Lancelot", 15, 5, 8, 80)
]

# Mostrar atributos de todos los personajes en el arreglo
print("\nAtributos de los personajes en el arreglo:")
for p in personajes:
    p.atributos()

#Agregar un elemento al arreglo
personajes.append(Mago("Houdini", 15, 15, 4, 100, 3))

#Quitar un elemento del arreglo
personajes.pop(0)
print("\nAtributos de los personajes en el arreglo:")
for p in personajes:
    p.atributos()
    
# Calcular la suma total de fuerza
fuerza_total = sum(p.fuerza for p in personajes)
print(f"La fuerza total de los personajes es: {fuerza_total}")    

#Objetos que contienen arreglos