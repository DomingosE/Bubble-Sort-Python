def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Últimos i elementos já estão classificados
        for j in range(n - i - 1):
            # Troca se o elemento atual for maior do que o próximo
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print("Array desordenado:")
print(arr)

arr_ordenado = bubble_sort(arr)

print("Array ordenado:")
print(arr_ordenado)