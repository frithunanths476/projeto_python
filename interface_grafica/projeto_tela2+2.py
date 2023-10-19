from Modulos import *
from BDTemp import *

def Clique():
    Nome = caixaTexto1.get()
    Quantidade = int(caixaTexto3.get())
    Preco = int (caixaTexto2.get())
    CadastrarBD(Nome,Quantidade,Preco)
    caixaTexto1.delete(0,"end")
    caixaTexto3.delete(0,"end")
    caixaTexto2.delete(0,"end")

def mostrar():
    totais=0
    for x in listaBD:
        totais += x.Total
    labelPreco.configure(text=f'Total gasto: R${totais:.2f}')
def registrar():
    labelConfirm.configure(text="Venda Registrada")

def Irnavegacao():
    pass

def Irlogin():
    pass

def Irgerenciamento():
    pass

Tk.set_appearance_mode("Dark")

janela = CriarJanela("Registro de Vendas","550x400+500+50",2)

# =====================(HEADER)==============

frame = CriarFrame(janela,0,0,800,50)
frame.configure(fg_color="black")
frame.grid(columnspan=13, sticky="N")

logo = CriarImagem(frame,"Logo.jpeg",0,0,50,50)

btnH_1 = CriarBotão(frame,"Navegação",Irnavegacao,0,10,10,10)
btnH_1.configure(fg_color="#4577B6", corner_radius=10)

btnH_2 = CriarBotão(frame,"Login",Irlogin,0,11,10,10)
btnH_2.configure(fg_color="#4577B6", corner_radius=10)

btnH_3 = CriarBotão(frame,"Gerenciamento de Estoque",Irgerenciamento,0,12,10,10)
btnH_3.configure(fg_color="#4577B6", corner_radius=10)

#======================(HEADER)=============

caixaTexto1 = CriarCaixaDeTexto(janela,220,30,3,10,"Insira o produto")
caixaTexto1.configure(fg_color="#51719B", border_color="#51719B", corner_radius=10)

caixaTexto3 = CriarCaixaDeTexto(janela,220,30,4,10,"Insira a quantidade")
caixaTexto3.configure(fg_color="#51719B", border_color="#51719B", corner_radius=10)

caixaTexto2 = CriarCaixaDeTexto(janela,220,30,5,10,"Insira o preço")
caixaTexto2.configure(fg_color="#51719B", border_color="#51719B", corner_radius=10)

btn1 = CriarBotão(janela,"Enviar",Clique,3,2,200,30)
btn1.configure(fg_color="#325899", corner_radius=15)

btn2 = CriarBotão(janela,"Total da Venda",mostrar,4,2,200,30)
btn2.configure(fg_color="#325899", corner_radius=15)
labelPreco = CriarLabel(janela," ",6,10)

btn3 = CriarBotão(janela,"Registrar Venda",registrar,5,2,200,30)
btn3.configure(fg_color="#325899", corner_radius=15)
labelConfirm = CriarLabel(janela," ",8,6)

janela.mainloop()