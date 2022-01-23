import sys

input = sys.stdin.readline

N = list(input().rstrip())

flag = False
word = ''
result = ''

for i in N:
  if flag == False:
    if i == '<':
      flag = True
      result += i
      print(result)
      print(i)
    elif i == ' ':
      word += i
      result += word
      word = ''
      print(result)
      print(word)
      print(i)
    else:
      word = i + word
      print(word)
      print(i)

  elif flag == True:
    word += i
    print(i)
    print(word)
    if i == '>':
      flag = False
      result += word
      print(result)
      word = ''

print(result + word)