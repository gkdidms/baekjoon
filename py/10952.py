# 끝에 0,0이 들어온다
while True:
    a,b = map(int, input().split())
    if(a <= 0 and b <= 0):
        exit()
    print(a+b)