preco = float(input('Digite o preco do prduto: '))
percentual = float(input('Digite o percentual de desconto (0-100%): '))

desconto = preco * (percentual / 100)
final = preco - desconto 

print(f' O preco do produto é {preco}. Desconto de {percentual}%')
print(f' Valor calculado de desconto: {desconto}. Valor final do produto: {final}')
