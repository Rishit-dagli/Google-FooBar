def ranged_xor(m, n):
    f_m = [m, 1, m + 1, 0][m % 4]
    f_n = [n, 1, n + 1, 0][n % 4]
    return f_m ^ f_n

def solution(start, length):
    xor = 0
    for i in range(length):
        xor ^= ranged_xor(start - 1, start + length - i - 1)
        start += length
    return xor

print(solution(0,3))
print(solution(17,4))