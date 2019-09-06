from os import system, name
from math import sqrt, acos, degrees
from fractions import Fraction

def produtoEscalar(vetorU, vetorV, tamanho):
    resultado = 0
    for i in range(0, tamanho):
        resultado += vetorU[i] * vetorV[i]
    return resultado

def comprimento(vetorU, tamanho):
    resultado = 0
    for i in range(0, tamanho):
        resultado += pow(vetorU[i], 2)
    return sqrt(resultado)

def anguloEntreVetores(vetorU, vetorV, tamanho):
    escalar = produtoEscalar(vetorU, vetorV, tam)
    comprimentoU = comprimento(vetorU, tamanho)
    comprimentoV = comprimento(vetorV, tamanho)
    resultado = escalar/(comprimentoU * comprimentoV)
    return round(degrees(acos(resultado)), 2)

def projecaoVetores(vetorU, vetorV, tamanho):
    escalar = produtoEscalar(vetorU, vetorV, tamanho)
    comprimentoV = pow(comprimento(vetorU,tamanho), 2)
    resultado = escalar / comprimentoV
    proj = list()
    for i in range(0, tamanho):
        proj.append(Fraction(resultado * vetorV[i]).limit_denominator())
    return proj

def menu():
    tilt = "*"
    print("{}Exercícios Computacionais do capítulo 3{}".format(tilt*10, tilt*10))
    for i in range(1, 6):
        print("Exercicio {}".format(i))
    print("0 para sair")

if __name__ == "__main__":
    op = -1
    while op != 0:
        menu()
        try:
            op = int(input("Digite o numero do exercicio: "))
        except ValueError:
            system('cls' if name == 'nt' else 'clear')
            print("Opção inválida")
        if op == 0:
            system('cls' if name == 'nt' else 'clear')
            print("Programa encerrado")
        elif op == 1:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 1")
            tam = int(input("Digite o tamanho do vetor: "))
            vetorU = list()
            vetorV = list()
            for i in range(0, tam):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i+1))))
            print("Produto escalar = ", produtoEscalar(vetorU, vetorV, tam))
        elif op == 2:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 2")
            tam = int(input("Digite o tamanho do vetor: "))
            vetorU = list()
            for i in range(0, tam):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
            print("Comprimento do vetor u: {}".format(comprimento(vetorU, tam)))
        elif op == 3:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 3")
            tam = int(input("Digite o tamanho do vetor: "))
            vetorU = list()
            vetorV = list()
            for i in range(0, tam):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i+1))))
            print("O angulo entre vetores é: {}°".format(anguloEntreVetores(vetorU, vetorV, tam)))
        elif op == 4:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 4")
            tam = int(input("Digite o tamanho do vetor: "))
            vetorU = list()
            vetorV = list()
            for i in range(0, tam):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i+1))))
            resultado = projecaoVetores(vetorU, vetorV, tam)
            print("(", end="")
            for i in range(0, tam):
                if(i == tam-1):
                    print("{}".format(resultado[i]), end="")
                else: print("{}, ".format(resultado[i]), end="")
            print(")")
        elif op == 5:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 5")
        else:
            system('cls' if name == 'nt' else 'clear')
            print("Opção inválida")
