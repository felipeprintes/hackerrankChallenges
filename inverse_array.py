"""
Objetivo: receber um array e imprimir o resultado
na ordem inversa.
Exemplo:
arr = [1,2,3]
arr_result = [3,2,1]
"""


# Função responsável pela regra de retornar
# o vetor na ordem inversa
def reverse(arr):
    # vetor auxiliar
    arr_result = []
    # variavel que irá receber o último indexe do vetor
    tam = len(arr) - 1

    # loop com o papel de percorre o 'arr' do último
    # elemento até o primeiro e adicionando esse elemento no arr_result
    while tam >= 0:
        arr_result.append(arr[tam])
        tam -= 1
    return arr_result


if __name__ == '__main__':
    # variavel n que irá receber o tamanho do array
    n = int(input())
    arr = list(map(int, input().strip().split()))
    result = reverse(arr)
    print(result)
