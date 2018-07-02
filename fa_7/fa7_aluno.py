class Aluno():

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return "O aluno {} tem o numero {}".format(self.nome, self.numero.title())
    
    def e_igual(self, aluno):
        return self.numero == aluno.numero

if __name__ == "__main__":

    A1 = Aluno(1, "Vitor")
    print(A1)

    A2 = Aluno(2, "Silva")
    print(A2)