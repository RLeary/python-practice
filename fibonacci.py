#import fibo
#
#print(fibo.fib(20))
#fibonacci_numbers = fibo.fib2(100)
#print(fibonacci_numbers)
#print(fibo.__name__)
#
# functions in other modules can be assigned local names
#fibonacci = fibo.fib2
#fibonacci_numbers2 = fibonacci(600)
#print(fibonacci_numbers2)

# can import names directly from a module
from fibo import fib, fib2
print(fib(20))

fibonacci_numbers = fib2(100)
print(fibonacci_numbers)