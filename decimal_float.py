# Decimal module provides decimal floating point data type for precise precision

from decimal import *

# Calculate 105% of 0.70, decimal fp and binary fp
# Decimal keeps the trailing 0, automatically inferring four place significance
# from multiplicands with two place significance. Decimal reproduces 
# mathematics as done by hand and avoids issues that can arise when binary
#  floating point cannot exactly represent decimal quantities.
decimal_calc = round(Decimal('0.70') * Decimal('1.05'), 2)
bin_calc = round(0.70 * 1.05, 2)

print("Decimal: ", decimal_calc)
print("Binary: ", bin_calc)

# Exact representation enables the Decimal class to perform modulo calculations
#  and equality tests that are unsuitable for binary floating point
dec_mod = Decimal('1.00') % Decimal('0.10')
print(dec_mod)
binary_mod = 1.00 % 0.10
print(binary_mod)

d = sum([Decimal('0.10')] * 10) == Decimal('1.0')
print(d)
b = sum([0.1] * 10) == 1.0
print(b)

# decimal module provides as much precision as needed
getcontext().prec = 40
precision = Decimal(1) / Decimal(7)
print(precision)