def adjacent_letters(line: str) -> str:

    count = len(line) - 1
    i = 0
    while True:
        if count == -1:
            break
        elif count == i:
            break
        elif line[i] == line[i+1]:
            line = line[:i] + line[i+2:]
            count = len(line) - 1
            i =0
        else:
            i += 1

    return line


print("Example:")
print(adjacent_letters("adjacent_letters"))

# These "asserts" are used for self-checking
assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
assert adjacent_letters("") == ""
assert adjacent_letters("aaa") == "a"
assert adjacent_letters("ABBA") == ""
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")