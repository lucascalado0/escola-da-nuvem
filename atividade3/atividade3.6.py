"""
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). 
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, 
informar o total a receber no final do mês, com duas casas decimais.
"""

nomeVendedor = input("Informe o nome do vendedor: ")
salarioFixo = (float(input(f"Informe o salário fixo do vendedor {nomeVendedor}: ")))
totalDeVendas = (float(input("Informe o total de vendas(em dinheiro): ")))

comissao = totalDeVendas * 0.15 

salarioTotal = salarioFixo + comissao

print(f"Salário total de {nomeVendedor}: R${comissao:.2f}")
