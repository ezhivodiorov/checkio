def index_power(ar: list[int], n: int) -> int:
    return pow(ar[n], n) if len(ar) > (n) else -1


print("Example:")
print(index_power([1, 2, 3], 2))

# These "asserts" are used for self-checking
assert index_power([1, 2, 3, 4], 2) == 9
assert index_power([1, 3, 10, 100], 3) == 1000000
assert index_power([0, 1], 0) == 1
assert index_power([1, 2], 3) == -1
assert index_power([96, 92, 94], 3) == -1

print("The mission is done! Click 'Check Solution' to earn rewards!")