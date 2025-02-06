n = 11

def funk1(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 3 != 0:
            count += 1
    return count

print("Количество делителей, не делящихся на 3:", funk1(n))

def funk2(n):
    digits = []
    for d in str(n):
        if int(d) % 2 == 1:
            digits.append(int(d))

    if digits:
        return min(digits)
    else:
        return None

print("Минимальная нечетная цифра:", funk2(n))