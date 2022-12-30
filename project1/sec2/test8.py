# if와 복수 조건
jum = [20,60,10]   # 파이썬의 열거형
# 모든 점수가 80점 이상이면, 합격
if(jum[0]>=80 and jum[1]>=80 and jum[2]>=80):
    print("합격")
else:
    print("불합격")

# 세 점수 중 하나라도 90점 이상이면 "과목우수", 아니면 공란

if(jum[0]>=90 or jum[1]>=90 or jum[2]>=90):
    print("과목우수")
else:
    print(" ")

# 학점
# 평균 90점 이상 -> A , 그중에서 96점이상이면 A+, 93점 이상이면 A0 92~90 A-

avg = float((jum[0]+jum[1]+jum[2])/3)
if(avg>=90):
    if(avg>=96):
        print("A+")
    elif(avg>=93):
        print("A0")
    else:
        print("A-")
elif(avg>=80):
    if(avg>=86):
        print("B+")
    elif(avg>=83):
        print("B0")
    else:
        print("B-")
elif(avg>=70):
    if(avg>=76):
        print("C+")
    elif(avg>=73):
        print("C0")
    else:
        print("C-")
elif(avg>=60):
    if(avg>=66):
        print("D+")
    elif(avg>=63):
        print("D0")
    else:
        print("D-")
else:
    print("F")

su = 87
hak=['F','F','F','F','F','D','C','B','A','A']
res = hak[su//10]
print("학점 : ", res)

