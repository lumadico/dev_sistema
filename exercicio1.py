class Trasnporte:

    def __init__(self, capacidade, velocMax):   
        self.__capacidade = capacidade
        self.__velocMax = velocMax
        

    def getCapacidade(self):    # o self 'guarda' tudo, porém o return manda de volta o que vc quer (chamar)
        return self.__capacidade
    
    def getVelocMax(self):
        return self.__velocMax

    def descricao(self):
        print(f'A capacidade máxima é {self.__capacidade} e a velocidade é {self.__velocMax}')

    def mover(self):   # poderia ser sem o self pq é um print simples sem chamar niguém
        print('O transporte está em movimento')


class Onibus(Trasnporte):

    def __init__(self, capacidade, velocMax):
        super().__init__(capacidade, velocMax) 
        
    def mover(self):  
        print('O ônibus está seguindo sua rota')

class Bicicleta(Trasnporte):

    def __init__(self, capacidade, velocMax):
        super().__init__(capacidade, velocMax) 
        
    def mover(self):
        print('A bicicleta está sendo pedalada')
    

onibus1 = Onibus(50, '70 km/h')
bicicleta1 = Bicicleta(1, '30 km/h')

onibus1.descricao()
onibus1.mover()

bicicleta1.descricao()
bicicleta1.mover()