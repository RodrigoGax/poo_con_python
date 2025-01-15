class Personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
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
jackson = Personaje("Michael Jackson",20,15,10,100)
ragnar = Guerrero("Ragnar Lothbrok",20,15,10,100,5)
merlin = Mago("Merlin", 20,15,10,100,5)
#Imprimir atributos 
jackson.atributos()
ragnar.atributos()
merlin.atributos()
