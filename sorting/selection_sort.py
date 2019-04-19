def selection_sort(collection):
    for i in range(len(collection)):
        min_index = i
        for j in range(i+1, len(collection)):
            if collection[min_index] > collection[j]:
                min_index = j
        if i != min_index:
            collection[i], collection[min_index] = collection[min_index], collection[i]
    return collection
