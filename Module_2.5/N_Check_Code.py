A, B = map(int, input().split())
S = input()
flag =True
for c in range(len(S)):
    if(c==A):
        if S[c] != '-' :
            flag = False
            break
    
        
    elif(S[c]!='0' and S[c]!='1' and S[c]!='2'and S[c]!='3'and S[c]!='4'and S[c]!='5'and S[c]!='6' and S[c]!='7'and S[c]!='8'and S[c]!='9'  ):
        flag = False
        break
    
if len(S) != A+B+1:
    flag = False

if( flag ):
    print("Yes")
else:
    print("No")