class Personaje:
    def __init__(self,nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        
    def atributos(self):
        print(self.__nombre)
        print("-Fuerza:",self.__fuerza)
        print("-Inteligencia:",self.__inteligencia)
        print("-Defensa:",self.__defensa)
        print("-Vida:",self.__vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa    
    
    def esta_vivo(self):
        return self.__vida > 0

    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
        
    #Daño que recibe nuestro personaje
    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa    
        
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.__morir()  
            
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self,fuerza):
        if fuerza<0:
            print("Error, has introducido un valor negativo")
        else:
            self.__fuerza = fuerza    
        
#Encapsulación
#Prueba 1. Sin acceso a mi_personaje.fuerza
mi_personaje = Personaje("Bruno Mars",160, 1, 40, 100)
mi_enemigo = Personaje("Michael Jackson", 60, 5, 50, 100)
#print(mi_personaje.fuerza) #AttributeError: 'Personaje' object has no attribute 'fuerza'
#Prueba 2. Sin acceso a mi_personaje.__fuerza (aún con el doble guión bajo)
#print(mi_personaje.__fuerza) #AttributeError: 'Personaje' object has no attribute '__fuerza'
#Prueba 3. Tampoco se pueden modificar valores
#mi_personaje.fuerza = 0
#mi_personaje.atributos() #No marca error, pero tampoco cambia el valor
#Los métodos, al ser funciones dentro de la clase, sí tienen acceso a los atributos. Por eso sí se pueden ver las estadísticas
#Queremos que el método morir solo se ejecute siendo llamado por el método atacar. 
#Entonces se le pone el doble guión bajo en su definición y en su llamado en el método atacar.
#Prueba 4. Sin acceso a mi_personaje.morir()
#mi_personaje.morir() #AttributeError: 'Personaje' object has no attribute 'morir'
#Prueba 5. Sin acceso a mi_personaje.__morir()
#mi_personaje.__morir() #AttributeError: 'Personaje' object has no attribute '__morir'
#Si se intenta ejecutar morir() desde atacar, sí funcionará.
#Prueba 6. Acceder a morir() ejecutando atacar()
#mi_personaje.atacar(mi_enemigo)
#Prueba 7. Usando getters y setters 
#print(mi_personaje.get_fuerza())
#mi_personaje.set_fuerza(-5)
#mi_personaje.atributos()
#Prueba 8. Evitando "setear" valores negativos agregando un if en set_fuerza
#Prueba 9. Python solo simula modificadores de acceso. Realmente todos los atributos son públicos
#print(mi_personaje._Personaje__fuerza)
# mi_personaje.atributos()
# mi_personaje._Personaje__fuerza = -5
# mi_personaje.atributos()
mi_personaje._Personaje__morir()
