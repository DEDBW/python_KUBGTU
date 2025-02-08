import re

def find_dates(text):
    pattern = r'\b(0?[1-9]|[12]\d|3[01]) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) (\d{4})\b'
    matches = re.findall(pattern, text)
    return [" ".join(match) for match in matches]

text = "Сегодня 31 февраля 2007, а завтра 1 марта 2007. Бывает ли 30 февраля 2025?"
dates = find_dates(text)
print(dates)
