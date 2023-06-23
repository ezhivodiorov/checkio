def fibo_poem(text):

    fib_sequence = [0, 1]  # Початкова послідовність Фібоначчі
    fib_text = []  # Результатний багаторядковий текст

    # Розбиття тексту на окремі слова
    words = text.split()

    # Генерація послідовності Фібоначчі до перевищення максимальної кількості слів
    while fib_sequence[-1] < len(words):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    # Формування багаторядкового тексту
    for fib_num in fib_sequence:
        line_words = words[:fib_num]  # Вибір кількості слів, що дорівнює числу Фібоначчі
        line = ' '.join(line_words)  # Формування рядка зі словами, розділеними пробілами
        line += ' _' * (fib_num - len(line_words))  # Доповнення до коректної довжини
        fib_text.append(line)
        words = words[fib_num:]  # Видалення використаних слів

    return '\n'.join(fib_text)

print(fibo_poem("Django framework"))