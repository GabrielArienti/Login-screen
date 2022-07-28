from difflib import restore
from hashlib import new
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image


# cores
branco = "#fafafa"
preto = "#171717"
azul = "#110069"
entry = "#edebeb"

janela = Tk()
janela.title("Login")
janela.configure(bg=branco)
janela.geometry("300x280")
janela.resizable(width=FALSE, height=FALSE)

# Frames

frame_cima = Frame(janela, width=300, height=70, bg=branco)
frame_cima.grid(row=0, column=0)


frame_baixo = Frame(janela, width=300, height=210, bg=branco)
frame_baixo.grid(row=1, column=0)

credenciais = ['Admin', 'Adm123']


def nova_janela():

    img = Image.open('icon.png')
    img = img.resize((50, 50), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    icon = Label(frame_cima, image=img, pady=5, padx=2, bg=branco)
    icon.place(x=10, y=10)

    titulo = Label(frame_cima, text="Bem vindo!", font="Raleway 19 bold",
                   bg=branco, fg=preto, relief=FLAT)
    titulo.place(x=85, y=20)

    linha = Label(frame_cima, bg=azul, font="Raleway 1", width=400)
    linha.place(x=0, y=67)

    nome = Label(frame_baixo, text="Usuário conectado: Admin", font="Raleway 10",
                 bg=branco, fg=preto, relief=FLAT)
    nome.place(x=13, y=20)

    nome = Label(frame_baixo, text="""
    Relatório 1 - Escreva aqui coisas pertinentes
    para mostrar ao usuário conectado.
    
    Relatório 2 - Escreva aqui coisas pertinentes
    para mostrar ao usuário conectado   
    """, font="Raleway 10",
                 bg=branco, fg=preto, justify=LEFT, relief=FLAT)
    nome.place(x=1, y=40)


def entrar():
    nome = entry_nome.get()
    senha = entry_senha.get()

    if nome == 'Admin' and senha == 'Adm123':
        messagebox.showinfo('Login', 'Login efetuado com sucesso!')
        for widget in frame_cima.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        nova_janela()
    else:
        messagebox.showerror('Login', 'Usuário ou senha incorretos')


# Frame cima
img = Image.open('icon.png')
img = img.resize((50, 50), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

icon = Label(frame_cima, image=img, pady=5, padx=2, bg=branco)
icon.place(x=10, y=10)

titulo = Label(frame_cima, text="LOGIN", font="Raleway 19 bold",
               bg=branco, fg=preto, relief=FLAT)
titulo.place(x=75, y=20)

linha = Label(frame_cima, bg=azul, font="Raleway 1", width=400)
linha.place(x=0, y=67)

# Frame baixo

nome = Label(frame_baixo, text="Usuário*", font="Raleway 10",
             bg=branco, fg=preto, relief=FLAT)
nome.place(x=10, y=20)

entry_nome = Entry(frame_baixo, font="Raleway 10", width=30,
                   relief=FLAT, bg=entry, fg=preto)
entry_nome.place(x=12, y=50)

senha = Label(frame_baixo, text="Senha*", font="Raleway 10",
              bg=branco, fg=preto, relief=FLAT)
senha.place(x=10, y=90)

entry_senha = Entry(frame_baixo, font="Raleway 10", width=30,
                    relief=FLAT, bg=entry, fg=preto)
entry_senha.place(x=12, y=120)

botao_entrar = Button(frame_baixo, command=entrar, text="Entrar",
                      font="Raleway 14 bold", width=10, bg=azul, fg=branco, relief=FLAT, overrelief=RAISED)
botao_entrar.place(x=90, y=160)


janela.mainloop()
