"""
function bucket-sort(array, n) is
  buckets ← new array of n empty lists
  for i = 0 to (length(array)-1) do
    insert array[i] into buckets[msbits(array[i], k)]
  for i = 0 to n - 1 do
    next-sort(buckets[i])
  return the concatenation of buckets[0], ..., buckets[n-1]
"""


DEFAULT_BUCKET_SIZE = 5


def bucket_sort(collection, bucket_size=DEFAULT_BUCKET_SIZE):
    if len(collection) == 0:
        return collection

    min_value, max_value = (min(collection), max(collection))
    bucket_count = ((max_value - min_value) // bucket_size + 1)
    buckets = [[] for _ in range(bucket_count)]
    for i in range(len(collection)):
        buckets[int((collection[i] - min_value) // bucket_size)].append(collection[i])
    return sorted([buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i]))])
