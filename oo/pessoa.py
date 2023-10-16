class Pessoa:
    # Atribudo default ou atributo de classe.
    # Deixamos fora do __init__ pois o atributo olhos por padrao sempre vai ser 2,
    # assim otimiza o espaço de armazenamento da memoria.
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = None): # Atributos de instancia ficam dentro do __init__
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod # decorator de modo estatico
    def modulo_estatico():
        return 42

    @classmethod # decorator de atributo de classe
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    del danilo.filhos # remover atributos dinamicamente do objetdo danilo, nao remove da classe Pessoa.
    danilo.olhos = 1 # quando atribuimos um valor diferente do default para o objeto danilo o id do objeto muda,
    # pois o atributo passa a fazer parte do __dict__ do objeto.
    del danilo.olhos
    Pessoa.olhos = 3 # Muda o valor da classe inteira.
    print(lucas.__dict__)
    print(danilo.__dict__)
    print(lucas.olhos)
    print(danilo.olhos)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos) , id(lucas.olhos), id(danilo.olhos))
    print(Pessoa.modulo_estatico() , lucas.modulo_estatico())
    print(Pessoa.nome_e_atributo_de_classe() , lucas.nome_e_atributo_de_classe())
    print()
