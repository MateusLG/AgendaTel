import tkinter as tk
from tkinter import messagebox
from agenda import AgendaTelefonica  # Importando a lógica da agenda (certifique-se de que seu código esteja no arquivo agenda.py)

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Telefônica")

        # Instanciando a agenda telefônica
        self.agenda = AgendaTelefonica()

        # Adicionando campos para adicionar um novo contato
        self.nome_label = tk.Label(root, text="Nome:")
        self.nome_label.grid(row=0, column=0)

        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=0, column=1)

        self.telefone_label = tk.Label(root, text="Telefone:")
        self.telefone_label.grid(row=1, column=0)

        self.telefone_entry = tk.Entry(root)
        self.telefone_entry.grid(row=1, column=1)

        # Botão para adicionar o contato
        self.adicionar_button = tk.Button(root, text="Adicionar Contato", command=self.adicionar_contato)
        self.adicionar_button.grid(row=2, column=0, columnspan=2)

        # Lista para exibir os contatos
        self.lista_contatos_label = tk.Label(root, text="Contatos:")
        self.lista_contatos_label.grid(row=3, column=0)

        self.lista_contatos = tk.Listbox(root, width=50, height=10)
        self.lista_contatos.grid(row=4, column=0, columnspan=2)

        # Atualizar lista ao iniciar
        self.atualizar_lista()

        # Campo de busca
        self.busca_label = tk.Label(root, text="Buscar Contato:")
        self.busca_label.grid(row=5, column=0)

        self.busca_entry = tk.Entry(root)
        self.busca_entry.grid(row=5, column=1)

        self.busca_button = tk.Button(root, text="Buscar", command=self.buscar_contato)
        self.busca_button.grid(row=6, column=0, columnspan=2)

    def adicionar_contato(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()

        if nome and telefone:
            self.agenda.adicionar_contato(nome, telefone)
            self.nome_entry.delete(0, tk.END)
            self.telefone_entry.delete(0, tk.END)
            self.atualizar_lista()
        else:
            messagebox.showwarning("Campos Inválidos", "Por favor, preencha todos os campos.")

    def buscar_contato(self):
        nome = self.busca_entry.get()
        if nome:
            todos_contatos = self.agenda.listar_todos_contatos()
            contatos_ordenados = sorted(todos_contatos, key=lambda x: x.nome)
            contato_encontrado = self.agenda.buscar_contato(nome)

            if contato_encontrado:
                messagebox.showinfo("Contato Encontrado", f"{contato_encontrado.nome} - {contato_encontrado.telefone}")
            else:
                messagebox.showwarning("Contato Não Encontrado", f"O contato {nome} não foi encontrado.")
        else:
            messagebox.showwarning("Campo de Busca Vazio", "Digite o nome do contato para buscar.")

    def atualizar_lista(self):
        # Limpa a lista atual
        self.lista_contatos.delete(0, tk.END)
        # Obtém todos os contatos, ordena e exibe na lista
        todos_contatos = self.agenda.listar_todos_contatos()
        contatos_ordenados = sorted(todos_contatos, key=lambda x: x.nome)

        for contato in contatos_ordenados:
            self.lista_contatos.insert(tk.END, f"{contato.nome} - {contato.telefone}")

# Função principal para iniciar a interface
def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

