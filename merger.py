import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog

merger = PyPDF2.PdfMerger()

def solicitar_arquivo(quant):
    x = 0
    while x < quant:
    # Criar uma instância da janela raiz oculta
        root = tk.Tk()
    # Ocultar a janela principal
        root.withdraw()
    
    # Abrir o gerenciador de arquivos e solicitar a seleção de um arquivo
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )
        if caminho_arquivo:
            # Adiciona o caminho do arquivo selecionado à lista do merger
            merger.append(caminho_arquivo)
            x += 1
        else:
            print("Nenhum arquivo selecionado. Tente novamente.")

quantidade_pdf = int(input("Quantos PDFs deseja mesclar?"))
solicitar_arquivo(quantidade_pdf)

merger.write("pdf_mesclado.pdf")
merger.close()
print("Seu PDF mesclado foi salvo no seguinte diretório: \n",os.getcwd())