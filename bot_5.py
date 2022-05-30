import math


def main(y):
    f = 0
    n = len(y)
    for i in range(0, n):
        f += 85 * ((abs(y[n - 1 - (int(i / 3))])) ** 5)
    return f


print(main([0.59, -0.36, -0.98, 0.07, 0.55, -0.07, 0.38]))
# print(main([0.88, 0.92, -0.14, 0.55, -0.2, 0.31, -0.01] ))


