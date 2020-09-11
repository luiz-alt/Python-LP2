repetir = True
while repetir:
    try:
        x = int(input("Primeiro Valor: ")) #incluir string e float
        y = int(input("Segundo Valor: "))   #incluir string e float
        z = x / y
        print("O resultado da atividade é: ", z)
    except ValueError:
        print("Atenção: O valor informado não é um tipo inteiro")
    except ZeroDivisionError:
        print("Atenção: O valor de y tem que ser menor que 0")
    except:
        print("Atenção: Algo deu errado")
    else:
        repetir = False

