class Aluno():

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return "O aluno {} tem o numero {}".format(self.nome, self.numero.title())
    
    def e_igual(self, lista_alunos):
        if self.numero == lista_alunos:
            return True
        return False

class Turma():

    def __init__(self, nome, ano):
        self.nome_turma = nome
        self.ano_letivo = ano
        self.lista_alunos = []
        self.total_alunos = 0

    def __str__(self):
        return "Nome da turma {} \n Ano letivo {} \n Número de alunos {} \n Lista de alunos {}".format(self.nome_turma, self.ano_letivo, self.total_alunos, self.lista_alunos)

    def verifica_aluno(self, aluno):
        for i in range(self.total_alunos):
            if self.lista_alunos.e_igual(aluno):
                return True
            return False

    def insere_instancia_aluno(self, aluno):
        if self.verifica_aluno(aluno) == False:
            self.lista_alunos.append(aluno)
            self.total_alunos += 1
            return True
        return False

    #def inserir_aluno(self):
       

    #def mostrar_lista(self):
        #for i in self.lista_alunos:
            #print(i)

A1 = Aluno(1, "Vitor")
print(A1)

A2 = Aluno(2, "Silva")
print(A2)

T1 = Turma("CRSI","2017/2018")
print(T1)
