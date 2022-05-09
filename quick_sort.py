import random
import datetime


def get_pivot(arr):
    random.seed(datetime.datetime.now())
    return random.choice(range(len(arr)))


def partition(arr, l, r):
    global comparisons
    comparisons += (r - l - 1)
    pivot_value = arr[l]
    after_pivot = l + 1
    for index in range(l + 1, r):
        if arr[index] <= pivot_value:            
            arr[index], arr[after_pivot] = arr[after_pivot], arr[index]
            after_pivot += 1
    arr[l], arr[after_pivot-1] = arr[after_pivot-1], arr[l]
    return after_pivot - 1


def merge_sort(arr, left, right):
    if left >= right:
        return arr
    arr[left], arr[right - 1] = arr[right- 1], arr[left]
    pivot_index = partition(arr, left, right)
    merge_sort(arr, left, pivot_index)
    merge_sort(arr, pivot_index + 1, right)

    return arr
     



arr = [12, 3, 4, 10, 1, 15, 8, 6, 0, 13, 11, 2, 5, 7, 9, 14]
comparisons = 0
with open("qs_array.txt", "r") as f:
    arr = [int(i) for i in f]


merge_sort(arr, 0, len(arr))
# print(f"Result: {arr}")
print(f"Comparisons: {comparisons}")

