class Cafe():
    def que_soy(self):
        print("Soy un café")

class Te():
    def que_soy(self):
        print("Soy un Té")

def definicion_bebida(bebida):        
    bebida.que_soy()

#El método que_soy() recibirá múltiples formas. Todo depende del objeto que reciba.
definicion_bebida(Te())
        
