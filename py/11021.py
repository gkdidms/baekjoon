num = int(input())
x = 0
for i in range(num):
    x += 1
    a,b = map(int, input().split())
    print("Case #{}:".format(x), a +b)