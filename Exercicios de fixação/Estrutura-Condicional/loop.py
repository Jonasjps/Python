print('LANCHONETE')
print('1- Coxinha RS 5,00')
print('2- Pastel RS 7,00')
print('3- Café RS 4,00')
print('4- Suco RS 6,00')
print('5- SAIR')

total = 0

while True :
    op = int(input('Qual item gostaria de comprar? '))
    

    if(op == 1) :
        qtd = int(input('Quatas unidades quer comprar? '))
        total = total + qtd * 5.00
    elif (op == 2) :
        qtd = int(input('Quatas unidades quer comprar? '))
        total = total + qtd * 7.00
    elif (op == 3) : 
        qtd = int(input('Quatas unidades quer comprar? '))
        total = total + qtd * 4.00
    elif (op == 4) :
        qtd = int(input('Quatasw unidades quer comprar? '))
        total = total + qtd * 6.00
    elif (op == 5) :
        break
    else:
        print('Produto invalido. Selecione outro.')


print(f'O total a ser gasto neste pedido é de R$ {total}')


