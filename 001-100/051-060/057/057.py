import itertools
from fractions import Fraction

# Spitter function taken from https://rosettacode.org/wiki/Continued_fraction#Python
# This would have taken me a long time without that code

try:
    zip = itertools.izip
except:
    pass

# The Continued Fraction

def CF(a, b, t):
  terms = list(itertools.islice(zip(a, b), t))
  z = Fraction(1, 1)
  for a, b in reversed(terms):
    z = a + b / z
  return z

def sqrt2_a():
    yield 1
    for x in itertools.repeat(2):
        yield x

def sqrt2_b():
  for x in itertools.repeat(1):
    yield x

counter = 0

for i in range(1002):
    fraction = 2 / CF(sqrt2_a(), sqrt2_b(), i)
    if len(str(fraction.numerator)) > len(str(fraction.denominator)):
        counter += 1
    if i % 100 == 0:
        print(i)

print(counter)
