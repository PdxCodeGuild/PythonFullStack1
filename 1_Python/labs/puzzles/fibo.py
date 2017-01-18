"""
Write a function that outputs a list of fibbonacci numbers up to the ceiling value.

>>> fibo(10)
[0, 1, 1, 2, 3, 5, 8]

>>> fibo(20)
[0, 1, 1, 2, 3, 5, 8, 13]

>>> fibo(30)
[0, 1, 1, 2, 3, 5, 8, 13, 21]


Write a Generator function named 'fib_infinite()' to calculate fibbonacci numbers to infinity.
>>> fibo_iterator = fib_infinite()
>>> next(fibo_iterator)
0
>>> next(fibo_iterator)
1
>>> next(fibo_iterator)
1
>>> next(fibo_iterator)
2
>>> next(fibo_iterator)
3
>>> next(fibo_iterator)
5
>>> next(fibo_iterator)
8
>>> next(fibo_iterator)
13
"""
