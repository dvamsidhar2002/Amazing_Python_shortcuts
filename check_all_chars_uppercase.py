import string
def is_upper(word):
    return all(c in string.ascii_uppercase for c in list(word))

print(is_upper('HUMANBEING'))
print(is_upper('humanbeing'))