def heapify(lst, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and lst[left_index] > lst[largest]:
        largest = left_index

    if right_index < heap_size and lst[right_index] > lst[largest]:
        largest = right_index

    if largest != index:
        lst[largest], lst[index] = lst[index], lst[largest]
        heapify(lst, largest, heap_size)


def heap_sort(collection):
    """Pure implement of heap sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    n = len(collection)
    for i in range(n // 2 - 1, -1, -1):
        heapify(collection, i, n)
    for i in range(n - 1, 0, -1):
        collection[0], collection[i] = collection[i], collection[0]
        heapify(collection, 0, i)
    return collection
