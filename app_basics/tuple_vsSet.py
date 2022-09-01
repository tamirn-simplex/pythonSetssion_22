from timeit import timeit


def time_access(n: int, iterations: int = 10000):
    test_tuple = tuple(range(n))
    test_set = set(range(n))

    result_tuple = timeit(f'{n-1} in test_tuple', globals=locals(), number=iterations)
    result_set = timeit(f'{n-1} in test_set', globals=locals(), number=iterations)

    return result_tuple, result_set


a = time_access(n=100_000)
b = time_access(n=10)

"""
Consider the above code.

In python, set is implemented by an HashTable. Which means that when we read/search, insert or delete, it will always be 
on O(1) average.

Further reading: https://wiki.python.org/moin/TimeComplexity 

When reading, set is definitely faster than tuples (~12,843 times faster on my machine).
But, ask yourselves. What will work best in our case?
What do we require from our data structure?
What are we trying to achieve?
Will we have a large list of command alternatives? ('//quit', '//exit', ....nth)
Will our user submit a very large number of requests in one time?
Do we have a lot of users?
Is it significant?
What is more consistent with our logic? what will work best for us in this case?

"""