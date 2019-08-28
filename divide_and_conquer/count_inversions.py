# practice: https://practice.geeksforgeeks.org/problems/inversion-of-array/0


def merge(nums, tmp, left, mid, right):
    i, j, k = left, mid+1, left
    count = 0

    while i <= mid and j <= right:
        # There will be no inversion if arr[i] <= arr[j]
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            tmp[k] = nums[j]
            # Count the number of the range mid - i, they are bigger than nums[j]
            count += (mid-i+1)
            k += 1
            j += 1

    while i <= mid:
        tmp[k] = nums[i]
        k += 1
        i += 1

    while j <= right:
        tmp[k] = nums[j]
        k += 1
        j += 1

    # Copy the sorted subarray into Original array
    for x in range(left, right+1):
        nums[x] = tmp[x]

    return count


def merge_sort(nums, tmp, left, right):
    """
    Initialize tmp at here because when the nums is too long,
    It save a lot of time.
    """
    count = 0
    if left < right:
        mid = (left + right) >> 1
        count = merge_sort(nums, tmp, left, mid)
        count += merge_sort(nums, tmp, mid+1, right)
        count += merge(nums, tmp, left, mid, right)
    return count


if __name__ == '__main__':
    arr = [1, 20, 6, 4, 5]
    print(merge_sort(arr, [0]*len(arr), 0, len(arr)-1))
