from os import popen
import sys

input = sys.stdin.readline
N = list(map(str, input().rstrip())) #괄호 입력

a = [] # 공백 리스트 선언
cnt = 0 #막대 갯수

for i in range (len(N)): # 괄호 길이만큼 반복
  if N[i] == '(': # ( 괄호이면
    a.append(i) # a에 i추가
  
  if N[i] == ')': # ) 이면
    if a[-1] == i -1: # 바로 전이 ( 이면 레이저
      a.pop() # 맨 왼쪽 괄호 제거
      cnt += len(a) # 남은 ( 만큼 막대의 길이
    else: #아닐 경우 괄호 끝내고 마지막 한 조각
      a.pop()
      cnt += 1

print(cnt)
