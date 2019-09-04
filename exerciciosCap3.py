from os import system, name

def produtoEscalar(vetorU, vetorV, tamanho):
    resultado = 0
    for i in range(0, tamanho):
        resultado += vetorU[i] * vetorV[i]
    return resultado

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
                vetorU.append(int(input("Digite a coordenada {} do vetor u: ".format(i))))
                vetorV.append(int(input("Digite a coordenada {} do vetor v: ".format(i))))
            print("Produto escalar = ", produtoEscalar(vetorU, vetorV, tam))
        elif op == 2:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 2")
        elif op == 3:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 3")
        elif op == 4:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 4")
        elif op == 5:
            system('cls' if name == 'nt' else 'clear')
            print("Exercicio 5")
        else:
            system('cls' if name == 'nt' else 'clear')
            print("Opção inválida")
