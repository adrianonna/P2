class ContaCorrente:
    def __init__(self, cliente, cc, ag, saldo = 0):
        self._cliente = cliente
        self._cc = cc
        self._ag = ag
        self._saldo = saldo

    def __str__(self):
        return "Cliente: {}\nAgência: {}\nConta-corrente: {}\nSaldo: {}".format( self._cliente, self._ag, self._cc, self._saldo)

    def getCc(self):
        return self._cc

    def getAg(self):
        return self._ag

    def getSaldo(self):
        return self._saldo

    def getCliente(self):
        return self._cliente

    def Depositar(self, deposito):
        self._saldo += deposito

    def Transferir(self, transferencia):
        self._saldo += transferencia

    def Sacar(self, saque):
        # total = self.__saldo - saque
        # if total > 0:
        #     self.__saldo -= saque
        #     return True
        # else:
        #     return False
        if self._saldo >= saque:
            self._saldo -= saque
            return True
        return False