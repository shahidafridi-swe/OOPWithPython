# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/M

lst = list(map(int, input().split()))
result = []
for i in range(lst[0],lst[1]+1):
    s = str(i)
    flag = 0
    for c in s:
        if(c!='4' and c!='7'):
            flag = 1
            break
            
    if(flag==0):
        result.append(i)

        
if(len(result) == 0):
    print(-1)
else:
    for x in result:
        print(x, end=' ')
