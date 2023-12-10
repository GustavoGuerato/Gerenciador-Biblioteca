class Pessoa:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

    def verifica_cpf(self):
        cpf = input("Digite o CPF: ")

        novo_cpf = cpf[:-2]
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

        sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

        if cpf == novo_cpf and not sequencia:
            print('Válido')
        else:
            print('Inválido')

    def endereco(self):
        rua = input('Digite o nome de sua rua: ')
        bairro = input('Digite o seu bairro: ')
        cidade = input('Digite sua cidade: ')

        endereco_completo = f' o seu endereço é{rua}, {bairro}, {cidade}'
        return endereco_completo


class Biblioteca:
    livros = []

    def __init__(self, titulo, data_devolucao=None):
        self.titulo = titulo
        self.data_devolucao = data_devolucao
        self.emprestado = False

    def adiciona_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print('A nossa biblioteca não tem nenhum livro no momento.')
        print('Livros disponiveis em nossa biblioteca: ')
        for livro in self.livros:
            if livro.esta_disponivel():
                print(f'{livro.titulo}está disponivel')

class Livro:

    def __init__(self, titulo, autor, data_devolucao=None):
        self.titulo = titulo
        self.autor = autor
        self.data_devolucao = data_devolucao
        self.emprestado = False

    def realizar_emprestimo(self):
        pass