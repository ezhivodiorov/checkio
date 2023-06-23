def not_order(data: list[int]) -> int:
    sdata = sorted(data)
    count = 0
    for i in range(len(sdata)):
        if data[i] != sdata[i]:
            count += 1
    return count


print("Example:")
print(not_order([1, 1, 4, 2, 1, 3]))

assert not_order([1, 1, 4, 2, 1, 3]) == 3
assert not_order([]) == 0
assert not_order([1, 1, 1, 1, 1]) == 0
assert not_order([1, 2, 3, 4, 5]) == 0
assert not_order([6, 5, 4, 3, 2, 1]) == 6

print("The mission is done! Click 'Check Solution' to earn rewards!")