def checkio(food: int) -> int:
    fed = 0
    new = 1
    while True:
        fed += new
        new += 1
        food -= fed
        if food < fed+new:
            break
    # while food > fed+new:
    #     fed += new
    #     new += 1
    #     food -= fed
    return max(food, fed)


print("Example:")
print(checkio(1))

# These "asserts" are used for self-checking
assert checkio(1) == 1
assert checkio(3) == 2
assert checkio(5) == 3
assert checkio(10) == 6

print("The mission is done! Click 'Check Solution' to earn rewards!")