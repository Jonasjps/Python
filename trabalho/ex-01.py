print('Bem- Vindo a loja do Jonas Pessoa')

valor_produto = float(input('Entre com o valor do produto:'))
qtd = int(input('Entre com a quantidade do produto:'))

valor_total = valor_produto * qtd # calcula o valor total da compra sem o desconto.

if valor_total < 2500 : # verifica se o valor da compra é menor que 2500.

    desconto = valor_total - (valor_total * 0 /100) # calcula o valor da compra já com o desconto.

    print(f'O valor SEM desconto: {valor_total}') #valor COM desconto 
    print(f'O valor COM desconto: {desconto} {' ' * 10} valor total sem desconto, para obter o desconto inicial de 4% é preciso que a compra \n {' '* 77}seja maior ou igual a 2500 para mais descontos. ')    #valor SEM desconto

elif valor_total >= 2500 and valor_produto < 6000: #verica se o valor da compara é maior ou igual a 2500 e menor que 6000

    desconto = valor_total - (valor_total * 4 / 100) # calcula o valor da compra já com o desconto.

    print(f'O valor SEM desconto: {valor_total}')  #valor COM desconto
    print(f'O valor COM desconto: {desconto}')     #valor SEM desconto

elif  valor_total >= 6000 and valor_produto < 10000 : # verifica se o valor da compra é maior ou igual a 6000 e menor que 10000

    desconto = valor_total - (valor_total * 7 / 100) # calcula o valor da compra já com o desconto.

    print(f'O valor SEM desconto: {valor_total}')  #valor COM desconto
    print(f'O valor COM desconto: {desconto}')     #valor SEM desconto

else : # nesse bloco, vai ser verificado se o valor da compra é igual ou maior que 10000.

    desconto = valor_total - (valor_total * 11 / 100) # calcula o valor da compra já com o desconto.

    print(f'O valor SEM desconto: {valor_total}')  #valor COM desconto
    print(f'O valor COM desconto: {desconto}')     #valor SEM desconto


