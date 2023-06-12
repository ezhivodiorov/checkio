def follow(instructions: str) -> tuple[int, int] | list[int]:
    tuple=[0, 0]
    for letter in instructions:
        if letter == 'f':
            tuple[1] += 1
        elif letter == 'b':
            tuple[1] -= 1
        elif letter == 'l':
            tuple[0] -= 1
        elif letter == 'r':
            tuple[0] += 1
        else:
            tuple
    return tuple


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")