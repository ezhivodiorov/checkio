def between_markers(text: str, begin: str, end: str) -> str:
    start = 0 if begin == '' or text.find(begin) == -1 else text.find(begin) + len(begin)
    finish = len(text) if end == '' or text.find(end) == -1 else text.find(end)
    if start > finish:
        return ''
    return text[start:finish]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)

assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")