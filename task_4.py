sentence = "Солнце светит ярко в голубом небе"

def sort_words(sentence):
    words = sentence.split()

    sorted_words = sorted(words, key=len)

    return " ".join(sorted_words)

print(sort_words(sentence))
