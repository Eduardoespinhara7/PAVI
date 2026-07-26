import math

def F(x):
  return x**3/ 3
  
a = 0
b = 1
  
integral1 = F(b) - F(a)

def F(x):
  return -math.cos(x)
  
  
a = 0 
b = math.pi

integral2 = F(b) - F(a)

def F(x):
  return math.exp(x)
  
  
a = 0
b = 1

integral3 = F(b) - F(a)

print(integral1)
print(integral2)
print(integral3)
