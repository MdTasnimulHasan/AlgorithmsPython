def QuickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return QuickSort(left) + middle + QuickSort(right)

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = QuickSort(my_list)
print(sorted_list)