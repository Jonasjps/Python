def mostrar_menu() :
    print(f'{" "*3}Bem-vindo A Loja de gelatos do Jonas Pessoa')
    print(f'{"-"*20}Cardápio{"-"*20}')
    print(f'{"-"*48} ')
    print(f'---| Tamanho  |  Cupuaçu (CP)  |  Açaí (AC) |---')
    print(f'---|    P     |    R$  9,00    |  R$ 11,00  |---')
    print(f'---|    M     |    R$ 14,00    |  R$ 16,00  |---')
    print(f'---|    G     |    R$ 18,00    |  R$ 20,00  |---')
    print(f'{"-"*48}')

mostrar_menu()
cont = 0
somar = 0

while True :
    sabor = input('Entre com sabor desejado (CP/AC):')#fazer um condiçao para verificar se o sabor é o certo.

    if(sabor != 'CP'.lower() and sabor != 'AC'.lower()):
        print('Sabor inválido. Tente novamente.')
        continue  
    else:
        tamanho = input('Entre com o tamanho desejado (P/M/G):')    
        break
         

def sabor_tamanho(sabor, tamanho):

    global cont 
    global somar 

    if (sabor == 'CP'.lower() and tamanho == 'P'.lower()):
        somar = somar + 9.00
        cont = cont + 1
        print(f'Você pedio um Cupuaçu no tamanh) o P: R$ 9.00')

    elif (sabor == 'AC'.lower() and tamanho == 'P'.lower()):
            somar = somar + 11.00
            cont = cont + 1
            print(f'Você pedio um Açai no tamanho P: R$ 11.00')

    elif (sabor == 'CP'.lower() and tamanho == 'M'.lower()):
            somar = somar + 14.00
            cont = cont + 1
            print(f'Você pedio um Cupuaçu no tamanho M: R$ 14.00')

    elif (sabor == 'AC'.lower() and tamanho == 'M'.lower()):
            somar = somar + 16.00
            cont = cont + 1
            print(f'Você pedio um Açai no tamanho M: R$ 16.00')

    elif (sabor == 'CP'.lower() and tamanho == 'G'.lower()):
        somar = somar + 18.00
        cont = cont + 1
        print(f'Você pedio um Cupuaçu no tamanho G: R$ 18.00') 

    elif (sabor == 'AC'.lower() and tamanho == 'G'.lower()):
            somar = somar + 20.00
            cont = cont + 1
            print(f'Você pedio um Açai no tamanho G: R$ 20.00')    
    else:
        print('Tamanho inválido. Tente novamente.')

sabor_tamanho(sabor,tamanho)

cont_pedido = input('Você deseja mais alguma coisa? (S/N):')

if(cont_pedido == 'S'.lower()):
    while True :
        novo_sabor = input('Entre com sabor desejado (CP/AC):')
        if(novo_sabor != 'CP'.lower and novo_sabor != 'AC'.lower): 
            print('Sabor inválido. Tente novamente.')
            
        else:
            novo_tamanho = input('Entre com o tamanho desejado (P/M/G):')
            break
    sabor_tamanho(novo_sabor,novo_tamanho)
    cont_pedido = input('Você deseja mais alguma coisa? (S/N):')
if(cont_pedido == 'N'.lower()):
    print(f'O valor total a ser pago: {somar}')






       
