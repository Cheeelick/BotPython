def zero(items, left, middle, right):
    if items[0] == 1988:
        return left
    if items[0] == 1979:
        return middle
    if items[0] == 1998:
        return right


def one(items, left, right):
    if items[1] == 'MASK':
        return left
    if items[1] == 'XBASE':
        return right


def two(items, left, middle, right):
    if items[2] == 1990:
        return left
    if items[2] == 1957:
        return middle
    if items[2] == 2009:
        return right


def three(items, left, middle, right):
    if items[3] == 'FISH':
        return left
    if items[3] == 'TXL':
        return middle
    if items[3] == 'HACK':
        return right


def four(items, left, right):
    if items[4] == 2013:
        return left
    if items[4] == 1957:
        return right


def main(items):
    return three(
        items,
        zero(items, one(items, two(items, 0, 1, 2), four(items, 3, 4)),
             two(items, four(items, 5, 6), 7, 8), 9),
        10,
        11
    )
