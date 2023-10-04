class Pessoa:
    def __init__(self, *filhos, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Ola'

if __name__ == '__main__':
    lucas = Pessoa(nome='Lucas',idade=24)
    gustavo = Pessoa(nome='Gustavo', idade=11)
    danilo = Pessoa(lucas,gustavo,nome='Danilo', idade=42)
    print(lucas.cumprimentar())
    print(lucas.idade)
    print(lucas.nome)
    print(id(lucas))
    print()
    print('FILHOS DE DANILO')
    for filho in danilo.filhos:
        print(filho.nome)
    danilo.sobrenome='Rubio'
    del danilo.filhos #remover atributos dinamicamente
    print(lucas.__dict__)
    print(danilo.__dict__)
