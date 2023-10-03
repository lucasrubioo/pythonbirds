class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return 'Ola'

if __name__ == '__main__':
    p = Pessoa('Lucas')
    print(p.cumprimentar(), p.nome)