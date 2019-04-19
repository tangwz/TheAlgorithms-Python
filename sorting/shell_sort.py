def shell_sort(collection):
    """Pure implement of shell sort algorithm in Python

    :param collection: ome mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    n = len(collection)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j-gap]
                j -= gap
            collection[j] = temp
        gap = gap // 2
    return collection


def shell_sort_v2(collection):
    """Pure implement of bubble sort algorithm in Python

    :param collection: ome mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    n = len(collection)
    # Using Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        i = gap
        while i < n:
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j-gap]
                j -= gap
            collection[j] = temp
            i += 1
    return collection
