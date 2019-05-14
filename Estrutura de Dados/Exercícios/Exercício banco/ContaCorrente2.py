class ContaCorrente:
    def __init__(self, nome, cc, saldo = 0):
        self._nome = nome
        self._cc = cc
        self._saldo = saldo

    def __str__(self):
        return "Nome: {}\nConta-corrente: {}\nSaldo: {}\n".format(self._nome, self._cc, self._saldo)

    def getNome(self):
        return self._nome

    def getCc(self):
        return self._cc

    def getSaldo(self):
        return self._saldo

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