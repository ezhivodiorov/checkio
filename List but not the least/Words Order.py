# def words_order(text: str, words: list) -> bool:
#     compare_list = []
#     result = True
#     current_index = -1
#     for word in words:
#         if word in compare_list:
#             return False
#         try:
#             new_index = text.index(word, current_index+1)
#         except:
#             return False
#         if new_index < current_index:
#             return False
#         compare_list.append(word)
#         current_index = new_index
#     return result

def words_order(text: str, words: list) -> bool:
    result = {i for i in text.split() if i in words}
    result = sorted(result, key=text.index) == words

    return result

# print("Example:")
# print(words_order("hi world im here", ["world", "here"]))

# These "asserts" are used for self-checking
assert words_order("hi world im here", ["wo", "rld"]) == False
assert words_order("hi world im here", ["world", "world"]) == False
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
assert words_order("hi world im here", ["world", "im", "here"]) == True
assert words_order("hi world im here", ["world", "hi", "here"]) == False
assert words_order("hi world im here", ["country", "world"]) == False
assert words_order("", ["world", "here"]) == False
assert words_order("hi world world im here", ["world", "world"]) == False
assert (
    words_order("hi world world im here hi world world im here", ["world", "here"])
    == True
)

print("The mission is done! Click 'Check Solution' to earn rewards!")