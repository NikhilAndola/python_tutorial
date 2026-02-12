# Recursion in python:


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


# Generate first 10 terms
for i in range(10):
    print(recur_fibo(i), end=" ")
