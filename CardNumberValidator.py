'''
My youtube chanel: https://www.youtube.com/channel/UCUxjylnMNFvQUa-faoqZjOw?
##############################################
#            Card Number Validator           #
#              Coded By J4CK_                #
#                01/13/018                   #
##############################################

 Algoritimos:
 Link: http://jurispro.net/a/mobile/articles.php?lng=pt&pg=24563
-De esquerda a direita, tomamos os dígitos que aparecem nas posições ímpares e vamos multiplicá-los por 2. Se o número obtido for menor que 10, ficamos com ele; se for maior que 10, somamos os dígitos desse número e ficamos com o resultado (isto é, calculamos o valor do resultado módulo 9).
-Somamos todos os resultados obtidos no passo anterior. Digamos que essa soma vale A.
-Somamos todos os dígitos que aparecem nas posições pares do número do cartão (excepto o dígito de controlo, que é o que não sabemos). Chamemos B à dita soma.
-Agora somamos os dois resultados anteriores. Tomamos o valor desta soma e vamos deixando 10 até obter um número entre 0 e 9 (isto é, calculamos Soma módulo 10). Então o dígito de controlo (DC) é 10 menos esse número obtido
-Para saber se um número de cartão é falso o que podemos fazer é acrescentar o último dígito do número (o suposto dígito de controlo) à soma dos dígitos das posições pares. Se o resultado de A+B não é múltiplo de 10 (quer dizer, se não é igual ao módulo 10) então o número do cartão é falso.

 Cartoes com 15 algarismos:
 Link: https://www.devmedia.com.br/validando-cartao-de-credito-cpf-e-cnpj/1923
 -Validar o nº. de cartão de crédito. O Algoritmo deste método verifica o último dígito para detectar erros. Neste método serão verificadas duas quantidades de dígitos, uma com 15 e outra com 16 dígitos. E cada dígito será multiplicado por 1 ou 2 numa seqüência.
 -Ex: 1,2,1,2,1,2.
 -Para cartões com 15 dígitos a seqüência começa por 1 e os de 16 por 2. Os resultados serão somados e divididos por 10 se o resultado for 0 o número do cartão digitado e válido.
'''

import platform
import time
import os

so = platform.system()

def limpar():
    if  so == 'Windows':
	    os.system("cls")
    else:
	    os.system("clear")

cartoesValidos = []
cartoesInvalidos = []
todosCartoes = []

def novesFora(numero):
    resultado = 0
    numero = list(str(numero))
    for i in numero:
        resultado = resultado + int(i)
    return resultado

def impar(card):
    total = 0
    card = card[::2]
    for i in card:
        i = int(i)*2
        total = total + novesFora(i)
    return total

def par(card):
    total = 0
    card = list(card)
    card.pop(0)
    card = card[::2]
    for i in card:
        total = total + int(i)
    return total

def impar15(card):
    total = 0
    card = card[::2]
    for i in card:
        total = total + int(i)
    return total

def par15(card):
    total = 0
    card = list(card)
    total = total + novesFora(int(card[0])*2)
    card.pop(0)
    card = "".join(card)
    card = str(card)
    for i in card:
        i = int(i)*2
        total = total + novesFora(i)
    return total

def testar(numero):
    total = 0
    numero = str(numero)
    resultado = None
    quantidadeDeAlgarismos = len(numero)
    if quantidadeDeAlgarismos < 13 or quantidadeDeAlgarismos > 16:
        return "Invalid!"
    elif quantidadeDeAlgarismos == 15:
        total = par15(numero) + impar15(numero)
    else:
        total = par(numero) + impar(numero)
    if total % 10 == 0:
        resultado = "Valid!"
    else:
        resultado = "Invalid!"
    return resultado

def pegarNumerosDoArquivo(arquivo):
    arquivo = open(arquivo, "r")
    numeros = arquivo.readlines()
    lista = []
    for i in numeros:
        lista.append(i.replace('\n', ''))
    arquivo.close()
    return lista

def salvarTodos(cartoesValidos, cartoesInvalidos):
    #Cria arquivo e adiciona os cartoes validos.
    arquivo = open("AllCards.txt", 'w')
    arquivo.write("#######Valid Cards#######\n\n")
    arquivo.close()
    arquivo = open("AllCards.txt", 'a')
    for cartao in cartoesValidos:
        arquivo.write(cartao+"\n")
    arquivo.close()
    #Abre arquivo e adiciona os cartoes invalidos
    arquivo = open("AllCards.txt", 'a')
    arquivo.write("\n#######Invalid Cards#######\n\n")
    arquivo.close()
    arquivo = open("AllCards.txt", 'a')
    for cartao in cartoesInvalidos:
        arquivo.write(cartao+"\n")
    arquivo.close()

def salvarValidos(cartoesValidos):
    arquivo = open("ValidCardis.txt", 'w')
    for cartao in cartoesValidos:
        arquivo.write(str(cartao)+"\n")
    arquivo.close()

def salvarInvalidos(cartoesInvalidos):
    arquivo = open("InvalidCards.txt", 'w')
    for cartao in cartoesInvalidos:
        arquivo.write(str(cartao)+"\n")
    arquivo.close()

limpar()

op = int(input('''
                         ________________________
                        |                  ####  |
                        |                  VISA  |
                        | ####             ####  |
                        | ####                   |
                        |                        | 
                        |C4RD NUM8 B3RV 4L1D 4T0R|
                        |By   J4CK_              |
                        |________________________|



                        [!] BY TEXT FILE  -----> 1
                        [!] BY NUMBER     -----> 2

>>> '''))
try:
    if op == 1:
        arquivo = input("\nTYPE THE FILE NAME\n\n>>> ")
        cartoes = pegarNumerosDoArquivo(arquivo)
        for cartao in cartoes:
            resultado = testar(cartao)
            time.sleep(0.1)
            print(cartao+" -----> "+resultado)
            todosCartoes.append(cartao)
            if resultado == "Valid!":
                cartoesValidos.append(cartao)
            else:
                cartoesInvalidos.append(cartao)

        opSalvar = int(input('''
        
        
        [!] SAVE ONLY INVALID CARD NUMBERS         -----> 1
        [!] SAVE ONLY VALID CARD NUMBERS           -----> 2
        [!] SAVE ALL CARD NUMBERS                  -----> 3
        [!] ALL OPTIONS (RECOMENDED)               -----> 4  
        
>>> '''))
        if opSalvar == 1:
            salvarInvalidos(cartoesInvalidos)
        elif opSalvar == 2:
            salvarValidos(cartoesValidos)
        elif opSalvar == 3:
            salvarTodos(cartoesValidos, cartoesInvalidos)
        else:
            salvarInvalidos(cartoesInvalidos)
            salvarValidos(cartoesValidos)
            salvarTodos(cartoesValidos, cartoesInvalidos)
        print("Saved!")
    
    if op == 2:
        cartao = input("\n\nTYPE A CARD NUMBER\n\n>>> ")
        print("\n\n"+cartao+" -----> "+testar(cartao)+"\n\n")
    
except:
    print("\n\nERROR! TRY AGAIN OR CONTACT THE DEVELOPER\n\n")