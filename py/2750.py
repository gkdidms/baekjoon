n = int(input())
li = []
for _ in range(n):
    m = int(input())
    li.append(m)

li.sort()
for i in range(n):
    print(li[i])