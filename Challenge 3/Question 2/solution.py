def solution(x, y):
    M, F = int(x), int(y)
    count = 0
    while F >= 1:
        if M < F:
            M, F = F, M
        M, F, t = F, M % F, M // F
        count += t
    if M == 1:
        return str(count - 1)
    return "impossible"

print(solution('4', '7'))
print(solution('2', '1'))