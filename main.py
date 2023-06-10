# Fazendo importações:
from googletrans import Translator
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyperclip

# Cores
cor1 = "#3b3b3b"  # preto/black
cor2 = '#feffff'  # branco
cor3 = '#38576b'  # azul_fosco
cor4 = '#05142b'  # Azul_escuro
cor5 = '#175dcf'  # azul_claro

# Começando a janela

janela = Tk()
janela.title('JB Tradutor')
janela.geometry('300x300')
janela.resizable(False, False)


# Função do programa:
def centralizar_janela():
    largura_janela = janela.winfo_reqwidth()
    altura_janela = janela.winfo_reqheight()
    posicao_x = int((janela.winfo_screenwidth() / 2) - (largura_janela / 2))
    posicao_y = int((janela.winfo_screenheight() / 2) - (altura_janela / 2))
    janela.geometry(f"+{posicao_x-70}-{posicao_y-50}")


def traducao():
    tranlater = Translator()
    idioma_entrada = str(idioma_de_origem.get())
    idioma_saida = str(idioma_de_destino.get())
    frase_para_traduir = str(texto_para_traduzir.get())

    texto_traduzido = tranlater.translate(frase_para_traduir, src=idioma_entrada, dest=idioma_saida)
    resultado.configure(text=texto_traduzido.text)


def copiar():
    texto_copia = resultado.cget('text')
    pyperclip.copy(texto_copia)
    messagebox.showinfo("Copiado!", "O texto traduzido foi copiado com sucesso para a sua área de tranferência.")


# chamando função para centralizar janela
centralizar_janela()

# Divisão da tela
frame_escolha = Frame(janela, width=300, height=100, bg=cor4)
frame_escolha.grid(row=0, column=0)

frame_texto = Frame(janela, width=300, height=200, bg=cor1)
frame_texto.grid(row=1, column=0)

# Criando os campos de escolhas no label de frames_de_escolhas
linguas = ['en', 'pt', 'fr', 'de', 'it', 'ja', 'ru', 'es']

# Titulo do programa
titulo = Label(frame_escolha, text='TRADUTO DE TEXTOS', height=20, width=20, pady=10, relief='flat', anchor=NW,
               font='Arial 10 bold', bg=cor4, fg=cor2)
titulo.place(x=80, y=0)

# Primeira linha de escolha
escolha_texto_de = Label(frame_escolha, text='De:', height=4, width=8, pady=7, relief="flat", anchor=NW,font='Ivy 10 bold', bg=cor4, fg=cor2)
escolha_texto_de.place(x=50, y=40)
# Criando um icone de escolhas para add valores de varios idiomas
idioma_de_origem = ttk.Combobox(frame_escolha, height=4, width=4, justify=CENTER, font='Ivy 10 bold')
idioma_de_origem['values'] = linguas
idioma_de_origem.place(x=80, y=45)

escolha_texto_para = Label(frame_escolha, text='Para:', height=4, width=8, pady=7, relief="flat", anchor=NW,font='Ivy 10 bold', bg=cor4, fg=cor2)
escolha_texto_para.place(x=150, y=40)
idioma_de_destino = ttk.Combobox(frame_escolha, height=4, width=4, justify=CENTER, font='Ivy 10 bold')
idioma_de_destino['values'] = linguas
idioma_de_destino.place(x=200, y=45)

# Campo para adicionar textos:

msg = Label(frame_texto, text='Frase que deseja traduzir:', height=4, width=50, pady=7, relief='flat', anchor=NW,font='Ivy 10 bold', bg=cor1, fg=cor2)
msg.place(x=0, y=0)
texto_para_traduzir = Entry(frame_texto, width=20, font='Ivy 12', relief=SOLID)
texto_para_traduzir.place(x=10, y=30, height=50)

msg_final = Label(frame_texto, text='Tradução:', height=4, width=10, pady=7, relief='flat', anchor=NW,font='Ivy 10 bold', bg=cor1, fg=cor2)
msg_final.place(x=0, y=100)
resultado = Label(frame_texto, text='', width=15, height=2, pady=7, relief="solid", anchor=CENTER, font='Ivy 15 bold',bg=cor2, fg=cor1)
resultado.place(x=10, y=130)

# botões

botao_taduzir = Button(frame_texto, text='Traduzir', command=traducao, width=5, padx=5, height=0, bg=cor1, fg=cor2,
                       font='Ivy 12 bold', relief=RAISED, overrelief=RIDGE)
botao_taduzir.place(x=210, y=37)
botao_copiar = Button(frame_texto, text='Copiar', command=copiar, width=5, padx=5, height=0, bg=cor1, fg=cor2,
                      font='Ivy 12 bold', relief=RAISED, overrelief=RIDGE)
botao_copiar.place(x=210, y=140)

# loop da janela
janela.mainloop()
