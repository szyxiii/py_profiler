# py_profiler
Simple python profiler decorator

## Usage examples:
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

## Output example:
```
[Profiling Average:factorial_math(13) = 6227020800] x10000 iters, x10 runs: 0.006301 ms
[Profiling Average:factorial_gamma(13) = 6227020800.0] x10000 iters, x10 runs: 0.004852 ms
[Profiling Average:factorial_reduce(13) = 6227020800] x10000 iters, x10 runs: 0.032857 ms
[Profiling Average:factorial_cache(13) = 6227020800] x10000 iters, x10 runs: 0.002400 ms
[Profiling Average:factorial_table(13) = 6227020800] x10000 iters, x10 runs: 0.003700 ms
```
