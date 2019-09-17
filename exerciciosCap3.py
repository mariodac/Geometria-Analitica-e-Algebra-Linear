from os import system, name
from math import sqrt, acos, degrees, inf
from fractions import Fraction
from numpy import arange

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
    comprimentoV = pow(comprimento(vetorV,tamanho), 2)
    resultado = escalar / comprimentoV
    proj = list()
    for i in range(0, tamanho):
        proj.append(Fraction(resultado * vetorV[i]).limit_denominator())
    return proj

def gerar_primos(quantidade, limite):
    primos = list()
    c = 0
    primo = 0
    for numero in range(2, limite+1):
        for i in range(2,numero):
            if numero % i == 0: break
            c += 1
        else:
            if len(primos) == 50: break
            primos.append(numero)
            primo += 1
    return primos


def menu():
    tilt = "*"
    print("{}Exercícios Computacionais do capítulo 3{}".format(tilt*10, tilt*10))
    for i in range(1, 6):
        print("Exercicio {}".format(i))
    print("Digite 6 para exercicio 1 ao 4")
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
            print("Comprimento do vetor u: {}".format(round(comprimento(vetorU, tam), 2)))
        elif op == 3:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 3")
            tam = int(input("Digite o tamanho do vetor: "))
            vetorU = list()
            vetorV = list()
            for i in range(0, tam):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i+1))))
            print("O angulo entre vetores é: {}°".format(round(anguloEntreVetores(vetorU, vetorV, tam),2)))
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
            tam = 50
            vetorU = gerar_primos(tam, 1000)
            vetorV = list()
            for i in range(0, tam):
                vetorV.append(int(pow(-1, i)))
            print("Produto Escalar =  {}".format(produtoEscalar(vetorU, vetorV, tam)))
            print("Comprimento Vetor U = {}".format(round(comprimento(vetorU, tam), 2)))
            print("Comprimento Vetor V = {}".format(round(comprimento(vetorV, tam), 2)))
            print("Angulo entre vetor u e v = {}°".format(round(anguloEntreVetores(vetorU, vetorV, tam), 2)))
            resultado = projecaoVetores(vetorU, vetorV, tam)
            print("Projeção de vetor u em relação a v = (", end="")
            for i in range(0, tam):
                if(i == tam-1):
                    print("{}".format(resultado[i]), end="")
                else: print("{}, ".format(resultado[i]), end="")
            print(")")
        elif op == 6:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 1 a 4")
            tam = int(input("Digite o tamanho do vetor: "))
            vetorU = list()
            vetorV = list()
            for i in range(0, tam):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i+1))))
            print("Comprimento do vetor u: {}".format(comprimento(vetorU, tam)))
            print("Comprimento do vetor v: {}".format(comprimento(vetorV, tam)))
            print("Produto escalar = ", produtoEscalar(vetorU, vetorV, tam))
            print("O angulo entre vetores é: {}°".format(anguloEntreVetores(vetorU, vetorV, tam)))
            resultado = projecaoVetores(vetorU, vetorV, tam)
            print("Projeção de vetor u em relação a v = (", end="")
            for i in range(0, tam):
                if(i == tam-1):
                    print("{}".format(resultado[i]), end="")
                else: print("{}, ".format(resultado[i]), end="")
            print(")")
                
        else:
            system('cls' if name == 'nt' else 'clear')
            print("Opção inválida")
