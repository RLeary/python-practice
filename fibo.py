# fibonacci numbers module

# write fibonacci numbers up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

#return fibonacci numbers up to n
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# With this, this function can be run as a script, as python fibo.py <args>
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))