def profile(iterations, runs=1, iter_results=True):
    def body(function):
        def inner(*args):
            results = []
            fact = 0

            for _ in range(runs):
                start = time.time()

                # Function calling
                for _ in range(iterations):
                    fact = function(*args)

                result = time.time() - start
                results.append(result)

                if iter_results:
                    print("[Profiling:{}({}) = {}] x{} iters: {:.6f} ms".format(function.__name__, ', '.join(map(str, args)), fact, iterations, result))

            if runs > 1:
                print("[Profiling Average:{}({}) = {}] x{} iters, x{} runs: {:.6f} ms".format(function.__name__, ', '.join(map(str, args)), fact, iterations, runs, sum(results) / len(results)))

        return inner
    return body
