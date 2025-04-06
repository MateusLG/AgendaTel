# agenda.py

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class AgendaTelefonica:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        # Verifica se o nome ou telefone já existem
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower() or contato.telefone == telefone:
                return False  # Duplicado
        self.contatos.append(Contato(nome, telefone))
        return True  # Adicionado com sucesso

    def listar_todos_contatos(self):
        return self.contatos

    def buscar_contato(self, nome):
        contatos_ordenados = sorted(self.contatos, key=lambda c: c.nome.lower())
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

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                self.contatos.remove(contato)
                return True
        return False

