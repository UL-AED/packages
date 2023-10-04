def ler_inteiro():
    try:
        return int(input('Insira um numero inteiro:'))
    except:
        print('Não é um numero inteiro válido. ')
        return ler_inteiro()

def ler_inteiro_positivo():
    while True:
        n = ler_inteiro()
        if n > 0:
            return n
        else:
            print('O numero não é positivo.')