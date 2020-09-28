import time

start = time.perf_counter()

nums: list = "34,48,52,61,76,76,61,84,61,39,83,61,79,81,56,88".split(",")


def get_mode(set_of_numbers: list):
    old_numbers: list = []
    count_: list = []
    for i in set_of_numbers:
        if int(i) not in old_numbers:
            old_numbers.append(int(i))
            count_.append((int(i), set_of_numbers.count(i)))


def get_median(set_of_numbers: list):
    if len(set_of_numbers) % 2:
        return sorted(set_of_numbers)[int((len(set_of_numbers) - 0.5) / 2)]
    else:
        return (int(sorted(set_of_numbers)[int(len(set_of_numbers) / 2)]) +
                int(sorted(set_of_numbers)[int((len(set_of_numbers) / 2)) + 1])) \
                              / 2


print(sorted(nums))

end = time.perf_counter()

print(f'Finished in {round(end - start, 2)} seconds(s)')
