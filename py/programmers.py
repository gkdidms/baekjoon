def solution(s):
    answer = 0

    if len(s) == 1:
        return 1

    for i in range(len(s)-1):
        for j in range(i+1,len(s)+1):
            word = s[i:j]
            if answer > len(word):
                continue
            
            if word[::-1] == word:
                answer = len(word)
                if answer == len(s):
                    return answer

    return answer

s = "ABCCBA"
print(solution(s))