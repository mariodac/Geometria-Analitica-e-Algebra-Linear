from os import system, name
from math import sqrt

def menu():
    print("*"*3 + "Exercicios computacionais capitulos 4" + "*"*3)
    print("Exercicio 1")
    print("Exercicio 2")
    print("Exercicio 3")
    print("Exercicio 4")
    print("Exercicio 5")
    op = int(input("Digite a opção desejada: "))
    return op

def limparTela():
    system('cls' if name == 'nt' else 'clear')

def produtoVetorial(vetorU, vetorV):
    resultado = list()
    resultado.append((vetorU[1]*vetorV[2]) - (vetorV[1]*vetorU[2]))
    resultado.append((vetorV[0]*vetorU[2]) - (vetorU[0]*vetorV[2]))
    resultado.append((vetorU[0]*vetorV[1]) - (vetorV[0]*vetorU[1]))
    return resultado

def comprimento(vetorU, tamanho):
    resultado = 0
    for i in range(0, tamanho):
        resultado += pow(vetorU[i], 2)
    return sqrt(resultado)

if __name__ == "__main__":
    op = -1
    tam = 3
    while op != 0 :
        op = menu()
        if op == 0:
            limparTela()
            print("Programa encerrado")
            
        elif op == 1:
            limparTela()
            print("Exercicio 1")
            vetorU = list()
            vetorV = list()
            for i in range(0, tam):
                vetorU.append(int(input("Digite a coordenada {} do vetor U: ".format(i + 1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor V: ".format(i + 1))))
            resultado = produtoVetorial(vetorU, vetorV)
            print("(", end="")
            for i in range(0, tam):
                if(i == tam - 1):
                    print("{}".format(resultado[i]), end="")
                else: print("{}, ".format(resultado[i]), end="")
            print(")")
            
        elif op == 2:
            limparTela()
            print("Exercicio 2")
            vetorU = list()
            vetorV = list()

            
        elif op == 3:
            limparTela()
            print("Exercicio 3")
            
        elif op == 4:
            limparTela()
            print("Exercicio 4")
            
        elif op == 5:
            limparTela()
            print("Exercicio 5")
            
        else:
            limparTela()
            print("Opção inválida")
            