# Validando a entrada 

# x = int(input('Digite um valor maior do que zero: '))

# while (x <= 0) : 
#     x = int(input('Digite um valor maior do que zero: '))
# print(f'Vacê digitou {x}. Encerrando o programa...')


soma = 0 
qtd = 0
for i in range(1, 101): 
    if (i % 2 == 0 ):
        soma += i
        qtd += 1
media = soma / qtd
print(f'A media dos pares de 1 até 100 é: {media}')
