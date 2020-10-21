def solution(p):
    answer = []
    count = 0
    for i in range(N):
        count += int(p[i])
        answer.append(count)
    answer = sum(answer)
    return answer

N = int(input())
p  = list(map(int,input().split()))
p.sort()
print(solution(p))
