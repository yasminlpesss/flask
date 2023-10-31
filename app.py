from flask import Flask, render_template

app = Flask(__name__)
class cadcarro:
    def __init__(self,modelo,roda,cor,ano):
        self.modelo = modelo
        self.roda = roda
        self.cor = cor
        self.ano = ano

class cadfoto:
    def __init__(self, portfolio,contato):
        self.portfolio = portfolio
        self.contato = contato


class cadmercado:
    def __init__(self, automotivo, skincare, roupas, brinquedos):
        self.automotivo = automotivo
        self.skincare = skincare
        self.roupas = roupas
        self.brinquedos = brinquedos



@app.route('/carro')
def carro():
    car1 = cadcarro("Chevrolet onix",4,"vermelho",2015)
    car2 = cadcarro("Citroen c3",2,"cinza",2010)
    car3 = cadcarro("fiat mob",2,"preto",2019)
    lista = [car1,car2,car3]
    return render_template("site.html", titulo = "venda de carros:", listacarros = lista)



@app.route('/foto')
def foto():
    ft1 = cadfoto("ensaios")
    ft2 = cadfoto("contatos")
    lista = [ft1, ft2]
    return render_template("site2.html", titulo = "fotografo", listafotografos = lista)

@app.route('/mercado')
def mercado():
    item1 = cadmercado("rodas","sabonete liquido","roupas infantis","lego surprise")
    item2 = cadmercado("lanterna","esfoliante facial ","roupas infanto juvenil","barbie")
    item3 = cadmercado("capotas","hidratante facial","roupas casuais","piscina inflavel")
    lista = [item1, item2, item3]
    return render_template("site3.html", titulo = "mercado livre:", listamercado = lista)



if __name__ == '__main__':
    app.run()

