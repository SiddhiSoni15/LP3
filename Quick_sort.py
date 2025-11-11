import random
import time

# Partition function (Lomuto partition scheme)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Deterministic Quick Sort
def quick_sort_deterministic(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_deterministic(arr, low, pi - 1)
        quick_sort_deterministic(arr, pi + 1, high)

# Randomized partition
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

# Randomized Quick Sort
def quick_sort_randomized(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        quick_sort_randomized(arr, low, pi - 1)
        quick_sort_randomized(arr, pi + 1, high)

# Driver code
arr_input = list(map(int, input("Enter elements separated by space: ").split()))
arr1 = arr_input.copy()
arr2 = arr_input.copy()

# Deterministic Quick Sort
start = time.time()
if arr1:
    quick_sort_deterministic(arr1, 0, len(arr1) - 1)
end = time.time()
print("\nDeterministic Quick Sort Result:", arr1)
print("Execution Time: {:.6f} seconds".format(end - start))

# Randomized Quick Sort
start = time.time()
if arr2:
    quick_sort_randomized(arr2, 0, len(arr2) - 1)
end = time.time()
print("\nRandomized Quick Sort Result:", arr2)
print("Execution Time: {:.6f} seconds".format(end - start))



# Quick Sort is a divide and conquer sorting algorithm that works by selecting a pivot element and partitioning the array such that all elements smaller than the pivot are placed before it and all greater elements after it.
# In Deterministic Quick Sort, a fixed pivot (commonly the last or first element) is chosen, which can lead to worst-case O(n²) time for already sorted or adversarial inputs.
# In Randomized Quick Sort, the pivot is chosen randomly from the current subarray, which helps in reducing the probability of encountering the worst case.
# This randomization ensures that all permutations of input are equally likely, giving an expected time complexity of O(n log n).
# Quick Sort is often preferred because of its in-place sorting (requires minimal extra space) and excellent average-case performance.
# It is widely used in system libraries and database sorting where high performance is needed.
# However, it is not stable, meaning equal elements may not retain their original order.

# Version	                  Best Case	    Average Case	Worst Case	Space Complexity	Pivot Selection
# Deterministic Quick Sort	  O(n log n)	O(n log n)	     O(n²)	      O(log n)	          Fixed (e.g., last element)
# Randomized Quick Sort	      O(n log n)	O(n log n)       O(n²) 	      O(log n)	          Random element