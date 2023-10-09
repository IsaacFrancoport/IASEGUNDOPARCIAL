def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Intercambia el elemento mínimo encontrado con el elemento en la posición actual
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Lista original:", arr)
    selection_sort(arr)
    print("Lista ordenada:", arr)