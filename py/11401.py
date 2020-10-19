#분할 정복을 이용
def bine(a,b):
    if b == 0:
        return 1
    if b % 2:
        return (bine(a,b//2)**2 * a)%p
    else:
        return (bine(a,b//2) ** 2)%p

n,k = map(int,input().split())
p = 1000000007

# 펙토리얼을 구하기 위해 dp사용
fact = [1 for _ in range(n + 1)]
for i in range(2,n+1):
    fact[i] = fact[i - 1] *i %p

A = fact[n]
B = (fact[n-k] * fact[k])%p

print((A % p) * (bine(B,p-2)%p)%p)