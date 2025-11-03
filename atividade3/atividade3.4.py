"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temperatura = (float(input("Informe a temperatura que deseja converter: ")))

while True:
    unidadeOrigem = input("Informe a unidade de temperatura que será convertida (C - Celsius, F - Fahrenheit, K - Kelvin): ").upper()
    
    if unidadeOrigem in ["C", "F", "K"]:
        break
    else:
        print("Valor inválido. Tente novamente.")
    
while True:
    unidadeConversao = input("Informe a unidade de temperatura que deseja obter a conversão (C - Celsius, F - Fahrenheit, K - Kelvin): ").upper()

    if unidadeConversao in ["C", "F", "K"]:
        break
    else:
        print("Valor inválido. Tente novamente.")
        
if(unidadeOrigem == "C" and unidadeConversao == "F"):
    print("Conversão de Celsius para Fahrenheit: ")
    celsiusParaFahrenheit = (temperatura * 1.8) + 32
    print(f"Celsius: {temperatura}º C")
    print(f"Fahrenheit: {celsiusParaFahrenheit:.1f} F")

elif(unidadeOrigem == "F" and unidadeConversao == "C"):
    print("Conversão de Fahrenheit para celsius: ")
    fahrenheitParaCelsius = (temperatura - 32) * (5 / 9) 
    print(f"Fahrenheit: {temperatura} F")
    print(f"Celsius: {fahrenheitParaCelsius:.1f}º C")

elif(unidadeOrigem == "C" and unidadeConversao == "K"):
    print("Conversão Celcius para Kelvin: ")
    celsiusParaKelvin = temperatura + 273.5
    print(f"Celsius: {temperatura}º C")
    print(f"Kelvin: {celsiusParaKelvin:.1f} K")

elif(unidadeOrigem == "K" and unidadeConversao == "C"):
    print("Conversão de Kelvin para Celsius")
    KelvinParaCelsius = temperatura - 273.5
    print(f"Kelvin: {temperatura} K")
    print(f"Celsius: {KelvinParaCelsius:.1f}º C")

elif(unidadeOrigem == "K" and unidadeConversao == "F"):
    print("Conversão de Kelvin para Fahrenheit: ")
    kelvinParaFahrenheit = (temperatura - 273.5) * (9 / 5) + 32
    print(f"Kelvin: {temperatura}")
    print(f"Fahrenheit: {kelvinParaFahrenheit:.1f} F")
    
elif(unidadeOrigem == "F" and unidadeConversao == "K"):
    print("Conversão Fahrenheit para Kelvin: ")
    fahrenheitParaKelvin = (temperatura - 32) * (5 / 9) + 273.15
    print(f"Fahrenheit: {temperatura} F")
    print(f"Kelvin: {fahrenheitParaKelvin:.1f} K")

else:
    print("Opções inválidas")