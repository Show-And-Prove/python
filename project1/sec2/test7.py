su1 = int(input("점수 입력 : "))
print("점수 : ", su1)
# 제어문 : 조건문(if), 반복문(while, for), 기타 제어문(break, continue)
# 프로그램 블록 : if, while, for, function,...에서 {} 사용하지 않음. 탭으로 들여쓰기하여 해당 블록을 구분.
# if(조건식) :
#           해당 조건이 참일 때 실행할 문장
# else :
#       해당 조건이 거짓일 때 실행할 문장

if(su1>=80) :
    print("합격")
else :
    print("불합격")

# if(조건식) :
#   실행문1
# elif(==elseif, 조건식2) :
#   실행문2
# else :
#   실행문n

if(su1>=90) :
    print("A")
elif(su1>=80) :
    print("B")
elif(su1>=70) :
    print("C")
elif(su1>=60) :
    print("D")
else :
    print("F")