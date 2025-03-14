# Linear Search and Binary Search

## Linear Search

Linear Search is a simple searching algorithm that sequentially checks each element of the array until the target element is found or the array ends.

### Algorithm

- Start from the first element.
- Compare each element with the target value.
- If a match is found, return the index.
- If the end of the array is reached without finding the target, return -1.

### Pseudocode
```csharp
    for i from 0 to length(arr) - 1:
        if arr[i] == target:
            return i
        else
          return -1
```

## Binary Search

Binary Search is a more efficient searching algorithm but requires a sorted array. It uses a divide-and-conquer approach.

### Algorithm:

- Set low to the first index and high to the last index.
- Find the middle element:
    mid = (low + high) // 2
- If arr[mid] == target, return mid.
- If arr[mid] > target, search in the left half (high = mid - 1).
- If arr[mid] < target, search in the right half (low = mid + 1).
- Repeat steps 2-5 until low > high.