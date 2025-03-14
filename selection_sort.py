"""

Algorithm
------------------------------
1. Start
2. Find the smallest element in the array and swap it with the first 
3. Move to the next element and repeat this process till array is sorted
4. Stop

Given Array [29, 10, 14, 37, 13]

Pass 1
Index  = 0
Min Value: 10
Swap 10 With 29
Array : [10, 29, 14, 37, 13]

Pass 2
Index = 1
Min Value: 13
Swap 13 With 29
Array : [10, 13, 14, 37, 29]

Pass 3
Index  = 2
Min Value: 14
No Swap needed
Array : [10, 13, 14, 37, 29]

"""

def selection_sort(arr):
  n = len(arr) # Return the length of array
  i = 0
  while i < n - 1:
    min_index = i
    j = i + 1
    while j < n:
      if arr[j] < arr[min_index]:
        min_index = j
      j += 1
    # Swap the min value with the array index value
    arr[i], arr[min_index] = arr[min_index], arr[i]

    print(f"Step {i+1}: {arr}")

    i += 1

arr = [29, 10, 14, 37, 13]
print(f"Original Array: {arr}")
selection_sort(arr)
print(f"Sorted Array: {arr}")