class Personaje:
   
   def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
      self.__nombre= nombre
      self.__fuerza= fuerza
      self.__inteligencia= inteligencia
      self.__defensa= defensa
      self.__vida= vida
      #¿Qué es el metodo init? es el contructor de la clase que define los valores iniciales de los atributos del objeto
      #El signo de igual(=) es una asignaciòn
      #Porque tiene (__) el init= porque es un metodo magico 
      #Cuando se ejecuta init= cuando se crea un nuevo objeto
      #Para que sirve self= es una referencia al propio objeto
   def atributos(self):
      print(self.__nombre)
      print("-Fuerza:", self.__fuerza)
      print("-Inteligencia:", self.__inteligencia)
      print("-Defensa:", self.__defensa)
      print("-Vida:", self.__vida)
   def subir_nivel(self, fuerza, inteligencia, defensa):
      self.__fuerza += fuerza
      self.__inteligencia += inteligencia
      self.__defensa += defensa
   
   def esta_vivo(self):
      return self.__vida > 0 
   
   def __morir(self):
      self.__vida = 0
      print(self.__nombre, "ha muerto")
      
   def dañar(self, enemigo):
      return self.__fuerza - enemigo.__defensa if self.__fuerza > enemigo.__defensa else 0

   def atacar(self, enemigo):
      daño = self.dañar(enemigo)
      enemigo.__vida = enemigo.__vida - daño
      print(self.__nombre, "ha realizado ", daño, " puntos de daño a", enemigo.__nombre)
      if not enemigo.esta_vivo():
         enemigo.__morir()
      print("Vida de ",enemigo.__nombre, " es", enemigo.__vida)
      
   def get_fuerza(self):
      return self.__fuerza
   
   def set_fuerza(self,fuerza):
      if fuerza < 0:
         print("Error, has puesto un valor negativo")
      else:
         self.__fuerza = fuerza
      

      
#Variable del constructor de la clase
mi_personaje = Personaj