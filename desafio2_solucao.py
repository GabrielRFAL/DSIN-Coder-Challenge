# Frase a ser decifrada - PLANETAKIXZTLNLKORBITAKOTVNHKRADIACAO
# Código CODER - 231289528980975032

def string_to_list(a):
    list = [i for i in a]
    return list

def palavra_par(p):
    nova_palavra_par = ''
    for letra in p:
        novo_indice = alfabeto.index(letra) + chave_par_final
        if novo_indice > 25:
            novo_indice -= 26
        nova_palavra_par += alfabeto[novo_indice]
    return nova_palavra_par

def palavra_impar(p):
    nova_palavra_impar = ''
    for letra in p:
        novo_indice = alfabeto.index(letra) + chave_impar_final
        if novo_indice > 25:
            novo_indice -= 26
        nova_palavra_impar += alfabeto[novo_indice]
    return nova_palavra_impar

palavra_inicial = 'PLANETAKIXZTLNLKORBITAKOTVNHKRADIACAO'
codigo_coder = '231289528980975032'

# Passo 1 - Identificar a letra que corresponde ao 'Espaço' para remove-la do sinal.
# Passo 1a - somando os dígitos do código CODER.

soma_digitos = 0

for i in codigo_coder:
    if i.isdigit():
        soma_digitos += int(i)
print(f'A soma dos dígitos do código CODER é: {soma_digitos}')

# Passo 1b - Checar se a soma dos dígitos é maior que 26 
# e somar os dígitos para obter um novo valor. ex: 83 é maior 
# que 26, portanto, somar o 8 e 3, até que a soma seja menor ou igual a 26.

digitos_da_soma = sum(int(digito) for digito in str(soma_digitos))

while True:
    if digitos_da_soma <= 26:
        break

print(f'A nova soma dos dígitos é: {digitos_da_soma}')

# Passo 1c - Mapear o número obtido na etapa anterior(1b) para 
# a letra correspondente no alfabeto (ex: A -> 1, B -> 2, ..., Z -> 26).

alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
    'Y', 'Z'
]

letra_espaco = alfabeto[digitos_da_soma - 1]  # Usa-se o -1, porque a lista começa em 0 e nosso desafio utiliza o A como 1.
print(f'A letra correspondente ao "Espaço" é: {letra_espaco}')

# Passo 1d - Remover da palavra inicial a letra descoberta, deixando 
# espaços no lugar.

palavra_inicial_com_espaco = palavra_inicial.replace(letra_espaco, ' ')
print(f'A palavra inicial com espaço é: {palavra_inicial_com_espaco}')

# Antes de decodificar as palavras vamos transformá-las em digitos.

palavra_inicial_lista = string_to_list(palavra_inicial)
print(f'A palavra inicial em lista é: {palavra_inicial_lista}')

palavra_inicial_digitos = []

for letra in palavra_inicial_lista:
    palavra_inicial_digitos.append(alfabeto.index(letra))
print(f'A palavra incial em dígitos é: {palavra_inicial_digitos}')

# Passo 2 - Decodificando cada palavra entre os espaços.
# Passo 2a - Chaves de decodificação.
# Passo 2a i - Chave de letra ímpares.

chave_impar = 0

for digito in codigo_coder:
    if int(digito) % 2 != 0:
        chave_impar += int(digito)

chave_impar_final = chave_impar % 26 + 1
print(f'A chave de letras ímpares é: {chave_impar_final}')

# Passo 2a ii - Chave de letra par.

chave_par = 0

for digito in codigo_coder:
    if int(digito) % 2 == 0:
        chave_par += int(digito)

chave_par_final = chave_par % 26 + 1
print(f'A chave de palavras par final é: {chave_par_final}')

# Passo 2b - Decodificando cada palavra

palavra_inicial += 'K'  # Colocar o 'K' no final que seria outro "Espaço" para poder dar o append na última palavra.
palavras_finais = []
palavra = ''

for i in palavra_inicial:
    if i == 'K':
        palavras_finais.append(palavra)
        palavra = ''
    else:
        palavra += i

# Passo final - Utilizando as chaves decodificadores para encontrar 
# as palavras.

print(
    f'A primeira palavra é: {palavra_impar(palavras_finais[0])}, '  # Primeira palavra da frase.
    f'A segunda palavra é: {palavra_par(palavras_finais[1])}, '  # Segunda palavra da frase.
    f'A terceira palavra é: {palavra_impar(palavras_finais[2])}, '  # Terceira palavra da frase.
    f'A quarta palavra é: {palavra_par(palavras_finais[3])}, '  # Quarta palavra da frase.
    f'A quinta palavra é: {palavra_impar(palavras_finais[4])}'  # Quinta palavra da frase.
)
