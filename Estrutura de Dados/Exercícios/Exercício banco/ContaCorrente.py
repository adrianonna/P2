class Cliente:
    def __init__(self, nome, ag, cc, saldo):
        self.nome = nome
        self.ag = ag
        self.cc = cc
        self.saldo = saldo

    def __str__(self):
        return "Nome: {}\nAgencia: {}\nConta-corrente: {}\nSaldo: {}\n".format(self.nome,self.ag,self.cc,self.saldo)

    def Sacar(self, saque):
        self.saldo -= saque

    def Depositar(self, deposito):
        self.saldo += deposito

    def Transferir(self, transferencia):
        self. saldo -= transferencia


