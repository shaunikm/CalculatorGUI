nums = input('Enter two numbers seperated by a comma: ').strip().split(',')


def get_factors(n):
    factors = []
    for i in range(1, int(n) + 1):
        if not int(n) % i:
            factors.append(i)
    return factors


def get_GCF(numbers):
    for i1, i2 in zip(get_factors(numbers[0])[::-1], get_factors(numbers[1])[::-1]):
        if i1 in get_factors(numbers[1])[::-1]:
            return i1
        elif i2 in get_factors(numbers[0])[::-1]:
            return i2


print(get_GCF(nums))
