def bubble_sort(collection):
    """Pure implement of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    length = len(collection)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
    return collection
