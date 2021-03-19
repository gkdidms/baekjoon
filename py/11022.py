num = int(input())
x = 0
for i in range(num):
    x += 1 
    a,b = map(int, input().split())
    c = a+b
    print(f"Case #{x}: {a} + {b} = {c}")