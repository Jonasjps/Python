print('Bem vindo a Copiadora do Jonas Pessoa.\n')

while True:
  def escolha_servico ():
    print('Entre com o tipo de serviço desejado ')
    print('DIG - Digitação\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia')
    servico = input('>>')

      
    if(servico != 'DIG'.lower() or servico != 'ICO'.lower() or servico != 'IPB'.lower() or servico != 'FOT'.lower()):
      print('Escolha inválida, entre com o tipo do serviço novamente.')

    if(servico == 'DIG'.lower() or servico == 'ICO'.lower() or servico == 'IPB'.lower() or servico == 'FOT'.lower()):
      num_paginas = print(int(input('Entre com o número de páginas:')))
      break
      
  escolha_servico()
  continue