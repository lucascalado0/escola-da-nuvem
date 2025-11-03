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
        numero2 = float(input("Informe o segundo valor"))
    
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
        continue    


    operacao = input("Informe a operação que deseja realizar(+, -, *, /): ")
    
    if operacao in ["+", "-", "*", "/"]:
        break

    if operacao == "+":
        print("Operação desejada: Adição")
        print("Resultado : " + numero1 + numero2)
    elif operacao == "-":
        print("Operação desejada: Subtração")
        print("Resultado: " + numero1 - numero2)
    elif operacao == "*":
        print("Operação desejada: Multiplicação")
        print("Resultado: " + numero1 * numero2)
    elif operacao == "/":
        print("Operação desejada: Divisão")
        print("Resultado: " + numero1 / numero2)
        try:
            resultado = numero1 / numero2
        except ZeroDivisionError:
            print("Erro: divisão por zero não é permitida.")
            continue  
    else:
        print("Operação inválida. Use apenas +, -, * ou /.")
        continue  
    

    
    print(f"O resultado de {numero1} {operacao} {numero2} é: {resultado}")
    break  