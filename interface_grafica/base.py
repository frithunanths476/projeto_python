import customtkinter as Tk
from modulo import *

#def clique():
#    var = check1.get()
#    if var == 1:
#        label.configure(text="Marcado")
#    else:
#        label.configure(text="Desmarcado")

#janela = CriarJanelaP("Teste","400x350",1)
#label = CriarLabel(janela," ",3,6)
#check1 = CriarCheckBox(janela,"Marque",4,6)
#btn = CriarBotao(janela,"Clique-me",clique,50,30,5,6)

#janela.mainloop()

#-------------------------------(Switch)---------------------------------------

#janela = CriarJanelaP("Teste","400x350",1)
#switch = CriarSwitch(janela,"Marque",4,6)

#janela.mainloop()

#-----------------------------(ComboBox)--------------------------------------

#janela = CriarJanelaP("Teste","400x350",1)

#Lista = ["Item 1","Item 2","Item 3","Item 4"]
#combo = CriarComboBox(janela,Lista,200,30,4,6)

#janela.mainloop()

#-----------------------------(Progressbar)--------------------------------------

#janela = CriarJanelaP("Teste","400x350",1)

#progress = CriarProgressBar(janela,200,10,7,6)

#janela.mainloop()

#-----------------------------------(Slide)--------------------------------------

#janela = CriarJanelaP("Teste","400x350",1)

#slider = CriarSlider(janela,200,10,6,6)

#janela.mainloop()

#-----------------------------------(revisão)--------------------------------------

tk.set_appearance_mode("Light")

Tela1 = CriarJanelaP("Revisão","600x600+500+50",1)

#Criar Label
Lb_Tela1 = CriarLabel(Tela1,"Texto 1",1,6)
#Alterações
Lb_Tela1.configure(text_color="red", font=("arial",18,"bold"))

#Função botão
def clicar():
    Tela1.withdraw()
    Tela2.deiconify()

def alterarTema():
    T = Switch_Tela1.get()
    if T == 1:
        tk.set_appearance_mode("Dark")
    else:
        Tk.set_appearance_mode("Light")


#Criar botão
Btn_Tela1 = CriarBotao(Tela1,"Clique-me",clicar,100,30,2,6)
#Alterar botão
Btn_Tela1.configure(fg_color="red",hover_color="Maroon")

#Caixa de texto
Caixa_Tela1 = CriarCaixaTexto(Tela1,200,30,3,6,"Insira a data",Modo="Data")

#Criar Switch
Switch_Tela1 = CriarSwitch(Tela1,"Alterar Tema",4,6,alterarTema)

#Criar Combo Box
Combo_Tela1 = CriarComboBox(Tela1,200,30,["Gustavo","Wellington","Mafi","Enzo","Milim"],5,6)

#Criar slider
Slider_Tela1 = CriarSlider(Tela1,400,10,6,6)

#Criar progressbar
BarraProgresso = CriarProgressBar(Tela1,500,10,8,6)

#Criar imgamem
label = CriarImagem(Tela1,300,200,9,6,"IMAGE.webp")


#Criar Janela 2
Tela2 = CriarJanelaP("Tela 2","600x600+500+50",2)
Tela2.withdraw()

Tela1.mainloop()