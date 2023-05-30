def long_repeat(line: str) -> int:
    result = []
    lenline = len(line)
    while line:
        line = line.lstrip(line[0])
        result.append(lenline - len(line))
        lenline = len(line)
    return max(result, default=0)  # we return the maximum value


print("Example:")
print(long_repeat("sdsffffse"))

assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")