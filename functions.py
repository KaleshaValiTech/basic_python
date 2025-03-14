"""
Working with python functions
"""
# Use the def kyword to define a function
def fx_name():
  pass

# create a function called sum_2 that takes two parameters
def sum_2(num1 = 0, num2 = 0):  # varibles defined here are parameters
  print(f"Number 1 = {num1} and Number 2 = {num2}")
  
sum_2(10, 2) # values that we pass to the parameters are called arguments
sum_2(num1=10, num2=30)

# Arbitary arguments *args
def sum_arb(*args):
  print(args)
  
sum_arb(1,2,3)
sum_arb(1,2,3,4,5)
sum_arb(1,2,3,4,5,6,7)

# Arbitary keyword arguments
def sum_kwarb(**kwargs):
  print(kwargs)
  
sum_kwarb(n1=1,n2=2)
sum_kwarb(n1=1,n2=2,n3=3)
sum_kwarb(n1=1,n2=2,n3=3,n4=4)

# f -> formatted string