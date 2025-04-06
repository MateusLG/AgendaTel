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

    def buscar_contato_hash(self, nome):
        indice = self._hash(nome)
        for contato in self.tabela_hash[indice]:
            if contato.nome == nome:
                return contato
        return None

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


# Exemplo de uso
if __name__ == "__main__":
    agenda = AgendaTelefonica()

    # Adicionando contatos
    agenda.adicionar_contato("João", "12345")
    agenda.adicionar_contato("Maria", "67890")
    agenda.adicionar_contato("Ana", "11111")
    agenda.adicionar_contato("Carlos", "22222")

    # Listando e ordenando
    todos_contatos = agenda.listar_todos_contatos()
    contatos_ordenados = ordenar_contatos_por_nome(todos_contatos)

    # Exibindo contatos ordenados
    print("Contatos ordenados:")
    for contato in contatos_ordenados:
        print(contato)

    # Busca binária
    nome_procurado = "Maria"
    resultado = busca_binaria(contatos_ordenados, nome_procurado)

    if resultado:
        print(f"\nContato encontrado: {resultado.nome} - {resultado.telefone}")
    else:
        print(f"\nContato '{nome_procurado}' não encontrado.")

