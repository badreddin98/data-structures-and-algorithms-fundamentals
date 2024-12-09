# Simple sorting algorithm analysis
# This is my implementation and analysis of the bubble sort algorithm

import time
import random

def simple_sort(arr):
    # My implementation of bubble sort
    # I chose this because it's straightforward to analyze
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    
    return comparisons, swaps

def test_sorting_performance():
    # Testing the performance with different array sizes
    print("\nTesting sorting performance:")
    print("\nSize | Time (ms) | Comparisons | Swaps")
    print("-" * 40)
    
    # Testing with different sizes to see how performance scales
    for size in [10, 100, 1000]:
        test_arr = [random.randint(1, 1000) for _ in range(size)]
        
        start = time.time()
        comps, swaps = simple_sort(test_arr.copy())
        end = time.time()
        
        ms_time = (end - start) * 1000
        print(f"{size:^4} | {ms_time:^9.2f} | {comps:^11} | {swaps:^5}")

# Main program
if __name__ == "__main__":
    print("My Analysis of Bubble Sort Algorithm")
    print("\nTime Complexity Analysis:")
    print("- O(n²) because of the nested loops")
    print("- Each element might need to bubble up through the entire array")
    
    print("\nSpace Complexity:")
    print("- O(1) since it sorts in-place")
    print("- Only needs a few variables for swapping")
    
    test_sorting_performance()
    
    print("\nPossible Improvements:")
    print("1. Could use QuickSort for O(n log n) average performance")
    print("2. Or MergeSort for guaranteed O(n log n)")
    print("3. Bubble sort is fine for very small arrays though")
