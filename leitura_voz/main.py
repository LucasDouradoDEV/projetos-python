from tkinter import *
from playsound import playsound
from gtts import *
import os

root = Tk()
root.title('Conversor de texto em fala')
root.geometry('500x420')
root.maxsize(500, 420)
root.minsize(500, 420)
root.configure(bg='#1d1d1d')

def margem(altura):
    tela = Canvas(root,
                   width=500, 
                   height=altura,
                   bg='#1d1d1d',
                   bd=0,
                   highlightthickness=0,
                   relief='ridge')
    tela.pack()

def botao(texto, comando, padx):
    botao = Button(root,
                   text=texto,
                   padx=padx,
                   pady=20,
                   command=comando,
                   fg='#ffffff',
                   activeforeground='#ffffff',
                   bg='#C69749',
                   activebackground='#C69749',
                   relief=FLAT,
                   font=('8514oem',18,'bold')
                   )
    botao.pack()

def inicia():
    texto_inserido = e.get()
    fala = gTTS(text=texto_inserido,
                lang='pt',
                tld='com.br')
    arquivo_fala = 'arquivo_fala.mp3'
    fala.save(arquivo_fala)
    playsound(arquivo_fala)

def reseta():
    e.delete(0, END)
    os.remove('arquivo_fala.mp3')

margem(20)
titulo = Label(root, 
               bg='#1d1d1d', 
               fg='#ffffff', 
               font=('8514oem',18), 
               text="Conversor texto para fala")
titulo.pack()

margem(10)

insere_texto = Label(root, 
               bg='#1d1d1d', 
               fg='#ffffff', 
               font=('8514oem',18), 
               text="Insira o seu texto:")
insere_texto.pack()

margem(10)

e = Entry(root, 
          width=25, 
          borderwidth=4, 
          relief=FLAT,
          fg='#ffffff',
          bg='#000000',
          font=('8514oem',18, 'bold'),
          justify=CENTER)

e.pack()

margem(20)
botao_iniciar = botao('INICIAR',
                      inicia,
                      30)

margem(10)
botao_reset = botao('RESETAR',
                    reseta, 
                    30)
root.mainloop()