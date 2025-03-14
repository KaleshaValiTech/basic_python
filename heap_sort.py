def heapify(arr, n, i):
    """Heapifies a subtree rooted at index i in a heap of size n."""
    largest = i  # Assume root is largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    print(f"\nHeapifying at index {i} with value {arr[i]}")
    print(f"Left child index {left} {'exists' if left < n else 'does not exist'}, ", 
          f"Value: {arr[left] if left < n else 'N/A'}")
    print(f"Right child index {right} {'exists' if right < n else 'does not exist'}, ",
          f"Value: {arr[right] if right < n else 'N/A'}")

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        print(f"Left child {arr[left]} is greater than current largest {arr[largest]}. Updating largest.")
        largest = left

    # Check if right child is larger than the largest so far
    if right < n and arr[right] > arr[largest]:
        print(f"Right child {arr[right]} is greater than current largest {arr[largest]}. Updating largest.")
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        print(f"Swapping {arr[i]} with {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"Heap after swap: {arr}")
        
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def max_heap(arr):
  n = len(arr)
  i = n // 2 - 1
  while i >= 0:
    heapify(arr, n, i)
    i-=1

def heap_sort(arr):
    """Main function to perform Heap Sort."""
    n = len(arr)

    # Step 1: Build a max heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root with last element
        heapify(arr, i, 0)  # Restore max heap property on reduced heap

# Given array
arr = [12, 11, 13, 5, 6, 7]
print("Original array", arr)
print()

heap_sort(arr)
print("Sorted array", arr)