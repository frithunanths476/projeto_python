class Produto:
    def __init__(self,Nome,Quantidade,Preco,Total):
        self.Nome = Nome
        self.Quantidade = Quantidade
        self.Preco = Preco
        self.Total = Total
listaBD = []

def CadastrarBD(Nome,Quantidade,Preco):
    Total = Quantidade*Preco
    print(Nome,Quantidade,Preco,Total)
    obj = Produto(Nome,Quantidade,Preco,Total)
    listaBD.append(obj)