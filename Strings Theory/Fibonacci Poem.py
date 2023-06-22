def fib(number):
    a, b = 0, 1
    for x in range(number):
        a, b = b, a + b
    return a
def fibo_poem(text: str) -> str:
    words = text.split(' ')
    newtext = ''
    index = 1
    while True:
        fibo = int(fib(index))
        index += 1
        newtext = ' '.join(words[i] for i in range(fibo))
        newtext += '/n'

        for i in fibo:
            words.pop(0)

        if words.count() == 0:
            break
    return newtext


print("Example:")
print(fibo_poem("Zen of Python"))

# # These "asserts" are used for self-checking
# assert fibo_poem("") == ""
# assert fibo_poem("Django framework") == "Django\nframework"
# assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
# assert (
#     fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.")
#     == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
# )
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")