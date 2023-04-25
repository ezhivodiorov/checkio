# Taken from mission Goes Right After (simplified)

def goes_after(word: str, first: str, second: str) -> bool:
    result  = word.index(first) == word.index(second)-1 if first in word and second in word else False
    # result = len(word) != 0\
    #          and first != second\
    #          and word.find(first+second) != -1\
    #          and word.index(first) < word.index(second)\
    #          and word.index(first) != len(word)-1\
    #          and word[word.index(first) + 1] == second
    return result


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "w") == False
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False
assert goes_after('transport', 'r', 't') == False
assert goes_after('almaz', 'm', 'a') == False

print("The mission is done! Click 'Check Solution' to earn rewards!")