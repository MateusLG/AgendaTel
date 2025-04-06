# interface_estruturada.py

import tkinter as tk
from tkinter import messagebox
import agenda_estruturada as agenda

class AgendaAppEstruturada:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Telefônica (Estruturada)")

        self.nome_label = tk.Label(root, text="Nome:")
        self.nome_label.grid(row=0, column=0)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=0, column=1)

        self.telefone_label = tk.Label(root, text="Telefone:")
        self.telefone_label.grid(row=1, column=0)
        self.telefone_entry = tk.Entry(root)
        self.telefone_entry.grid(row=1, column=1)

        self.adicionar_button = tk.Button(root, text="Adicionar Contato", command=self.adicionar_contato)
        self.adicionar_button.grid(row=2, column=0, columnspan=2)

        self.lista_label = tk.Label(root, text="Contatos:")
        self.lista_label.grid(row=3, column=0)

        self.lista_contatos = tk.Listbox(root, width=50, height=10)
        self.lista_contatos.grid(row=4, column=0, columnspan=2)

        self.busca_label = tk.Label(root, text="Buscar Contato:")
        self.busca_label.grid(row=5, column=0)
        self.busca_entry = tk.Entry(root)
        self.busca_entry.grid(row=5, column=1)
        self.busca_button = tk.Button(root, text="Buscar", command=self.buscar_contato)
        self.busca_button.grid(row=6, column=0, columnspan=2)

        self.remover_button = tk.Button(root, text="Remover Contato Selecionado", command=self.remover_contato_selecionado)
        self.remover_button.grid(row=7, column=0, columnspan=2)

        self.atualizar_lista()

    def adicionar_contato(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        if nome and telefone:
            sucesso = agenda.adicionar_contato(nome, telefone)
            if sucesso:
                self.nome_entry.delete(0, tk.END)
                self.telefone_entry.delete(0, tk.END)
                self.atualizar_lista()
            else:
                messagebox.showerror("Contato Duplicado", "Nome ou telefone já existe na agenda.")
        else:
            messagebox.showwarning("Campos Inválidos", "Preencha todos os campos.")

    def buscar_contato(self):
        nome = self.busca_entry.get()
        if nome:
            contato = agenda.buscar_contato(nome)
            if contato:
                messagebox.showinfo("Contato Encontrado", f"{contato['nome']} - {contato['telefone']}")
            else:
                messagebox.showwarning("Não Encontrado", f"{nome} não está na agenda.")
        else:
            messagebox.showwarning("Campo Vazio", "Digite um nome para buscar.")

    def remover_contato_selecionado(self):
        selecionado = self.lista_contatos.curselection()
        if not selecionado:
            messagebox.showwarning("Nenhum selecionado", "Selecione um contato da lista para remover.")
            return

        contato_str = self.lista_contatos.get(selecionado[0])
        nome = contato_str.split(" - ")[0]

        confirmado = messagebox.askyesno("Confirmar Remoção", f"Remover {nome}?")
        if confirmado:
            sucesso = agenda.remover_contato(nome)
            if sucesso:
                self.atualizar_lista()
                messagebox.showinfo("Removido", f"{nome} foi removido.")
            else:
                messagebox.showerror("Erro", "Contato não encontrado para remoção.")

    def atualizar_lista(self):
        self.lista_contatos.delete(0, tk.END)
        for contato in agenda.listar_contatos():
            self.lista_contatos.insert(tk.END, f"{contato['nome']} - {contato['telefone']}")

