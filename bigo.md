# Big O

Big O notation is a mathematical concept used in computer science to describe the efficiency of algorithms in terms of time and space complexity. It helps us analyze how an algorithm's performance scales as the size of the input increases.

It defines the runtime of your algorithm based on the input size.

## Time Space Complexity

```python

# Assuming input is an Array or List

input = [1, 2, 3, 4, 5]

def cal_sum(input):
  sum = 0           # Statement 1
  for(i in input):
    sum = sum + i   # Statement 2

  return sum        # Statement 3

  # Statement 1 is executed 1 time
  # Statement 2 is executed 5 times
  # Statement 3 is executed 1 time
  # Total = [input.size] + 2 execution
```

### In Big O, there are six major types of complexities (time and space):

 - Constant: O(1)
 - Linear time: O(n)
 - Logarithmic time: O(n log n)
 - Quadratic time: O(n^2)
 - Exponential time: O(2^n)
 - Factorial time: O(n!)

**Constant - O(1)**

When your algorithm is not dependent on the input size `n`, it is said to have a constant time complexity with order O(1). This means that the run time will always be the same regardless of the input size.

**Linear Time - O(n)**

When a function has an iteration that iterates over an input size of n, it is said to have a time complexity of order O(n).

**Logarithm Time - O(log n)**

This is similar to linear time complexity, except that the runtime does not depend on the input size but rather on half the input size. When the input size decreases on each iteration or step, an algorithm is said to have logarithmic time complexity.


## Importance 

- Allow us to compare and select alogrithms based on their efficiencies
- Focus on Worst Case Scenario and Best Case Scenario

```python
  
  arr = [1, 2, 5, 6, 7, 3, 9]
  
  # If num_to_find = 9 then it is found at last,  Worst Case Scneario
  # If num_to_find = 1 then it is found at first, Best Case Scneario

  ```
