import matplotlib.pyplot as plt
def extrair_dados (pib):  #Extração e organização dos dados.
    cabecalho_anos = []
    with open('Assessment_PIBs - modelo 2.csv', 'r') as arquivo:
        conteudo_arquivo= arquivo.read()
    ano_pib = []
    conteudo_arquivo = conteudo_arquivo.splitlines()
    cabecalho_paises = conteudo_arquivo[0]
    conteudo_arquivo = conteudo_arquivo[1:]
    cabecalho_paises = cabecalho_paises.split(',')
    for indice in conteudo_arquivo:
        indice = indice.split(",")
        ano_pib.append(indice)
    for i in range(8):
        cabecalho_anos.append(ano_pib[i][0])
    return cabecalho_paises, ano_pib, cabecalho_anos

def mostrar_pib_pais(pais, ano): #Função para mostrar o PIB do pais e anos selecionados
    cabecalho_paises, ano_pib, cabecalho_anos = extrair_dados('Assessment_PIBs - modelo 2.csv')
    if pais not in cabecalho_paises:
        print("\nPaís não disponível.")
        exit()
    if ano not in cabecalho_anos:
        print("\nAno não disponível.")
        exit()
    indice_pais = cabecalho_paises.index(pais)
    indice_ano = cabecalho_anos.index(ano)
    print( f"\nPIB {pais} em {ano}: US${ano_pib[indice_ano][indice_pais]} trilhões.")

def estimativa_variacao ():# Função para estimar a variação do PIB
    cabecalho_paises, ano_pib, cabecalho_anos= extrair_dados('Assessment_PIBs - modelo 2.csv')
    j=1
    for i in cabecalho_paises[1:]:
        valor = ano_pib[0][j]
        valor2= ano_pib[7][j]
        j= j+1
        valor = float(valor)
        valor2 = float(valor2)
        variacao = (valor2/valor-1)*100
        print(f"{i}         Variação de {variacao:.2f}% entre 2013 e 2020.")


def mostrar_grafico(pais): #Função para mostrar o gráfico do PIB
    cabecalho_paises, ano_pib, cabecalho_anos = extrair_dados('Assessment_PIBs - modelo 2.csv')
    if pais not in cabecalho_paises:
        print("País Inválido!!")
        exit()
    lista_pibs = []
    indice_pais = cabecalho_paises.index(pais)
    for i in range(8):
        lista_pibs.append(float(ano_pib[i][indice_pais]))
    plt.title(pais)
    plt.xlabel("Anos")
    plt.ylabel("PIB")
    plt.plot(cabecalho_anos, lista_pibs, 'r-o')
    plt.show()
    

#Selecionar a opção de qual função usar.
resposta = input("Digite a opção desejada:\n 1- Mostrar PIB de um pais de um ano selecionado;\n 2- Listar estimativa da variação do PIB dos paises;\n 3- Mostrar gráfico da evolução do PIB de uma país selecionado.\n Digite sua escolha (1, 2 ou 3): ")
if resposta == "1":    #LETRA A
    pais = input("\nInforme um país: " )
    ano = input("Informer um ano entre 2013 e 2020: ")
    mostrar_pib_pais(pais,ano)

elif resposta == "2":    #LETRA B
    estimativa_variacao()

elif resposta == "3":    #LETRA C
    pais = input("\nDigite o nome do país: ")
    mostrar_grafico(pais)

else:
    print("Opção Inválida")
    exit()


