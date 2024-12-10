###############

texto = "texto de exemplo, na terceira aula de python"

novo_texto = texto.replace(",","")
palavras = novo_texto.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] = +1
    else:
        contagem[palavra] = 1