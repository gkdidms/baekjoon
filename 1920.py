
n = int(input())
nn = list(input().split())
nn.sort()
m = int(input())
mm = list(input().split())

def search(mm,start,end,nn):
    if start > end:
        return 0
    mid = (start + end) // 2
    if nn[mid] == mm:
        return 1
    elif nn[mid] < mm:
        start = mid + 1
    else :
        end = mid -1

    return search(mm, start, end, nn)


start = 0
end = n - 1
for i in range(m):
    print(search(mm[i],start,end,nn))
    