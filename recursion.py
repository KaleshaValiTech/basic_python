
"""
Factorial of a number
"""
def factorial(num):
  result = 1
  for i in range(2, num+1):
    result *= i
  return result

def factorial_rec(num):
  if num == 0 or num == 1: # Base case
    return 1
  return num * factorial_rec(num-1)
