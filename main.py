from leitura_dados.leitura_dados import ler_inteiro,ler_inteiro_positivo
from operacoes_aritmeticas.operacoes_aritmeticas import soma,subtracao, fatorial
from resultados.resultado import resultado

while True:
    print('Menu:')
    print('1. Soma')
    print('2. Subtração')
    print('3. Fatorial')
    print('4. Sair')

    opcao = input("Escolha uma opção (1/2/3/4): ")
    opcao = opcao.strip()

    if not opcao.isdigit():
        print("Opção inválida. Deve ser um número (1/2/3/4).")
        continue

    opcao = int(opcao)

    if opcao == 1:
        a = ler_inteiro()
        b = ler_inteiro()
        conta = soma(a,b)
        resultado(conta)

    elif opcao == 2:
        a = ler_inteiro()
        b = ler_inteiro()
        conta = subtracao(a,b)
        resultado(conta)

    elif opcao == 3:
        x = ler_inteiro_positivo()
        conta = fatorial(x)
        resultado(conta)

    elif opcao == 4:
        break
    else:
        print('Opção invalida. Deve ser um número (1/2/3/4).')