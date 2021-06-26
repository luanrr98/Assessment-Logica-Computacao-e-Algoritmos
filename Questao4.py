import matplotlib.pyplot as plt


def calcular_rendimento(montante_inicial,rendimento_periodo,aporte_periodo,total_periodo):
    valor_acumulado = []
    montante_meses = [] 
    for i in range(total_periodo):
        valor_rendimento = (montante_inicial*rendimento_periodo)/100 #calculando qual é o valor a adicionar
        montante_inicial = montante_inicial+valor_rendimento
        montante_inicial = montante_inicial+aporte_periodo
        print(f"Após {i+1} periodo(s), o montante será de R${montante_inicial:.2f}.")
        montante_meses.append(i+1)
        valor_acumulado.append(montante_inicial)
    return montante_meses, valor_acumulado

#Letra b, grafico
def grafico(montante_meses, valor_acumulado):
    plt.plot(valor_acumulado, montante_meses)
    plt.show()





#Pegando os valores
montante_inicial = float(input("Valor inicial: R$"))
rendimento_periodo= float(input("Rendimento por periodo (%): "))
aporte_periodo= float(input("Aporte a cada período: R$"))
total_periodo= int(input("Total de períodos (meses): "))

montante_meses, valor_acumulado = calcular_rendimento(montante_inicial,rendimento_periodo,aporte_periodo,total_periodo) 

grafico(montante_meses, valor_acumulado)
