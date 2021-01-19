def profile(iterations, runs=1, iter_results=True):
    '''Profile function
    
    :param iterations: iterations count
    :type iterations: int
    
    :param runs: number of runs
    :type runs: int
    
    :param iter_results: print results for each iteration
    :type iter_results: bool
    '''
    def body(function):
        def inner(*args):
            results = []
            fresult = None

            for _ in range(runs):
                start = time.time()

                # Function calling
                for _ in range(iterations):
                    fresult = function(*args)

                result = time.time() - start
                results.append(result)

                if iter_results:
                    print("[Profiling:{}({}) = {}] x{} iters: {:.6f} ms".format(function.__name__, ', '.join(map(str, args)), fresult, iterations, result))

            if runs > 1:
                print("[Profiling Average:{}({}) = {}] x{} iters, x{} runs: {:.6f} ms".format(function.__name__, ', '.join(map(str, args)), fresult, iterations, runs, sum(results) / len(results)))

        return inner
    return body
