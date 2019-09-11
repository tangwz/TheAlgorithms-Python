def counting_sort(collection):
    if not collection:
        return
    maximum = max(collection)
    count = [0] * (maximum + 1)
    for i in collection:
        count[i] += 1

    k = 0
    for i in range(maximum+1):
        for j in range(count[i]):
            collection[k] = i
            k += 1

    return collection


if __name__ == '__main__':
    print(counting_sort([5, -5, 7, 8, 2, 4, 1]))
