file1 = open("27-170a.txt")
file2 = open("27-170b.txt")

def result(file):
    n, k = map(int, file.readline().split())
    p = [0]
    for i in file:
        p.append(p[-1] + int(i))
    mx = -10 ** 9
    mxi = 0
    mxp = 0
    for i in range(n - k):
        if mxi < i + k + 1:
            mxi = i + k + 1
            mxp = p[mxi]
            for j in range(i + k + 2, n + 1):
                if p[j] > mxp:
                    mxi = j
                    mxp = p[j]
        mx = max(mx, mxp - p[i])
    print(mx)

result(file1)
result(file2)