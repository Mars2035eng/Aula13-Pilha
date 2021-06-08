from no import no


class lista:

    def __init__(self):
        self.tamanho = 0
        self.inicio = None

    def incluir(self, valor):

        if self.tamanho == 0:
            self.inicio = no(valor)
            self.tamanho += 1
            print("Item ", valor, " incluido")

        elif self.tamanho == 1:
            self.inicio.proximo = no(valor)
            self.tamanho += 1
            print("Item ", valor, " incluido")

        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo

            aux.proximo = no(valor)
            self.tamanho += 1
            print("Item ", valor, " incluido")

    def excluir(self):

        global auxAnt
        if self.tamanho == 0:
            print("Falha ao excluir - A lista está vazia")

        elif self.tamanho == 1:
            self.inicio = None
            self.tamanho = 0

        else:
            aux = self.inicio
            while aux.proximo:
                auxAnt = aux
                aux = aux.proximo

            auxAnt.proximo = None
            self.tamanho -= 1

    def imprimir(self):

        if self.inicio is None:
            print("A lista está vazia")

        else:
            aux = self.inicio
            i = 1
            print("______LISTA_______")
            print("fim da pilha")
            while aux:
                print(i, "- ", aux.dado)
                aux = aux.proximo
                i += 1
            print("início da pilha")
