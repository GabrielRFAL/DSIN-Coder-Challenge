def seq_action(a):
    acao = str(dici_matriz[int(a)])
    return acao

def troca_cor(l, c):
    indice_novo = 0
    #print(f'Cor da posição da matriz [{l},{c}]: {matriz[l][c]}')
    indice_novo = seq(matriz[l][c])
    matriz[l][c] = indice_novo
    #print(f'Indice novo da cor nova: {indice_novo}')
    return matriz

def seq(x):
    indice = sequencia.index(x)
    indice_new = indice + 1
    #print(f'Indice da cor na lista de sequencia: {indice}')
    if indice_new > 4:
        indice_new = 0
    return sequencia[indice_new]


sequencia = ['A', 'B', 'C', 'D', 'E']
#l = []
#c = []
matriz = [['A', 'B', 'C'], 
          ['C', 'A', 'E'], 
          ['A', 'B', 'C']
          ]

dici_matriz = {
    1: [1, 2, 4, 5],  # muda a cor das vizinhas
    2: [2, 1, 3],  # muda a cor das vizinhas na horizontal
    3: [3, 2, 5],  # muda a cor das vizinhas na horizontal e diagonal
    4: [4, 2, 8],  # muda a cor das vizinhas na diagonal
    5: [5, 2, 8],  # muda a cor das vizinhas na vertical
    6: [6, 2, 8],  # muda a cor das vizinhas na diagonal
    7: [7, 8],  # muda a cor das vizinhas na horizontal
    8: [8, 7, 9, 5],  # muda a cor das vizinhas na horizontal e vertical
    9: [9, 6, 5]  # muda a cor das vizinhas na vertical e diagonal
}

dici_index_matriz = {
    '1': [0,0],
    '2': [0,1],
    '3': [0,2],
    '4': [1,0],
    '5': [1,1],
    '6': [1,2],
    '7': [2,0],
    '8': [2,1],
    '9': [2,2]
}

realizar_acao = ''

codigo = '2312895289897532'
for i in codigo:
    realizar_acao += seq_action(i)

realizar_acao = realizar_acao.replace('[', '').replace(']', ',').replace(' ', '').replace(',', '').replace(' ', '')
print(f'Código: {codigo}')
print(f'Sequencia de ações: {realizar_acao}')
print(f'Matriz original:')
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')

# print(matriz[0][0])
# print(dici_matriz)

for i in realizar_acao:
    # print(i)
    # print(dici_index_matriz[i])
    linha = dici_index_matriz[i][0]
    coluna = dici_index_matriz[i][1]
    # print(linha)
    # print(coluna)
    print('------------------------'*3)
    troca_cor(linha, coluna)
    print(f'Matriz modificada na célula {i}:')
    print(f'{matriz[0]}')
    print(f'{matriz[1]}')
    print(f'{matriz[2]}')
print('------------------------'*3)
print(f'Matriz nova:')
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')