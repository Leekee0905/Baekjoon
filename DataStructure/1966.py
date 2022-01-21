import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque(range(1,N+1))

while len(deq) > 1:
  deq.popleft()
  deq.append(deq.popleft())

print(deq.pop())