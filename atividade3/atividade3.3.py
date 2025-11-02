"""
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

< 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"
"""
import math

peso = (float(input("Informe o seu peso(ex: 50.00): ")))
altura = (float(input("Informe a sua altura(ex: 1.50): ")))

imc = peso / math.pow(altura, 2)

print("---Descricao---")
print(f"Altura: {altura:.2f} m")
print(f"Peso: {peso:.2f} kg")
print(f"IMC = {imc:.2f}")

if(imc <= 18.5):
    "Abaixo do peso"
elif(imc > 18.5 and imc <= 25):
    print("Peso normal")
elif(imc > 25 and imc <= 30):
    print("Sobrepeso")
elif(imc > 30): 
    print("Sobrepeso")
else: 
    print("Procure um médico, você tem algo de errado")