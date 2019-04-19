def max_heapify(lst, index):
    pass


def heap_sort(collection):
    """Pure implementation of the heap sort algorithm in Python

    :param collection: ome mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    n = len(collection)

    # build a max heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(collection, i)

    for i in range(len(collection) - 1, 0, -1):
        collection[0], collection[i] = collection[i], collection[0]
        max_heapify(collection, i)
    return collection
