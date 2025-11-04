"""
Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:



1. A calculadora deve solicitar ao usuário que insira dois números e uma operação.

2. As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

3. O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

4. Trate os seguintes erros:

    Entrada inválida (não numérica) para os números

    Divisão por zero

    Operação inválida
    
5. Use try/except para capturar e tratar os erros apropriadamente.

6. Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

7. Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
"""

while True:
    try:
        numero1 = float(input("Informe o primeiro valor: "))
        numero2 = float(input("Informe o segundo valor: "))
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.\n")
        continue 

    operacao = input("Informe a operação que deseja realizar (+, -, *, /): ")

    try:
        if operacao == "+":
            resultado = numero1 + numero2
            print("Operação desejada: Adição")
        elif operacao == "-":
            resultado = numero1 - numero2
            print("Operação desejada: Subtração")
        elif operacao == "*":
            resultado = numero1 * numero2
            print("Operação desejada: Multiplicação")
        elif operacao == "/":
            resultado = numero1 / numero2
            print("Operação desejada: Divisão")
        else:
            print("Erro: Operação inválida. Use apenas +, -, * ou /.\n")
            continue  
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.\n")
        continue  

    print(f"O resultado de {numero1} {operacao} {numero2} é: {resultado}")
    break
