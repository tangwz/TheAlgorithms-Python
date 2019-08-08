def binary_search(sorted_collection, target):
    """
    :param sorted_collection:  some ascending sorted collection with comparable items.
    :param target: target value to search
    :return: index of found target or -1 if target is not fount

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search([0, 5, 7, 10, 15], 6)
    -1

    >>> binary_search([1, 2, 2, 2, 2, 3], 2)
    2

    >>> binary_search([1, 2, 2, 2, 3], 2)
    2
    """
    left, right = 0, len(sorted_collection) - 1
    while left <= right:
        mid = (left + right) >> 1
        if sorted_collection[mid] == target:
            return mid
        elif sorted_collection[mid] < target:
            left = mid + 1
        elif sorted_collection[mid] > target:
            right = mid - 1
    return -1


def binary_search_lower_bound(sorted_collection, target):
    """
    Examples:
    >>> binary_search_lower_bound([1, 2, 2, 2, 2, 3], 2)
    1

    >>> binary_search_lower_bound([1, 2, 2, 2, 3], 2)
    1

    >>> binary_search_lower_bound([1, 2, 5, 5, 5, 9], 5)
    2
    """
    left, right = 0, len(sorted_collection) - 1
    while left < right:
        mid = (left + right) >> 1
        if sorted_collection[mid] < target:
            left = mid + 1
        else:
            right = mid
    if sorted_collection[left] != target:
        return -1
    return left


def binary_search_up_bound(sorted_collection, target):
    """
    Examples:
    >>> binary_search_up_bound([1, 2, 2, 2, 2, 3], 2)
    4

    >>> binary_search_up_bound([1, 2, 2, 2, 3], 2)
    3

    >>> binary_search_up_bound([1, 2, 5, 5, 5, 9], 5)
    4
    """
    left, right = 0, len(sorted_collection) - 1
    while left < right:
        mid = (left + right) >> 1
        if sorted_collection[mid] > target:
            right = mid
        else:
            left = mid + 1
    if sorted_collection[left-1] != target:
        return -1
    return left - 1


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
