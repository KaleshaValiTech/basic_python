"""
  List and Tuple
  A list is a mutable, ordered collection that can hold a mix of different data types. 
  Lists are defined using square brackets [ ].
  
  Features
  They are ordered
  Allow Duplicates
  Mutable
  Hetrogenous
  Dynamic
"""

fruits = ["banana", "apple", "orange"]
numbers = [3,1,5,2,8]
mixed = [1,2,True,"Hello"]

fruits.sort()
print(fruits)
print(fruits, numbers, mixed)
print(fruits[1], numbers[3], mixed[2])

fruits.insert(0, "mango")
print(fruits)
fruits.append("grape")
print(fruits)

print("removing")
fruits.remove("banana")
print(fruits)
print(fruits.pop())
print(fruits)

numbers.sort()
print(numbers)

# mixed.sort() Cannot sort
# print(mixed)

"""
Tuple - A tuple is an immutable, ordered collection of elements. 
Tuples are defined using parentheses ( ).
"""

books = ("1984", "Great Gatsby")
books2 = ("Old man and the sea")

user = ("ashish.s", "password", "ashish.s.panicker")
user_name, password, email = user
print(user_name, password, email)

fruits_tuple = tuple(fruits) # convert list to tuple