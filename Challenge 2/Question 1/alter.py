def locate(top,num,under):
    under=under//2
    right=top-1
    left=top-1-under
    if right==num or left==num:
        return top
    else:
        if num<=left:
            return locate(left, num, under)
        else:
            return locate(right,num,under)

def solution(h,q):
    head=(2**h)-1
    result=[]
    q = tuple(q)
    for i in range(len(q)):
        if q[i]<head and q[i]>=1:
            x = locate(head,q[i],head-1)
            result.append(x)
        else:
            result.append(-1)
            return result
print(solution(5, {19, 14, 28}))
print()
print(solution(3, {7, 3, 5, 1}))