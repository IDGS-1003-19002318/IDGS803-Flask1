class Compra:
    precio = 12
    
    def __init__(self,precio):
        self.precio = precio
        
    def compraB(self,boletos):
        return boletos * self.precio
   
    

#if __name__ == '__main__':
#    Compra()
        