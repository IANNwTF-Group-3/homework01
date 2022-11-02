import cat

# 2.1 Objects and modules
susan = cat.Cat("Susan")
rolf = cat.Cat("Rolf")

print(susan.greet(rolf))
print(rolf.greet(susan))

# 2.2 List comprehension
listSquares = [x*x for x in range(100)]
print(listSquares)

listSquaresEven = [x*x for x in range(100) if x%2==0]
print(listSquaresEven)

# 2.3 Generators
def generator_func():
    calling = 1
    while True:
        meows = ["Meow" for _ in range(calling)]
        calling *= 2
        yield ' '.join(meows)

i = 0
for meows in generator_func():
    print(meows)
    i += 1
    if i == 4:
        break

# 2.4 NumPy

# Create a 5x5 NumPy array filled with normally distributed (i.e. μ = 0, σ = 1)
import numpy as np

a = np.random.normal(size=(5,5))
print(a)

npwhere = np.where(a > 0.09, a*a, 42)
print(npwhere)

print(npwhere[:, 3])

