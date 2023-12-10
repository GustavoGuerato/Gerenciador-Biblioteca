class Pessoa:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

    def verifica_cpf(self):
        novo_cpf = self.cpf[:-2]
        reverso = 10
        total = 0

        for index in range(19):
            if index > 8:
                index -= 9

            total += int(novo_cpf[index]) * reverso
            reverso -= 1

            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                novo_cpf += str(d)

        sequencia = novo_cpf == str(novo_cpf[0]) * len(self.cpf)

        if self.cpf == novo_cpf and not sequencia:
            print('Válido')
        else:
            print('Inválido')

    def mostra_info(self):
        print(f'seu CPF é {self.cpf}')
        print(f'Seu Nome é {self.nome}')
        print(f'seu endereço é {self.endereco}')
    