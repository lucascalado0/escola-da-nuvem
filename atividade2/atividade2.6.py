"""
Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. Calcule o salário do funcionário e exiba o resultado formatado corretamente.

Entrada:

O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:

Número do funcionário (numero_funcionario).

Quantidade de horas trabalhadas (horas_trabalhadas).

Valor recebido por hora (valor_por_hora).
"""

numeroFuncionario = (int(input("Informe o número do funcionário: ")))
quantidadeHorasTrabalhadas = (int(input("Quantidade de horas trabalhadas: ")))
valorHora = (float(input("Valor recebido por hora: ")))

salario = quantidadeHorasTrabalhadas * valorHora

print("---Informações---")
print(f"Número do funcionário: {numeroFuncionario}")
print(f"Quantidade de horas trabalhadas: {quantidadeHorasTrabalhadas}")
print(f"Valor recebido por hora: {valorHora:.2f}")
print(f"Salário: R${salario:.2f}")