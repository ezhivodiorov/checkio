def text_formatting(text: str, width: int, style: str) -> str:
    newtext = ''
    words = text.split();
    adstring = ''
    for word in words:
        if len(adstring + '' + word) >= width:
            newtext += adstring + '\n'
            adstring = word
        else:
            adstring = adstring + ' ' + word

    return newtext


LINE = (
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure "
    "harum suscipit aperiam aliquam ad, perferendis ex molestias "
    "reiciendis accusantium quos, tempore sunt quod veniam, eveniet "
    "et necessitatibus mollitia. Quasi, culpa."
)
print("Example:")
print(text_formatting(LINE, 38, "l"))

# These "asserts" are used for self-checking
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        38,
        "l",
    )
    == "Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit. Iure\nharum suscipit aperiam aliquam ad,\nperferendis ex molestias reiciendis\naccusantium quos, tempore sunt quod\nveniam, eveniet et necessitatibus\nmollitia. Quasi, culpa."
)
# assert (
#     text_formatting(
#         "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
#         30,
#         "c",
#     )
#     == " Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa."
# )
# assert (
#     text_formatting(
#         "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
#         50,
#         "r",
#     )
#     == "           Lorem ipsum dolor sit amet, consectetur\n     adipisicing elit. Iure harum suscipit aperiam\n   aliquam ad, perferendis ex molestias reiciendis\n       accusantium quos, tempore sunt quod veniam,\n eveniet et necessitatibus mollitia. Quasi, culpa."
# )
# assert (
#     text_formatting(
#         "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
#         45,
#         "j",
#     )
#     == "Lorem   ipsum  dolor  sit  amet,  consectetur\nadipisicing elit. Iure harum suscipit aperiam\naliquam    ad,   perferendis   ex   molestias\nreiciendis  accusantium  quos,  tempore  sunt\nquod   veniam,   eveniet   et  necessitatibus\nmollitia. Quasi, culpa."
# )
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")