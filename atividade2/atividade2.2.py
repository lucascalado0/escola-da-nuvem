"""
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

Nome do produto: "Camiseta"

Preço original: R$ 50.00

Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nomeProduto = "Camiseta"
precoOriginal = 50.00
desconto = 0.2

precoFinal = precoOriginal - (precoOriginal * desconto) 

print("---Descrição---")
print("Produto: " + nomeProduto)
print(f"Preço original: R${precoOriginal}")
print(f"Preço com desconto de 20%: R${precoFinal}")

