s = "AbcBA"

def palindrome(s):
    uppercase_letters = []
    for ch in s:
        if ch.isupper():
            uppercase_letters.append(ch)

    reversed_letters = []
    for ch in reversed(uppercase_letters):
        reversed_letters.append(ch)

    if uppercase_letters == reversed_letters:
        return "Это палиндром"
    else:
        return "Это не палиндром"

print(palindrome(s))
