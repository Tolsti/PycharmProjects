import random

array = [random.randint(1, 100) for i in range(10)]


def bubble_sort(arr):
    for lap in range(len(arr) - 1):
        for i in range(len(arr) - 1 - lap):
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
    return arr


print(array)
print(bubble_sort(array))
