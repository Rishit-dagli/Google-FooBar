import math
def generate_dist_vector(size, start, tot_length, length):
    tmp = [start]
    count = 0
    l, r = -length, tot_length - length
    for i in range(size):
        left, right = tmp[0], tmp[count]
        left += (l*2)
        right += (r*2)
        l, r = -r,-l
        tmp = [left] + tmp + [right]
        count += 2
    return tmp

def make_mat(vec1, vec2):
    mat, count = [], 0
    for i in vec2:
        mat.append([])
        for j in vec1:
            mat[count].append((j,i))
        count += 1
    return mat

def translate(x, y, vec):
    mat, count = [], 0
    for i in vec:
        mat.append([])
        for j in i:
            mat[count].append((j[0] + x, j[1] + y))
        count += 1
    return mat

def serialize(vec):
    start = int(len(vec)/ 2) 
    elms = [vec[start][start]]
    count = 3
    start -= 1
    while( start >= 0):
        x, y = start, start

        for j in range(1, count):
            x += 1
            elms += [vec[y][x]]
        for j in range(1, count):
            y += 1
            elms += [vec[y][x]]
        for j in range(1, count):
            x -= 1
            elms += [vec[y][x]]
        for j in range(1, count):
            y -= 1
            elms += [vec[y][x]]
        
        start -= 1
        count += 2
    return elms

def key(x,y):
    return format(math.atan2(x,y))
    # return format(math.atan2(x,y),'.32f')
    
def dist(x,y):
    return math.hypot(x,y)

def calc(you, guard, distance):
    visited, count, l = {}, 0, len(you)
    for i in range(l):
        ce, be = you[i], guard[i]
        visited[key(ce[0], ce[1])] = True
        if distance - dist(be[0], be[1]) >=0 :
            k = key(be[0], be[1])
            if k not in visited:
                count += 1
                visited[k] = True
        else:
            k = key(be[0], be[1])
            visited[k] = True
    return count

def solution(dimensions, your_position, guard_position, distance):
    tx, ty = your_position
    width, height = dimensions

    mat_size = int(math.ceil(max( distance/width, distance / height))) + 1
    guard_x =  generate_dist_vector(mat_size, guard_position[0], width, guard_position[0])
    guard_y =  generate_dist_vector(mat_size, guard_position[1], height, guard_position[1])
    you_x =  generate_dist_vector(mat_size, your_position[0], width, your_position[0])
    you_y =  generate_dist_vector(mat_size, your_position[1], height, your_position[1])
    
    elms_guard =  serialize(translate(-tx, -ty, make_mat(guard_x, guard_y)))
    elms_you =  serialize(translate(-tx, -ty, make_mat(you_x, you_y)))
    
    return calc(elms_you, elms_guard, distance)

print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))