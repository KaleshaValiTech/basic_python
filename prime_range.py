"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""
Example code:-
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=", ")

start = int(input("Enter start: "))
end = int(input("Enter end: "))
prime_numbers_in_range(start, end)

Example output:-
Enter start: 10  
Enter end: 30  
11, 13, 17, 19, 23, 29, 
