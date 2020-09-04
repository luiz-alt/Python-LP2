def funcao_1():
    try:
        print("Inicio da funcao")
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(15):
            print(lista[i])
        print("Fim da funcao")
    except IndexError:
        print("Erro: Lista ou tupla menor que range.")
    except:
        print("Atenção: Erro")

print("Inicio da funcção")
funcao_1()
print("Fim da funcão")