import modulo

""" Explicação: utilizo o try para verificar a excecão
    Utilizo o assert para poder comparar valores logicos diferentes

try:
    resultado = modulo.soma(3, 5)
    esperado = 8
    assert resultado == esperado
    print("Passou no teste")
except AssertionError:
    print("Erro: o valor esperado é: ", esperado, "mas a função obteve o valor: ", resultado)

    
    irei criar a função do teste_funcao para ficar mais automatizada."""

def teste_funcao(x, y, esperado):
    try: 
        resultado = modulo.soma(x, y)
        assert resultado == esperado
        print("Passou no teste")
    except AssertionError:
        print("Erro: o valor esperado é: ", esperado, "mas a função obteve o valor: ", resultado)

teste_funcao(0, 0, 0)
teste_funcao(1, 5, 5)
