def count_frequency(a): 
    freq = dict() 
    for items in a: 
        freq[items] = a.count(items) 
    return freq
    
def solution(data, n): 
    frequency = count_frequency(data)
    for key, value in frequency.items():
        if value > n:
            data = list(filter(lambda a: a != key, data))
    return data

print(solution([1, 2, 3], 0))
print(solution([5, 10, 15, 10, 7], 1))
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
