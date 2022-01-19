import sys

N,M = map(int, input().split())

findList  = list(map(int, input().split()))
queue = [i for i in range(1,N+1)]
count = 0

for i in range(M):
    length = len(queue)
    idx = queue.index(findList[i])

    if length - idx > idx:
        while True:
            if queue[0] == findList[i]:
                del queue[0]
                break
            else:
                queue.append(queue[0])
                del queue[0]
                count += 1
    
    else:
        while True:
            if queue[0] == findList[i]:
                del queue[0]
                break
            else :
                queue.insert(0,queue[-1])
                del queue[-1]
                count += 1

print(count)