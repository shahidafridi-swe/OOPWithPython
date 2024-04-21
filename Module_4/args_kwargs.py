# def sumOfNum(*num):
#     sum = 0
#     for n in num:
#         sum += n
    
#     return sum

# result = sumOfNum(1,2,3,4,5)
# print(result)

def studentInfo(**info):
    
    for key, value in info.items():
        print(key, ":", value)
        # print("{} is {}".format(key,value))

studentInfo(Name="Shahid Afridi", Roll = 378 ,Phone='01704805886' , Email='shahidafrdi.cse@gmail.com')
