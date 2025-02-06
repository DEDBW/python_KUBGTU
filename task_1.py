n = 11

def funk1(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 3 != 0:
            count += 1
    return count

print("Количество делителей, не делящихся на 3:", funk1(n))