class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class AgendaTelefonica:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        self.contatos.append(Contato(nome, telefone))

    def listar_todos_contatos(self):
        return self.contatos

    def buscar_contato(self, nome):
        # Ordena os contatos antes de fazer a busca binária
        contatos_ordenados = sorted(self.contatos, key=lambda c: c.nome.lower())

        # Implementação de busca binária
        inicio = 0
        fim = len(contatos_ordenados) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            atual = contatos_ordenados[meio].nome.lower()

            if atual == nome.lower():
                return contatos_ordenados[meio]
            elif atual < nome.lower():
                inicio = meio + 1
            else:
                fim = meio - 1

        return None

