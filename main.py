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

    def atualizar_endereco(self):
        nova_rua = input('Digite o novo nome de sua rua: ')
        novo_bairro = input('Digite o novo bairro: ')
        nova_cidade = input('Digite a nova cidade: ')
        self.endereco = f'O novo endereço é {nova_rua}, {novo_bairro}, {nova_cidade}'


class Biblioteca:
    livros = []

    def __init__(self, titulo, data_devolucao=None):
        self.titulo = titulo
        self.data_devolucao = data_devolucao
        self.emprestado = False

    def adiciona_livro(self, livro):
        self.livros.append(livro)

    def verifica_disponibilidade(self, livro_titulo):
        for livro in self.livros:
            if livro_titulo == livro_titulo:
                if livro.esta_disponivel():
                    print(f'{livro.titulo} está disponivel')
                else:
                    print(f'{livro.titulo} não está disponivel')
                return
        print(f'O livro "{livro_titulo}" não está na biblioteca.')

    def listar_livros(self):
        if not self.livros:
            print('A nossa biblioteca não tem nenhum livro no momento.')
        print('Livros disponiveis em nossa biblioteca: ')
        for livro in self.livros:
            if livro.esta_disponivel():
                print(f'{livro.titulo}está disponivel')

    def remove_livros(self, livro):
        if livro in self.livros:
            print(f'O livro "{livro.titulo}" foi removido da biblioteca.')
        else:
            print(f'O livro "{livro.titulo}" não está na biblioteca.')


class Livro:

    def __init__(self, titulo, autor, data_devolucao=None):
        self.titulo = titulo
        self.autor = autor
        self.data_devolucao = data_devolucao
        self.emprestado = False

    def realizar_emprestimo(self):
        if not self.emprestado:
            self.emprestado = True
            print(f'O livro {self.titulo} foi emprestado com sucesso.')
        else:
            print(f'O livro {self.titulo} já foi emprestado para outra pessoa')

    def devolver_livro(self):
        if self.emprestado:
            self.emprestado = False
            print(f'O livro {self.titulo}Foi devolvido com sucesso.')
        else:
            print(f'{self.titulo}ainda não foi emprestado.')

    def renovar_emprestimo(self, nova_data_devolucao):
        if self.emprestado:
            self.data_devolucao = nova_data_devolucao
            print(f'O empréstimo do livro "{self.titulo}" foi renovado até {nova_data_devolucao}.')
        else:
            print(f'O livro "{self.titulo}" não está atualmente emprestado.')
