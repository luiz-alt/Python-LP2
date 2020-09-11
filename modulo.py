def soma(x, y):
    z = x + y
    return z


#TESTE DAS MINHAS FUNCÕES

def test_soma1():
    assert soma(3, 5) == 8 #Passo o parametro chamando a função que gistaria de testar e coloco o == para 
                           #passar o meu resultado o meu resultado 

#Tenho que criar cada função para cada teste com os outros valores.

def test_soma2():
    assert soma(1, 5) == 6

def test_soma3():
    assert soma(3, 3) == 6

def test_soma4():
    assert soma(3, 7) == 9

#se for 0 devolva 0