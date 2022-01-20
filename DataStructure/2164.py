N = int(input())

card = [number for number in range(1, N+1)]

top = 1

for i in range(len(card)-2):
    card.append(card[top])
    top += 2


print(card.pop())
