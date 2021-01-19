# py_profiler
Simple python profiler decorator

Usage examples:
```python
@profile(iterations=10000, runs=10, iter_results=False)
def factorial_math(x):
    return math.factorial(x)


@profile(10000, runs=10, iter_results=False)
def factorial_gamma(x):
    return math.gamma(x + 1)


@profile(10000, 10, False)
def factorial_reduce(x):
    return reduce((lambda x, y: x * y), range(1, x + 1))


@profile(10000, 10, False)
def factorial_cache(x, _factcache={}):
    if x not in _factcache:
        _factcache[x] = math.factorial(x)
    return _factcache[x]


_FAC_TABLE = [1, 1]


@profile(10000, 10, False)
def factorial_table(n):
    if n < len(_FAC_TABLE):
        return _FAC_TABLE[n]

    last = len(_FAC_TABLE) - 1
    total = _FAC_TABLE[last]
    for i in range(last + 1, n + 1):
        total *= i
        _FAC_TABLE.append(total)

    return total


factorial_math(13)
factorial_gamma(13)
factorial_reduce(13)
factorial_cache(13)
factorial_table(13)
```
