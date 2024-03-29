from math import sqrt, pow
from os import system, name


def comprimentoVetor(vetor):
    soma = 0
    for v in vetor:
        soma += (pow(v,2))
    print(soma)
    return sqrt(soma)

def somaVetores(vetorU, vetorV, tamanho):
    soma = list()
    for i in range(0, tam):
        soma.append(vetorU[i] + vetorV[i])
    return soma

def diferencaVetores(vetorU, vetorV, tamanho):
    diferenca = list()
    for i in range(0, tam):
        diferenca.append(vetorU[i] - vetorV[i])
    return diferenca

def vetorCombinacaoAlphaBeta(vetorU, vetorV, alpha, beta):
    vetorCombinacao = list()
    tamanho = 0
    if len(vetorU) >= len(vetorV):
        tamanho = len(vetorU)
    else: tamanho = len(vetorV)
    for i in range(0, tamanho):
        vetorCombinacao.append((alpha * vetorU[i]) + (beta * vetorV[i]))
    return vetorCombinacao

def vetorCombinacaoAlpha(vetorU, vetorV, alpha):
    vetorCombinacao = list()
    for i in range(0, len(vetorU)):
        vetorCombinacao.append((vetorV[i]) + (alpha * vetorU[i]))
    return vetorCombinacao


def vetorCombinacaoVetorAlpha(vetorU, alpha, tam):
    vetorCombinacao = list()
    for i in range(0, tam):
        vetorCombinacao.append()
    return vetorCombinacao

def vetorCombinacaoSomatorio(vetorU, alpha):
    vetorCombinacao = list()
    for i in range(0, len(vetorU)): vetorCombinacao.append(0)
    count = 0
    while count <= alpha-1:
        for i in range(0, len(vetorU)):
            vetorCombinacao[i] += count * vetorU[i]
        count += 1

    return vetorCombinacao

def vetorFibonacci(vetorFib):
    vetorCombinacao = list()
    for i in range(0, len(vetorFib)): vetorCombinacao.append(0)
    for i in range(0, len(vetorFib)):
        vetorCombinacao[i] += (int(pow(-1, i))) * vetorFib[i]
    return vetorCombinacao
        
def menu():
    tilt = "*"
    print("{}Exercícios Computacionais do capítulo 2{}".format(tilt*10, tilt*10))
    for i in range(1, 6):
        print("Exercicio {}".format(i))
    print("0 para sair")

def limparTela():
    system('cls' if name == 'nt' else 'clear')

if __name__ == "__main__":
    op = -1
    while op != 0:
        menu()
        op = int(input("Digite o numero do exercicio: "))
        if op == 0: 
            limparTela()
            print("Programa encerrado")
        elif op == 1:
            limparTela()
            tamanho = int(input("Digite o tamanho do vetor: "))
            vetor = list()
            for i in range(0, tamanho):
                vetor.append(int(input("Digite a coordenada {}: ".format(i+1))))
            print("O comprimento do vetor informado é: {} u.c.".format(comprimentoVetor(vetor)))
        elif op == 2:
            vetorU = list()
            vetorV = list()
            tamanho = int(input("Digite o tamanho: "))
            alpha = int(input("Digite o valor de \u03B1: "))
            beta = int(input("Digite o valor de \u03B2: "))
            for i in range(0, tamanho):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i+1))))
            resultado = vetorCombinacaoAlphaBeta(vetorU, vetorV, alpha, beta)
            print("(", end="")
            for i in range(0, len(resultado)):
                if i == (len(resultado) - 1):
                    print(resultado[i], end="")
                else:
                    print("{}, ".format(resultado[i]), end="")
            print(")")
        elif op == 3:
            limparTela()
            vetorU = list()
            vetorV = list()
            tamanho = int(input("Digite o tamanho: "))
            alpha = int(input("Digite o valor de \u03B1: "))
            for i in range(0, tamanho):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i+1))))
            resultado = vetorCombinacaoAlpha(vetorU, vetorV, alpha)
            print("(", end="")
            for i in range(0, len(resultado)):
                if i == (len(resultado) - 1):
                    print(resultado[i], end="")
                else:
                    print("{}, ".format(resultado[i]), end="")
            print(")")
        elif op == 4:
            limparTela()
            vetorU = list()
            tamanho = int(input("Digite o tamanho: "))
            alpha = int(input("Digite o valor de \u03B1: "))
            for i in range(0, tamanho):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
            resultado = vetorCombinacaoSomatorio(vetorU, alpha)
            print("(", end="")
            for i in range(0, len(resultado)):
                if i == (len(resultado)-1):
                    print(resultado[i], end="")
                else:
                    print("{}, ".format(resultado[i]), end="")
            print(")")
        elif op == 5:
            a = 0
            b = 1
            vetorFib = [a, b]
            for i in range(0, (20 - len(vetorFib))):
                auxiliar = a + b
                a = b
                b = auxiliar
                vetorFib.append(auxiliar)
            for i in vetorFib: print(i)
            resultado = vetorFibonacci(vetorFib)
            print("(", end="")
            for i in range(0, len(resultado)): 
                if i == len(resultado)-1:
                    print(resultado[i], end="")
                else:
                    print("{}, ".format(resultado[i]), end="")
            print(")")
        elif op == 6:
            limparTela()
            print("Soma entre vetores")
            vetorU = list()
            vetorV = list()
            tam = int(input("Digite o tamanho do vetor: "))
            for i in range(0, tam):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i+1))))
            print("Resultado: {}".format(somaVetores(vetorU, vetorV, tam)))
        elif op == 7:
            limparTela()
            print("Diferença entre vetores")
            vetorU = list()
            vetorV = list()
            tam = int(input("Digite o tamanho do vetor: "))
            for i in range(0, tam):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i+1))))
            print("Resultado: {}".format(diferencaVetores(vetorU, vetorV, tam)))
        elif op == 8:
            limparTela()
            vetorU = list()
            vetorV = list()
            tamanho = int(input("Digite o tamanho: "))
            alpha = [-9, 0]
            for i in range(0, tamanho):
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i+1))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i+1))))
        else: 
            limparTela()
            print("Opção inválida")