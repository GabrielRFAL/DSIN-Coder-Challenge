# Código - PLANETAKIXZTLNLKORBITAKOTVNHKRADIACAO

def soma(a):
    somatoria = sum(a)
    return somatoria

def string_to_list(a):
    list = [i for i in a]
    return list

def palavra_par(p):
    nova_palavra_par = ""
    for letra in p:
        novo_indice = alfabeto.index(letra) + chave_par_final
        # print(novo_indice)
        if novo_indice > 25:
            novo_indice -= 26
        nova_palavra_par += alfabeto[novo_indice]
        # print(nova_palavra_par)
    return nova_palavra_par

def palavra_impar(p):
    nova_palavra_impar = ""
    for letra in p:
        novo_indice = alfabeto.index(letra) + chave_impar_final
        # print(novo_indice)
        if novo_indice > 25:
            novo_indice -= 26
        nova_palavra_impar += alfabeto[novo_indice]
        # print(nova_palavra_impar)
    return nova_palavra_impar


# Passo 1a - Somando os dígitos do código inicial

palavra_inicial = "PLANETAKIXZTLNLKORBITAKOTVNHKRADIACAO"
codigo_coder = "231289528980975032"
soma_digitos = 0

for i in codigo_coder:
    if i.isdigit():  # .isalpha() funciona como o .isdigit() só que para letras.
        soma_digitos += int(i)

print(f"Soma dos dígitos do CÓDIGO CODER: {soma_digitos}")

# Passo 1b - Checar se a soma dos dígitos é maior que 26 
# e somar os dígitos para obter um novo valor

# digitos_da_contagem = 0

# if soma_digitos > 26:
#     while soma_digitos > 0:
#         digitos_da_contagem += soma_digitos % 10  # digito_da_contagem = 7
#         soma_digitos //= 10  # soma_digitos = 3

# print(digitos_da_contagem)
digitos_da_contagem = sum(int(digito) for digito in str(soma_digitos))
# print(digitos_da_contagem)

while True:
    if digitos_da_contagem <= 26:
        break    
    novo_valor = sum(int(digito) for digito in str(digitos_da_contagem))

print(f"Soma dos dígitos do resultado: {digitos_da_contagem}")

# Passo 1c - Mapear o número obtido na etapa anterior para a letra correspondente no 
# alfabeto (ex: 1 -> A, 2 -> B, ..., 26 -> Z)

alfabeto = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

letra_espaco = alfabeto[digitos_da_contagem - 1]  # Tira 1, porque o A = 1.
print(f"A letra correspondente ao 'Espaço' é: {letra_espaco}")

# print(len(alfabeto))
# print(alfabeto[digitos_da_contagem])

# Passo 1d - Remover do sinal a letra descoberta, deixando espaços no lugar.

codigo_com_espaco = palavra_inicial.replace(alfabeto[digitos_da_contagem], " ")
# print(codigo_com_espaco)

# Transformando o Código Inicial em números (digitos)
lista_codigo_inicial = string_to_list(palavra_inicial)
print(f' isso aki {lista_codigo_inicial}')
lista_digitos_codigo_inicial = []

for letra in lista_codigo_inicial:
    lista_digitos_codigo_inicial.append(alfabeto.index(letra))
    # print(alfabeto.index(letra) + 1)

print(lista_digitos_codigo_inicial)
# Passo 2 - Decodificando cada palavra
# Passo 2a - Chave de letras ímpares

chave_impar = 0  # Resultado para dar certo 26.

for digito in codigo_coder:
    if int(digito) % 2 != 0:
        chave_impar += int(digito)

chave_impar_final = chave_impar % 26 + 1
print(f"A chave de letra impar é: {chave_impar_final}")

chave_par = 0  # Resultado para dar certo 7.

for digito in codigo_coder:
    if int(digito) % 2 == 0:
        chave_par += int(digito)

chave_par_final = chave_par % 26 + 1
print(f"A chave de letra par é: {chave_par_final}")

# Decodificando cada palavra
    # Palavras ímpares

palavra_inicial += "K"  # Coloca-se o "K" no final da palavra para dar append na última palavra.
palavra_separada_por_espaco = []
palavra = ""

for i in palavra_inicial:
    if i == "K":
        palavra_separada_por_espaco.append(palavra)
        palavra = ""
    else:
        palavra += i

print(palavra_impar(palavra_separada_por_espaco[0]))
print(palavra_par(palavra_separada_por_espaco[1]))
print(palavra_impar(palavra_separada_por_espaco[2]))
print(palavra_par(palavra_separada_por_espaco[3]))
print(palavra_impar(palavra_separada_por_espaco[4]))