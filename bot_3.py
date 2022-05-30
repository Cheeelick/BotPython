import math


def main(b, m, y):
    f = 0
    for c in range(1, b + 1):
        f += (62 * ((math.ceil(c)) ** 5))
    for c in range(1, b + 1):
        for i in range(1, m + 1):
            f -= ((((c ** 3) + (81 * (y ** 2))) ** 2) +
                  (((76 * i) - (c ** 3)) ** 7))
    return f


print(main(6, 8, 0.03))
print(main(6, 2, 0.15))
