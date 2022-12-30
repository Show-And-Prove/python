# for 반복 : for~in, for~not in, for~in~range

data = [90,80,100,60,70]
a=0
tot=0
for i in data:
    a+=1
    tot+=i
    print(i)

print("평균: ",float(tot/a))
print("합계: ", tot)

jum =[(100,80,70),(90,100,80),(80,90,60),(90,100,100)]
for(kor,eng,mat) in jum:
    tot = kor+eng+mat
    avg = float(tot/3)
    hak = ""
    if(avg>=90):
        hak = "A"
    elif(avg>=80):
        hak = "B"
    print("총점 : ", tot)
    print("평균 : ", avg)


lst = [80,90,70,100,75]
i=0
for pt in lst:
    i+=1
    if(pt>=80):
        print("%d 번째 학생 ㅊㅋ" % i)
    else:
        continue


#
b1 = range(10)
print(b1)
for i in b1:
    print(i)

b2 = range(0,6)
for i in b2:
    print(i)

b3 = range(0,12,2)      # range(start[,end][,step])
for i in b3:
    print(i)

tot = 0
for i in range(1,101):
    tot+=i
print(tot)
#

#i=tot=0
#while(i<=100):
#    tot+=i
#    i+=1
#print(tot)

data1 = [40,60,70,90,95]    #list
data2 = [num *2 for num in data1 if num%2==0]
data3 = [(num-3) for num in data1 if num<=70]
data4 = [num//2 for num in data1 if num>=90]
print(data2)
print(data3)
print(data4)

