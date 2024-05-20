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

sabor = input('Entre com sabor desejado (CP/AC):')
tamanho = input('Entre com o tamanho desejado (P/M/G):')
somar = 0

if (sabor == 'CP'.lower() and tamanho == 'P'.lower()):
    somar = somar * 9.00
    print(f'Você pedio um Cupuaçu no tamanh) o P: R$ 9.00')
elif (sabor == 'CP'.lower() and tamanho == 'M'.lower()):
        somar = somar * 14.00
        print(f'Você pedio um Cupuaçu no tamanho P: R$ 14.00')
elif (sabor == 'CP'.lower() and tamanho == 'G'.lower()):
    somar = somar * 18.00
    print(f'Você pedio um Cupuaçu no tamanho P: R$ 18.00')
else:
    print('Tamanho inválido. Tente novamente.')
    
        

cont_pedido = input('Você deseja mais alguma coisa? (S/N):')

if(cont_pedido == 'S'.lower()):
    novo_sabor = input('Entre com sabor desejado (CP/AC):')
    novo_tamanho = input('Entre com o tamanho desejado (P/M/G):')
else:
    print(f'O valor total a ser pago: {somar}')


# if mostrar_menu() == 'CP'.upper():




# if tamanho != 'P/M/G' :
#     print('Tamanho inválido. Tente novamnete.')


       
