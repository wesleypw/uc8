"""A03 — complete as funções antes de conectá-las à janela."""
import tkinter as tk
from tkinter import ttk

def criar_janela():
    janela = tk.Tk()
    janela.title("Cadastro em memória — A02")
    janela.columnconfigure(1, weight=1)
    campos = {"nome": "", "sobrenome": "", "idade": ""}
    

    def ao_calcular(campos, registro):
        # TODO: ler reais e as duas cotações; aceitar vírgula ou ponto decimal.
        reais = float(campos["reais"].replace(",", "."))
        cotacao_dolar = float(campos["cotacao_dolar"].replace(",", "."))
        cotacao_euro = float(campos["cotacao_euro"].replace(",", "."))

        # TODO: tratar conversão inválida, reais negativos e cotações <= 0.
        if reais < 0:
            return "Erro: valor em reais é negativo."
        if cotacao_dolar <= 0 or cotacao_euro <= 0:
            return "Erro: cotações são inválidas."

        # TODO: dividir reais por cada cotação.
        registro["dolar"] = reais / cotacao_dolar
        registro["euro"] = reais / cotacao_euro

        # TODO: confirmar entradas e os dois resultados somente após validar tudo.
        if "dolar" not in registro or "euro" not in registro:
            return "Erro: conversão não realizada."

        return "Conversão realizada com sucesso."


    def ao_exibir(registro):
        # TODO: tratar ausência de conversão; consultar somente registro.
        if "dolar" not in registro or "euro" not in registro:
            return "Nenhuma conversão registrada nesta sessão."
        # TODO: mostrar entradas usadas e resultados, estes com duas casas.
        return f"Reais: {campos['reais']}, Dólar: {registro['dolar']:.2f}, Euro: {registro['euro']:.2f}"


    def ao_limpar(campos):
        # TODO: esvaziar os três campos; preservar registro e resultados.
        campos.clear("reais")
        campos.clear("cotacao_dolar")
        campos.clear("cotacao_euro")

    ttk.Label(janela, text="reais:").grid(row=0, column=0, padx=12, pady=6, sticky="w")
    entrada_reais = ttk.Entry(janela)
    entrada_reais.grid(row=0, column=1, padx=12, pady=6, sticky="ew")
    ttk.Label(janela, text="Cotação do dólar:").grid(row=1, column=0, padx=12, pady=6, sticky="w")
    entrada_cotacao_dolar = ttk.Entry(janela)
    entrada_cotacao_dolar.grid(row=1, column=1, padx=12, pady=6, sticky="ew")
    ttk.Label(janela, text="Cotação do euro:").grid(row=2, column=0, padx=12, pady=6, sticky="w")
    entrada_cotacao_euro = ttk.Entry(janela)
    entrada_cotacao_euro.grid(row=2, column=1, padx=12, pady=6, sticky="ew")

    ttk.Button(janela, text="Calcular", command=ao_calcular).grid(row=3, column=0, padx=12, pady=8)
    ttk.Button(janela, text="Exibir", command=ao_exibir).grid(row=3, column=1, padx=12, pady=8)
    ttk.Button(janela, text="Limpar campos", command=ao_limpar).grid(row=4, column=0, columnspan=2, pady=6)
    aviso = ttk.Label(janela, text="Preencha os dados fictícios e registre.", wraplength=390)
    aviso.grid(row=5, column=0, columnspan=2, padx=12, pady=8, sticky="w")
    resultado = ttk.Label(janela, text="Nenhum cadastro registrado nesta sessão.", wraplength=390)
    resultado.grid(row=6, column=0, columnspan=2, padx=12, pady=8, sticky="w")
    entrada_reais.focus_set()
    return janela

if __name__ == "__main__":
    criar_janela().mainloop()

    # Acrescente as outras sequências da matriz, prevendo antes de executar.
