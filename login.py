from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox


# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

#criando janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.config(bg=co1)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo janela

frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')# janela,largura, altura e estilo
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW) # linha, coluna,

frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW)

# Configurando freme cima / label
l_log = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_log.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)


credenciais = ['joao', '123456789']

# verificar login
def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome =='admin' and senha =='admin':
        messagebox.showinfo('Login', 'Seja bem vindo (a) Admin !!!')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo ' + credenciais[0])

        # deletar itens presente no frame
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()
        nova_janela()
    else:
        messagebox.showwarning('ERRO', 'Verifique seu nome ou senha')

#
def nova_janela():
    l_nome = Label(frame_cima, text='Usuario: '+credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text='Seja Bem Vindo(a) ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)

# frame baixo
l_nome = Label(frame_baixo, text='Nome *', anchor=NE, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text='Senha *', anchor=NE, font=('Ivy 10'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, show='*', justify='left', font=("", 15), highlightthickness=1, relief='solid') #show rsconde a senha
e_pass.place(x=14, y=130)

b_confirmar = Button(frame_baixo, command=verificar_senha, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)


janela.mainloop()