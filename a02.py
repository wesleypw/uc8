"""A02 — prática 2: complete a lógica e os callbacks."""
import tkinter as tk
from tkinter import ttk


def registrar(campos, registro):
    # TODO: ler e normalizar nome e sobrenome; recusar texto vazio.
    if campos["nome"] == "" or campos["sobrenome"] == "":
        return "Nome e sobrenome não podem ser vazios."
    # TODO: converter idade e validar inteiro maior que zero.
    if not campos["idade"].isdigit() or int(campos["idade"]) <= 0:
        return "Idade deve ser um número inteiro maior que zero."
    # TODO: atualizar registro somente depois de todas as validações.
    registro["nome"] = campos["nome"].strip().capitalize()
    registro["sobrenome"] = campos["sobrenome"].strip().capitalize()
    registro["idade"] = int(campos["idade"])
    return "Registro atualizado com sucesso."

def exibir(registro):
    # TODO: tratar a ausência de registro e consultar o último válido.
    if not registro:
        return "Nenhum cadastro registrado nesta sessão."
    return f"Nome: {registro['nome']}, Sobrenome: {registro['sobrenome']}, Idade: {registro['idade']}"

def limpar(campos):
    # TODO: esvaziar os três textos editáveis.
    # O registro confirmado é separado e não é recebido por esta função.
    campos.delete("nome")
    campos.delete("sobrenome")
    campos.delete("idade")
    

def criar_janela():
    janela = tk.Tk()
    janela.title("Cadastro em memória — A02")
    janela.columnconfigure(1, weight=1)
    campos = {"nome": "", "sobrenome": "", "idade": ""}
    registro = {}

    ttk.Label(janela, text="Nome fictício:").grid(row=0, column=0, padx=12, pady=6, sticky="w")
    entrada_nome = ttk.Entry(janela)
    entrada_nome.grid(row=0, column=1, padx=12, pady=6, sticky="ew")
    ttk.Label(janela, text="Sobrenome fictício:").grid(row=1, column=0, padx=12, pady=6, sticky="w")
    entrada_sobrenome = ttk.Entry(janela)
    entrada_sobrenome.grid(row=1, column=1, padx=12, pady=6, sticky="ew")
    ttk.Label(janela, text="Idade fictícia:").grid(row=2, column=0, padx=12, pady=6, sticky="w")
    entrada_idade = ttk.Entry(janela)
    entrada_idade.grid(row=2, column=1, padx=12, pady=6, sticky="ew")

    def ao_registrar():
        # TODO: copiar os textos atuais para campos e chamar registrar.
        campos["nome"] = entrada_nome.get()
        campos["sobrenome"] = entrada_sobrenome.get()
        campos["idade"] = entrada_idade.get()
        mensagem = registrar(campos, registro)
        # TODO: atualizar a mensagem e a consulta ao registro confirmado.
        resultado.configure(text=mensagem)
        aviso.configure(text="Complete o callback Registrar.")

    def ao_exibir():
        # TODO: consultar apenas registro; não ler os campos em edição.
        aviso.configure(text="Complete o callback Exibir.")

    def ao_limpar():
        # TODO: limpar campos e Entry; manter registro e consulta intactos.
        limpar(campos)
        entrada_nome.delete(0, tk.END)
        entrada_sobrenome.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        aviso.configure(text="Complete o callback Limpar campos.")

    ttk.Button(janela, text="Registrar", command=ao_registrar).grid(row=3, column=0, padx=12, pady=8)
    ttk.Button(janela, text="Exibir", command=ao_exibir).grid(row=3, column=1, padx=12, pady=8)
    ttk.Button(janela, text="Limpar campos", command=ao_limpar).grid(row=4, column=0, columnspan=2, pady=6)
    aviso = ttk.Label(janela, text="Preencha os dados fictícios e registre.", wraplength=390)
    aviso.grid(row=5, column=0, columnspan=2, padx=12, pady=8, sticky="w")
    resultado = ttk.Label(janela, text="Nenhum cadastro registrado nesta sessão.", wraplength=390)
    resultado.grid(row=6, column=0, columnspan=2, padx=12, pady=8, sticky="w")
    entrada_nome.focus_set()
    return janela


if __name__ == "__main__":
    criar_janela().mainloop()
