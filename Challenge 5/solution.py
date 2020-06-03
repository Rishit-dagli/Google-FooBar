import math
def summation(n):
    if n == 1:
        return 1 
    if n < 1:
        return 0
    m = math.floor((math.sqrt(2) - 1) * n)
    return (m * n) + (n * (n + 1) / 2) - (m * (m + 1) / 2) - summation(m)
def solution(s):
    s = int(s)
    return str(int(summation(s)))

print(solution('77'))
print(solution('5'))