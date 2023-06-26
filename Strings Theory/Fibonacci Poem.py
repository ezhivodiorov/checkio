def fib(number):
    a, b = 0, 1
    for x in range(number):
        a, b = b, a + b
    return a

def fibo_poem(text):

    # Розбиття тексту на окремі слова
    words = text.split()

    fib_text = []  # Результатний багаторядковий текст

    # Формування багаторядкового тексту
    circle = 1
    while True:
        fib_num = fib(circle)
        if len(words) == 0:
            break
        line_words = words[:fib_num]  # Вибір кількості слів, що дорівнює числу Фібоначчі
        line = ' '.join(line_words)  # Формування рядка зі словами, розділеними пробілами
        line += ' _' * (fib_num - len(line_words))  # Доповнення до коректної довжини
        fib_text.append(line)
        words = words[fib_num:]  # Видалення використаних слів
        circle += 1

    return '\n'.join(fib_text)

print("Example:")
print(fibo_poem("Zen of Python"))

# These "asserts" are used for self-checking
assert fibo_poem("") == ""
assert fibo_poem("Django framework") == "Django\nframework"
assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
assert (
    fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.")
    == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
)

print("The mission is done! Click 'Check Solution' to earn rewards!")