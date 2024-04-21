S = input()
cntL = 0
cntR = 0
substrings = []
tmp = ''
for c in S:
    if c == 'L':
        cntL +=1
        tmp += 'L'
    else:
        cntR +=1
        tmp += 'R'
    if cntL == cntR:
        substrings.append(tmp)
        tmp = ''

print(len(substrings))
for i in substrings:
    print(i)