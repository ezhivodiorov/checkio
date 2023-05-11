def cut_sentence(line: str, length: int) -> str:
    new_line = ''
    stock = length
    for word in line.split(" "):
        newword = word[:min(len(word), stock)]
        if len(new_line + newword) > length:
            return new_line.rstrip() + '...'
        else:
            stock -= len(newword)
            new_line += newword + ' '
    return new_line.rstrip()


print("Example:")
print(cut_sentence("Hi my name is Alex", 1))
print(cut_sentence("Hi my name is Alex", 8))
print(cut_sentence("Hi my name is Alex", 4))
print(cut_sentence("Hi my name is Alex", 18))
# print(cut_sentence("Hi my name is Alex", 1))
#
# # These "asserts" are used for self-checking
# assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
# assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
# assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
# assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"
# assert cut_sentence("Hi my name is Alex", 1) == "..."
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")