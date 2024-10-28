import tkinter as tk
import random
from PIL import Image, ImageTk

def resultado(jogador):
    escolhas = ["Pedra", "Papel", "Tesoura"]
    pc_escolha = random.choice(escolhas)

    label_computador.config(text=f"PC escolheu: {pc_escolha}")
    
    if jogador == pc_escolha:
        resultado_texto = "Empatou!"
    elif (jogador == "Pedra" and pc_escolha == "Tesoura") or \
         (jogador == "Papel" and pc_escolha == "Pedra") or \
         (jogador == "Tesoura" and pc_escolha == "Papel"):
        resultado_texto = "Você ganhou!"
    else:
        resultado_texto = "Você perdeu :("

    label_resultado.config(text=resultado_texto)

janela = tk.Tk()
janela.title("Pedra, papel e tesoura game!")

label_instrucoes = tk.Label(janela, text="Escolha uma opção", fg="blue", bg="lightgray", font=("Helvetica", 16))
label_instrucoes.pack()

tamanho_imagem = (50, 50)
imagem_pedra = ImageTk.PhotoImage(Image.open("pedra.png").resize(tamanho_imagem, Image.LANCZOS))
imagem_papel = ImageTk.PhotoImage(Image.open("papel.png").resize(tamanho_imagem, Image.LANCZOS))
imagem_tesoura = ImageTk.PhotoImage(Image.open("tesoura.png").resize(tamanho_imagem, Image.LANCZOS))

janela.imagem_pedra = imagem_pedra
janela.imagem_papel = imagem_papel
janela.imagem_tesoura = imagem_tesoura

botao_pedra = tk.Button(janela, image=imagem_pedra, command=lambda: resultado("Pedra"))
botao_pedra.pack(side=tk.LEFT, padx=10, pady=10)

botao_papel = tk.Button(janela, image=imagem_papel, command=lambda: resultado("Papel"))
botao_papel.pack(side=tk.LEFT, padx=10, pady=10)

botao_tesoura = tk.Button(janela, image=imagem_tesoura, command=lambda: resultado("Tesoura"))
botao_tesoura.pack(side=tk.LEFT, padx=10, pady=10)

label_computador = tk.Label(janela, text="PC escolheu:", font=("Courier", 14), bg="lightblue")
label_computador.pack(pady=10)

label_resultado = tk.Label(janela, text="Resultado:", font=("Arial", 18), fg="green")
label_resultado.pack(pady=10)

janela.mainloop()
