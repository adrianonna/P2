class Cliente:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    def __str__(self):
        return "Nome: {}\nCPF: {}".format(self._nome, self._cpf)

    def getNome(self):
        return self._nome

    def getCPF(self):
        return self._cpf