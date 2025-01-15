class Personaje:
   
   def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
      self.nombre= nombre
      self.fuerza= fuerza
      self.inteligencia= inteligencia
      self.defensa= defensa
      self.vida= vida
      #¿Qué es el metodo init? es el contructor de la clase que define los valores iniciales de los atributos del objeto
      #El signo de igual(=) es una asignaciòn
      #Porque tiene (__) el init= porque es un metodo magico 
      #Cuando se ejecuta init= cuando se crea un nuevo objeto
      #Para que sirve self= es una referencia al propio objeto
   def atributos(self):
      print(self.nombre)
      print("-Fuerza:", self.fuerza)
      print("-Inteligencia:", self.inteligencia)
      print("-Defensa:", self.defensa)
      print("-Vida:", self.vida)
   def subir_nivel(self, fuerza, inteligencia, defensa):
      self.fuerza += fuerza
      self.inteligencia += inteligencia
      self.defensa += defensa
   
   def esta_vivo(self):
      return self.vida > 0 
   
   def morir(self):
      self.vida = 0
      print(self.nombre, "ha muerto")
      
   def dañar(self, enemigo):
      return self.fuerza - enemigo.defensa

   def atacar(self, enemigo):
      daño = self.dañar(enemigo)
      enemigo.vida = enemigo.vida - daño
      print(self.nombre, "ha realizado ", daño, " puntos de daño a", enemigo.nombre)
      print("Vida de ",enemigo.nombre, " es", enemigo.vida)
   
#Creando clase "Guerrero" que hereda de su clase padre "Personaje"   
class Guerrero(Personaje):
   #Sobreescribir el constructor
   def __init__(self, nombre, fuerza, inteligencia, defensa, vida,espada):
      #Llamar a la clase padre
      super().__init__(nombre, fuerza, inteligencia, defensa, vida)
      self.espada = espada

hercule