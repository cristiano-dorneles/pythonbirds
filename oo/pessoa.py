class Pessoa:
    def __init__(self, *filhos, nome=None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    emilly = Pessoa(nome='Emilly')
    Cristiano = Pessoa(emilly, nome='Cristiano')
    print(Pessoa.cumprimentar(Cristiano))
    print(id(Cristiano))
    print(Cristiano.cumprimentar())
    print(Cristiano.nome)
    print(Cristiano.idade)
    for filho in Cristiano. filhos:
    print(filho.nome)
    Cristiano.sobrenome = 'Dorneles'
    del Cristiano.filhos
    print(Cristiano.__dict__)
    print(emilly.__dict__)















