def solution(m, musicinfos):
    answer = ''
    li=[]
    play=[]
    for i in range(len(musicinfos)):
        li.append(musicinfos[i].split(","))
        if li[i][0][:2] == li[i][1][:2]:
            n = int(li[i][1][3:5])-int(li[i][0][3:5])
            play.append(n)
        else:
            n = (60+int(li[i][1][3:5])) - int(li[i][0][3:5])
            play.append(n)

    result = []
    for i in range(len(play)):
        if len(li[i][3]) < play[i]:
            while(len(li[i][3])//play[i] < 1):
                n = li[i][3] + li[i][3]
                li[i][3] = n

            if m in li[i][3]:
                index = li[i][3].find(m)+ len(m)
                if len(li[i][3]) > index:
                    if li[i][3][index] != '#':
                        result.append([play[i],li[i][2]])
                    else:
                        x = li[i][3][index+1:]
                        if m in x:
                            index = x.find(m)+ len(m)
                            if len(x) > index:
                                if x[index] != '#':
                                    result.append([play[i],li[i][2]])
                else:
                    if li[i][3][index] != '#':
                        result.append([play[i],li[i][2]])

                    
        else:
            if m in li[i][3]:
                index = li[i][3].find(m) + len(m)
                if len(li[i][3]) > index:
                    if li[i][3][index] != '#':
                        result.append([play[i],li[i][2]])
                else:
                    result.append([play[i],li[i][2]])
    
    if len(result) >1 :
        sorted(result,key=lambda x: x[0])
        answer = result[0][1]
    elif len(result) == 1:
        answer = result[0][1]
    else:
        return "(None)"


    return answer


m = "CCB"
musicinfos = ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"] 
print(solution(m,musicinfos))