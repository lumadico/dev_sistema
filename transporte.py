class Veiculo:
    # iniciar pelo método construtor
    def __init__(self, marca, modelo, cor, ano):
        self.__marca = marca     # os __ são para manter privados ao desenvolvedor
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano
        self.__cores = ['Branco', 'Preto', 'Cinza', 'Vermelho']

    def getMarca(self):     # pegando a marca do carro
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAno(self):
        return self.__ano
    
    def getCor(self):
        return self.__cor
    
    def setCor(self, novaCor):  
        controle = 0 # para mudar de cor -> nova cor
        for cor in self.__cores:
            if cor == novaCor:   
                controle = 1
                break     # para o 'for' - quebra o laço caso a cor escolhida esteja na lista de disponíveis 
        if controle == 1:
            self.__cor = novaCor
        else: 
            print('Cor não alterada')    
                

    def detalhes(self):
        print(f'Esse carro é da marca: {self.__marca}, do modelo: {self.__modelo}, da cor: {self.__cor} e de {self.__ano}') 
        # -> o 'f' no início permite chamar as chaves com variável, sem necessiade de colocar várias , pra mencionar no texto

    def acelerar(self):
        print('Acelerando um veículo aleatório')


class Carro(Veiculo):    # HERANÇA -> Carro é 'filho' de Veiculo

    def __init__(self, marca, modelo, cor, ano, portas):
        super().__init__(marca, modelo, cor, ano)   # faz a conexão com Veículo, 'chama' eles lá de cima 
        self.__portas = portas   # completando a classe Veiculo, esse exclusivo de Carro

    def getPortas(self):
        return self.__portas

    def acelerar(self):
        print(f'Andando de {self.getModelo()} por aí') # o self.__modelo não pega pq foi posto como privado no início, por isso o self.getModelo()



carro1 = Carro('BYD', 'Dolphin Mini', 'Cinza', 2025, 4)
carro2 = Carro('VW', 'Gol Bolinha', 'Cinza', 1998, 2)

carro1.detalhes()
carro1.acelerar()


