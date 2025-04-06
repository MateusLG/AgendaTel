class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __repr__(self):
        return f"{self.nome} - {self.telefone}"


class AgendaTelefonica:
    def __init__(self, tamanho=10):
        self.tabela_hash = [[] for _ in range(tamanho)]
        self.tamanho = tamanho

    def _hash(self, nome):
        return hash(nome) % self.tamanho

    def adicionar_contato(self, nome, telefone):
        indice = self._hash(nome)
        novo_contato = Contato(nome, telefone)
        self.tabela_hash[indice].append(novo_contato)

    def listar_todos_contatos(self):
        contatos = []
        for bucket in self.tabela_hash:
            for contato in bucket:
                contatos.append(contato)
        return contatos


def ordenar_contatos_por_nome(contatos):
    return sorted(contatos, key=lambda contato: contato.nome)


def busca_binaria(contatos_ordenados, nome_busca):
    esquerda = 0
    direita = len(contatos_ordenados) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        nome_meio = contatos_ordenados[meio].nome

        if nome_meio == nome_busca:
            return contatos_ordenados[meio]
        elif nome_meio < nome_busca:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return None


# Exemplo de interação no terminal
if __name__ == "__main__":
    agenda = AgendaTelefonica()

    while True:
        print("\n--- Agenda Telefônica ---")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Listar todos os contatos")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
            print(f"Contato de {nome} adicionado com sucesso!")

        elif escolha == "2":
            nome_busca = input("Digite o nome do contato a ser buscado: ")
            todos_contatos = agenda.listar_todos_contatos()
            contatos_ordenados = ordenar_contatos_por_nome(todos_contatos)
            resultado = busca_binaria(contatos_ordenados, nome_busca)

            if resultado:
                print(f"Contato encontrado: {resultado.nome} - {resultado.telefone}")
            else:
                print(f"Contato '{nome_busca}' não encontrado.")

        elif escolha == "3":
            todos_contatos = agenda.listar_todos_contatos()
            contatos_ordenados = ordenar_contatos_por_nome(todos_contatos)
            print("\nContatos na agenda:")
            for contato in contatos_ordenados:
                print(contato)

        elif escolha == "4":
            print("Saindo da agenda...")
            break

        else:
            print("Opção inválida. Tente novamente.")

