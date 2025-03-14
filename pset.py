"""
Set in python
Set is unordered, unchangeable and unindexed
created using {}
"""

fruits = {"apple", "orange", "grapes", "apple", False, 0, True, 1}
tropical = {"pineapple", "mango", "papaya"}
fruits.update(tropical)

print(fruits)
print(len(fruits))

for fruit in fruits:
  print(f"Fruit is {fruit}")
  
fruits.remove("apple")
print(fruits)

fruits.discard("apple")
print(fruits)

tropical.clear()

del fruits