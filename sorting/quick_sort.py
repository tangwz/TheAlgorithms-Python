def quick_sort(collection):
    """Pure implement of bubble sort algorithm in Python

    :param collection: ome mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """

    def partition(lst, left, right):
        pivot = lst[left]
        i = left
        j = right
        while j > i:
            while lst[j] >= pivot and j > i:
                j -= 1
            while lst[i] <= pivot and j > i:
                i += 1
            if j > i:
                lst[i], lst[j] = lst[j], lst[i]
        lst[left], lst[i] = lst[i], lst[left]
        return i

    def sort(lst, left, right):
        if left >= right:
            return
        p = partition(lst, left, right)
        sort(lst, left, p - 1)
        sort(lst, p + 1, right)

    sort(collection, 0, len(collection) - 1)
    return collection


def quick_sort_v2(collection):
    """Pure implement of bubble sort algorithm in Python

    :param collection: ome mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """

    def partition(lst, left, right):
        pivot = lst[left]
        i = left
        j = right
        while j > i:
            while lst[j] >= pivot and j > i:
                j -= 1
            lst[i] = lst[j]
            while lst[i] <= pivot and j > i:
                i += 1
            lst[j] = lst[i]
        lst[i] = pivot
        return i

    def sort(lst, left, right):
        if left >= right:
            return
        p = partition(lst, left, right)
        sort(lst, left, p - 1)
        sort(lst, p + 1, right)

    sort(collection, 0, len(collection) - 1)
    return collection
