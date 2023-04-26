import datetime

def bubble_sort(arr):
    n = len(arr)
    # Parcourt tous les éléments du tableau
    for i in range(n):
        # On va jusqu'à n-i-1 car les i derniers éléments sont déjà triés
        for j in range(n-i-1):
            # Si l'élément courant est plus grand que le suivant, on les échange
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Trouver l'élément minimum restant dans la liste non triée
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Échanger l'élément minimum avec l'élément actuel
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)


def fastest(lst):
    start_time = datetime.datetime.now()
    bubble_sort(lst)
    end_time = datetime.datetime.now()
    t1 = (end_time - start_time).total_seconds()

    start_time = datetime.datetime.now()
    selection_sort(lst)
    end_time = datetime.datetime.now()
    t2 = (end_time - start_time).total_seconds()

    start_time = datetime.datetime.now()
    insertion_sort(lst)
    end_time = datetime.datetime.now()
    t3 = (end_time - start_time).total_seconds()

    start_time = datetime.datetime.now()
    quicksort(lst)
    end_time = datetime.datetime.now()
    t4 = (end_time - start_time).total_seconds()


    if t1 < t2 and t1 < t3 and t1 < t4:
        return (1)
    if t2 < t1 and t2 < t3 and t2 < t4:
        return (2)
    if t3 < t1 and t3 < t2 and t3 < t4:
        return (3)
    if t4 < t1 and t4 < t2 and t4 < t3:
        return (4)
