import re

with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read()

sentences = re.split(r'[.!?]+', content)
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

common_words = None

for sentence in sentences:
    words = set(re.findall(r'\w+', sentence.lower()))
    if common_words is None:
        common_words = words
    else:
        common_words &= words

if common_words:
    print("Слово(а), встречающееся(ие) в каждом предложении:", common_words)
else:
    print("Такого слова нет.")