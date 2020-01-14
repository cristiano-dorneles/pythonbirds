class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
class Homen(Pessoa):
    pass
class Mulher(Pessoa):
    pass

if __name__ == '__main__':
    emilly = Mulher(nome='Emilly')
    Cristiano = Homen(emilly, nome='Acelerar')
    print(Pessoa.cumprimentar(Cristiano))
    print(id(Cristiano))
    print(Cristiano.cumprimentar())
    print(Cristiano.nome)
    print(Cristiano.idade)
for filho in Cristiano.filhos:
    print(filho.nome)
    Cristiano.sobrenome = 'Dorneles'
    del Cristiano.filhos
    Cristiano.olhos=1
    del Cristiano.olhos
    print(Cristiano.__dict__)
    print(emilly.__dict__)
    Pessoa. olhos = 3
    print(Pessoa.olhos)
    print(Cristiano.olhos)
    print(emilly.olhos)
    print(id(Pessoa.olhos), id(Cristiano.olhos), id(emilly.olhos))
    print(Pessoa.metodo_estatico(), Cristiano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Cristiano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homen))
    print(isinstance(Cristiano, Pessoa))
    print(isinstance(emilly, Homen))
    print(isinstance(emilly, Mulher))




























