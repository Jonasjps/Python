def mostrar_menu() : #função que mostra o Menu
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

sabor = input('Entre com sabor desejado (CP/AC):')
while True :
    if(sabor != 'CP'.lower() and sabor != 'AC'.lower()): #Verificando o sabor se é de Cupuaçu ou Açai.
        print('Sabor inválido. Tente novamente.\n')
        sabor = input('Entre com sabor desejado (CP/AC):')
        continue
    else:
        tamanho = input('Entre com o tamanho desejado (P/M/G):') 
        break   
         

def sabor_tamanho(sabor, tamanho): # função que verifica os sabores e tamanho dos gelatos.

    global cont 
    global somar 

    if (sabor == 'CP'.lower() and tamanho == 'P'.lower()):# sequêcia de condições onde se verifica o tamanho e define o valor do gelato.
        somar = somar + 9.00
        cont = cont + 1
        print(f'Você pedio um Cupuaçu no tamanho P: R$ 9.00 \n')

    elif (sabor == 'AC'.lower() and tamanho == 'P'.lower()):
            somar = somar + 11.00
            cont = cont + 1
            print(f'Você pedio um Açai no tamanho P: R$ 11.00 \n')

    elif (sabor == 'CP'.lower() and tamanho == 'M'.lower()):
            somar = somar + 14.00
            cont = cont + 1
            print(f'Você pedio um Cupuaçu no tamanho M: R$ 14.00 \n')

    elif (sabor == 'AC'.lower() and tamanho == 'M'.lower()):
            somar = somar + 16.00
            cont = cont + 1
            print(f'Você pedio um Açai no tamanho M: R$ 16.00 \n')

    elif (sabor == 'CP'.lower() and tamanho == 'G'.lower()):
        somar = somar + 18.00
        cont = cont + 1
        print(f'Você pedio um Cupuaçu no tamanho G: R$ 18.00 \n') 

    elif (sabor == 'AC'.lower() and tamanho == 'G'.lower()):
            somar = somar + 20.00
            cont = cont + 1
            print(f'Você pedio um Açai no tamanho G: R$ 20.00 \n')    
    else:
        print('Tamanho inválido. Tente novamente. \n')

sabor_tamanho(sabor,tamanho)

novo_sabor = input('Entre com sabor desejado (CP/AC):')# variavel que armazena o novo sabor.
novo_tamanho = input('Entre com o tamanho desejado (P/M/G):') # variavel que armazena o novo tamanho.

sabor_tamanho(novo_sabor, novo_tamanho)
cont_pedido = input('Deseja mais alguma coisa? (S/N): ')

if(cont_pedido == 'S'.lower()):# verifica se o usuario quer continuar fazendo o pedido.
  novo_sabor = input('Entre com sabor desejado (CP/AC):')
  novo_tamanho = input('Entre com o tamanho desejado (P/M/G):') 
  sabor_tamanho(novo_sabor, novo_tamanho)    

cont_pedido = input('Deseja mais alguma coisa? (S/N): ')    

if (cont_pedido == 'N'.lower()):#verifica se o usuario quer continuar comprando ou finalizar o pedido.
  print(f'\nO valor total a ser pago: {somar}')# codigo armazena o valor total do pedido.
