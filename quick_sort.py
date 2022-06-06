import random
import datetime


def get_pivot(arr, l, r):
    random.seed(datetime.datetime.now())
    # right = r + 1 if r < len(arr) else len(arr)
    return get_median(arr, l, r)
    return (l + r) // 2
    return random.choice(range(len(arr[l:right])))


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


def get_median(arr, l, r):
    if l >= r:
        return max(arr[l:r])

    temp_arr = arr[l:r]
    first_val = temp_arr[0]
    last_val = temp_arr[-1]
    middle_val = temp_arr[(len(temp_arr) // 2) - 1]
    selection_pool = [first_val, middle_val, last_val]
    exclusion_pool = [max(temp_arr), min(temp_arr)]
    print(selection_pool, exclusion_pool)
    result_arr = [num for num in selection_pool if num not in exclusion_pool]
    return result_arr[0]
    


def quick_sort(arr, left, right):
    # import pdb
    # pdb.set_trace()
    if left >= right:
        return arr
    # arr[left], arr[right - 1] = arr[right- 1], arr[left]
    pivot = get_pivot(arr, left, right)
    if pivot != left:
        arr[pivot], arr[left] = arr[left], arr[pivot]
    pivot_index = partition(arr, pivot, right)
    quick_sort(arr, left, pivot_index)
    quick_sort(arr, pivot_index + 1, right)

    return arr
     



arr = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
arr = [4, 1, 5, 2, 3, 0]
comparisons = 0
# with open("qs_array.txt", "r") as f:
#     arr = [int(i) for i in f]


quick_sort(arr, 0, len(arr))
print(f"Result: {arr}")
print(f"Comparisons: {comparisons}")

