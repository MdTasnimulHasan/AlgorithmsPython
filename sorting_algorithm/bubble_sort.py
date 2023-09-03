def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break
    return arr

a = [1,3,4,2,5,9,8,7]
sorted_a = BubbleSort(a)
print(sorted_a)
