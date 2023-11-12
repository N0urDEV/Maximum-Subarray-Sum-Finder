def max_subarray_sum(arr):
    n = len(arr)
    if n == 0:
        return None 

    somme_max = arr[0]
    somme_courante = arr[0]

    for i in range(1, n):
        somme_courante = max(arr[i], somme_courante + arr[i])
        somme_max = max(somme_max, somme_courante)

    return somme_max
 

tableau = [int(x) for x in input("Enter numbers for the array (space-separated): ").split()]
result = max_subarray_sum(tableau)
print("La somme maximale est:", result)
