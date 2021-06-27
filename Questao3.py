def saude_financeira(renda_mensal, gastos_moradia, gastos_educacao, gastos_transporte):
    #Calcular a porcentagem de cada gasto referente a renda total
    percent_moradia = (gastos_moradia*100)/renda_mensal
    percent_educacao = (gastos_educacao*100)/renda_mensal
    percent_transporte = (gastos_transporte*100)/renda_mensal
    
    #Calcuar o valor máximo ideal referente a renda total
    moradia_ideal= (renda_mensal*30)/100
    educacao_ideal=(renda_mensal*20)/100
    transporte_ideal=(renda_mensal*15)/100

    print("Diagnóstico:\n")

    print(f"Seus gastos com moradia comprometem {percent_moradia:.2f}% de sua renda total.")

    if percent_moradia<=30:
        print("O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.\n")
    else:
        print(f"O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${moradia_ideal:.2f}.\n")

    print(f"Seus gastos com educação comprometem {percent_educacao:.2f}% de sua renda total.")

    if percent_educacao <= 20:
        print("O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.\n")
    else:
        print(f"O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R${educacao_ideal:.2f}.\n")

    print(f"Seus gastos com  transporte comprometem {percent_transporte:.2f}% de sua renda total.")

    if percent_transporte <= 15:
        print("O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.\n")
    else:
        print(f"O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R${transporte_ideal:.2f}.\n")

#Adquirindo os dados para passar como parâmetro para a função

renda_mensal = float(input("Renda mensal total: R$"))
gastos_moradia = float(input("Gastos totais com moradia: R$"))
gastos_educacao = float(input("Gastos totais com educação: R$"))
gastos_transporte = float(input("Gastos totais com transporte: R$"))
print("\n")
saude_financeira(renda_mensal,gastos_moradia,gastos_educacao,gastos_transporte)
