"""A04 — complete a lógica e os callbacks do sistema escolar."""
import tkinter as tk
from tkinter import ttk


def calcular(campos, registro):
    # TODO: normalizar nome/turma e recusar texto vazio.
    nome = campos["nome"].strip()
    turma = campos["turma"].strip()
    if not nome or not turma:
        return "Nome e turma são obrigatórios."

    # TODO: conferir a presença de exatamente cinco notas.
    notas_texto = campos["notas"]
    if len(notas_texto) != 5:
        return "Deve haver exatamente cinco notas."

    # TODO: converter cada texto, validar de 0 a 10 e criar uma nova lista.
    notas = []
    for texto in notas_texto:
        try:
            nota = float(texto)
            if not (0 <= nota <= 10):
                return f"Nota inválida: {nota}. Deve estar entre 0 e 10."
            notas.append(nota)
        except ValueError:
            return f"Formato inválido para nota: {texto}."

    # TODO: calcular a média com sum e len.
    media = sum(notas) / len(notas)

    # TODO: confirmar nome, turma, notas e média somente após validar tudo.
    registro["nome"] = nome
    registro["turma"] = turma
    registro["notas"] = notas
    registro["media"] = media

    return "Cálculo realizado com sucesso."


def exibir(registro):
    # TODO: tratar ausência; consultar apenas o último registro confirmado.
    if not registro:
        return "Nenhum registro confirmado nesta sessão."
    # TODO: mostrar identificação e cinco notas usadas, com média em uma casa.
    return f"Nome: {registro['nome']}, Turma: {registro['turma']}, Notas: {', '.join(f'{nota:.1f}' for nota in registro['notas'])}, Média: {registro['media']:.1f}"


def limpar(campos):
    # TODO: esvaziar nome, turma e os cinco textos de notas.
    # O registro confirmado não é recebido por esta função.
    campos["nome"] = ""
    campos["turma"] = ""
    campos["notas"] = ["", "", "", "", ""]


    


def criar_janela():
    janela = tk.Tk()
    janela.title("Sistema escolar fictício — A04")
    janela.columnconfigure(1, weight=1)
    campos = {"nome": "", "turma": "", "notas": ["", "", "", "", ""]}
    registro = {}

    ttk.Label(janela, text="Dados fictícios. Cinco notas de 0 a 10; média simples.", wraplength=440).grid(row=0, column=0, columnspan=2, padx=12, pady=8, sticky="w")
    ttk.Label(janela, text="Nome fictício:").grid(row=1, column=0, padx=12, pady=4, sticky="w")
    entrada_nome = ttk.Entry(janela)
    entrada_nome.grid(row=1, column=1, padx=12, pady=4, sticky="ew")
    ttk.Label(janela, text="Turma fictícia:").grid(row=2, column=0, padx=12, pady=4, sticky="w")
    entrada_turma = ttk.Entry(janela)
    entrada_turma.grid(row=2, column=1, padx=12, pady=4, sticky="ew")
    entradas_notas = []
    for numero in range(1, 6):
        ttk.Label(janela, text=f"Nota {numero} (0 a 10):").grid(row=numero+2, column=0, padx=12, pady=4, sticky="w")
        entrada = ttk.Entry(janela)
        entrada.grid(row=numero+2, column=1, padx=12, pady=4, sticky="ew")
        entradas_notas.append(entrada)

    def ao_calcular():
        # TODO: ler identificação e reunir os cinco textos de Entry numa lista.
        
        # TODO: chamar calcular e atualizar mensagem/consulta ao último válido. 
        nome = entrada_nome.get().strip()
        turma = entrada_turma.get().strip()
        mensagem = calcular(campos, registro)
        resultado.configure(text=mensagem)
        notas_texto = [entrada.get().strip() for entrada in entradas_notas]
        campos["nome"] = nome
        campos["turma"] = turma
        campos["notas"] = notas_texto

    def ao_exibir():
        # TODO: consultar somente registro; não ler os Entry em edição.
        mensagem = exibir(registro)
        resultado.configure(text=mensagem)
        aviso.configure(text="Complete o callback Exibir.")

    def ao_limpar():
        # TODO: limpar campos e os sete Entry; devolver foco ao nome.
        # TODO: preservar registro e painel do último válido.
        limpar(campos)
        entrada_nome.delete(0, tk.END)
        entrada_turma.delete(0, tk.END)
        for entrada in entradas_notas:
            entrada.delete(0, tk.END)
        aviso.configure(text="Complete o callback Limpar campos.")

    ttk.Button(janela, text="Calcular média", command=ao_calcular).grid(row=8, column=0, padx=12, pady=6)
    ttk.Button(janela, text="Exibir", command=ao_exibir).grid(row=8, column=1, padx=12, pady=6)
    ttk.Button(janela, text="Limpar campos", command=ao_limpar).grid(row=9, column=0, columnspan=2, pady=4)
    aviso = ttk.Label(janela, text="Preencha nome, turma e as cinco notas fictícias.", wraplength=440)
    aviso.grid(row=10, column=0, columnspan=2, padx=12, pady=6, sticky="w")
    resultado = ttk.Label(janela, wraplength=440)
    resultado.grid(row=11, column=0, columnspan=2, padx=12, pady=6, sticky="w")
    entrada_nome.focus_set()
    return janela


if __name__ == "__main__":
    criar_janela().mainloop()

