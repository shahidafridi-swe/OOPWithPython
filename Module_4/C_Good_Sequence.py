# n = int(input())

# A = list(map(int, input().split()))

# B = list(set(A))
# cnt = 0
# for i in range(len(B)):
#     x = A.count(B[i])
#     if x > B[i]:
#         cnt += x-B[i]
#     elif x < B[i]:
#         cnt += x
# print(cnt)

n = int(input())
A = list(map(int, input().split()))

countD = {}

for num in A:
    if num in countD:
        countD[num] +=1
    else:
        countD[num] = 1

cnt = 0
for num, numCount in countD.items():
    if num < numCount:
        cnt += numCount -num
    elif num > numCount:
        cnt += numCount 
print(cnt)
                 

