# Data-Structure-and-Algorithm
My data structure and Algorithm activities
# Activity 1: Array Operations - Data Structures and Algorithms
# Name: [Elden Ryan Piloton]
# Section: [BSIT 2B]

def display(arr):
    print("Array:", arr)

def insert(arr, value, position):
    arr.insert(position, value)
    return arr

def delete(arr, value):
    if value in arr:
        arr.remove(value)
    return arr

def search(arr, value):
    return arr.index(value) if value in arr else -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test
my_array = [10, 5, 20, 8, 15]
display(my_array)
print("After insert 99 at position 2:", insert(my_array, 99, 2))
print("After delete 5:", delete(my_array, 5))
print("Search 20 found at index:", search(my_array, 20))
print("Sorted:", bubble_sort(my_array))
