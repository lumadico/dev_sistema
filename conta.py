class Conta: 
    # Primeiro método: construtor
    def __init__(self, numConta, titular, saldo=0):   # o self guarda as infos das variáveis (conta1, conta2...), passando por elas uma por vez; autoreferencia
        self.numConta = numConta
        self.titular = titular
        self.saldo = saldo 
        inicio = 'Extrato de ' + self.titular + '\t' + str(self.saldo) + '\n'
        self.extrato = [inicio]
    
    def realizarDeposito(self, valor):
        if valor > 0:
            self.saldo += valor
            saida = 'Depósito realizado com sucesso no valor de: ' + str(valor)
            self.extrato.append(saida)
        else: 
            print('Insira um valor válido')

    def realizarSaque(self, valor):
        if self.saldo >= valor and valor > 0:
            self.saldo -= valor 
            saida = 'Saque realizado! Valor de: ' + str(valor)
        elif valor <= 0:
            print('Insira um valor válido')
        else:
            print('Saldo insuficiente') 

    def realizarTransferencia(self, destinatario, valor):
        saida = 'Transferencia para a conta ' + \
            destinatario.numConta + ' no valor de: R$ ' \
            + str(valor)
        self.realizarSaque(valor)
        destinatario.realizarDeposito(valor)
        saida += 'Fim da Transferencia'
        



conta1 = Conta('00001','Renan')
conta1.realizarDeposito(100)
conta1.realizarSaque(50)
conta2 = Conta('00002', 'Raphael', 2)

conta2.realizarTransferencia(conta1, 1.99)
print(conta2.saldo)