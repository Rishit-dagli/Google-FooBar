def bfs(matrix, source, destination):
    visited = [-1 for i in range(len(matrix))]
    visited[source], queue = source, [source]
    while len(queue) > 0:
        top_element = queue.pop()
        for i in range(len(matrix)):
            if (matrix[top_element][i][1] - matrix[top_element][i][0]) != 0 and visited[i] == -1:
                if i == destination:
                    visited[destination] = top_element
                    path = [destination]
                    temp = destination
                    while temp != source:
                        temp = visited[temp]
                        path.append(temp)
                    path.reverse()
                    temp, total, current = 1, float('inf'), source
                    while temp != len(path):
                        entry = matrix[current][path[temp]]
                        diff = abs(entry[1]) - entry[0]
                        total = min(total, diff)
                        current = path[temp]
                        temp += 1
                    temp, current = 1, source
                    while temp != len(path):
                        entry = matrix[current][path[temp]]
                        if entry[1] < 0:
                            entry[1] += total
                        else:
                            entry[0] += total
                        entry = matrix[path[temp]][current]
                        if entry[1] <= 0:
                            entry[1] -= total
                        else:
                            entry[0] += total
                        current = path[temp]
                        temp += 1
                    return True
                else:
                    visited[i] = top_element
                    queue.append(i)
    return False

def solution(entrances, exits, path):
    max_val = sum(list(map(sum, path)))
    aug = []
    for i in range(len(path)):
        aug.append([])
        for j in range(len(path[i])):
            aug[i].append([0, path[i][j]])
        aug[i].append([0, 0])
        if i in exits:
            aug[i].append([0, max_val])
        else:
            aug[i].append([0, 0])
    aug.extend([[], []])
    for i in range(len(path[0]) + 2):
        if i in entrances:
            aug[-2].append([0, max_val])
        else:
            aug[-2].append([0, 0])
        aug[-1].append([0, 0])
    while bfs(aug, len(aug)-2, len(aug)-1):
        pass
    total = 0
    for i in range(len(aug)):
        total += aug[-2][i][0]
    return total

print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))