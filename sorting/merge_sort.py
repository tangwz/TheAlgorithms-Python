def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    mid = length // 2
    left = collection[:mid]
    right = collection[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
