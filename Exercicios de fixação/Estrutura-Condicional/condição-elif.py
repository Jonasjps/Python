print('Escolha o que deseja comprar: ')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Qual sua escolha?'))
qtd = int(input('quantas unidades?'))

match (produto) : 
    case 1:
        pagar = qtd * 2.3
        print(f'Você comprou {qtd} maças. Total a pagar: {pagar}')
    case 2: 
        pagar = qtd * 3.6
        print(f'Você comprou {qtd} maças. Total a pagar: {pagar}')
    case 3:
        pagar = qtd * 1.85
        print(f'Você comprou {qtd} maças. Total a pagar: {pagar}')
    case _:
        print('Produto Inexistente.')