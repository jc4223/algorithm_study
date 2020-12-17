import random
import time

"""
decorator는 함수를 래핑 해주는 역활
random_tree = benchmark(random_tree)
"""

def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print("{0} {1}".format(func.__name__, time.perf_counter() - t))
        return res
    return wrapper


@benchmark
def random_tree(n):
    temp = [n for n in range(n)]
    for i in range(n + 1):
        temp[random.choice(temp)] = random.choice(temp)
    return temp

if __name__ == "__main__":
    res = random_tree(10000)
    print(res)
