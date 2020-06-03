def solution(h, q):
    p=[]
    q = tuple(q)
    for i in range(len(q)):
        head=2**h-1
        if q[i]==head: p.append(-1)
        else:
            j=h-1
            while j>0: 
                par,l,r = head,head-2**j,head-1
                while True:
                    if q[i]==l or q[i]==r:
                        p.append(par)
                        j=0
                        break
                    elif q[i]<l: head=l
                    else: head=r
                    j-=1
                    par,l,r = head,head-2**j,head-1

    return p

print(solution(5, {19, 14, 28}))
print()
print(solution(3, {7, 3, 5, 1}))