def insertion_sort(collection):
    for i in range(1, len(collection)):
        for j in range(i, 0, -1):
            if collection[j] < collection[j-1]:
                collection[j], collection[j-1] = collection[j-1], collection[j]
            else:
                break
    return collection
