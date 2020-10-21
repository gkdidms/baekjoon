def solution(pay):
    m500, m100, m50, m10, m5,m1 =0,0,0,0,0,0
    while(pay >= 500):
        pay = pay- 500
        m500 += 1
    while(pay >= 100):
        pay = pay-100
        m100 += 1
    while(pay >= 50):
        pay = pay-50
        m50 += 1
    while(pay>=10):
        pay = pay - 10
        m10 += 1
    while(pay>= 5):
        pay = pay -5
        m5 += 1
    while(pay>=1):
        pay = pay -1
        m1 += 1

    return (m500 + m100 + m50+ m10+ m5+ m1)

pay = int(input())
m = 1000-pay
print(solution(m))
