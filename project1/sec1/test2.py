# 데이터 입력 : input(입력 메시지)
# 캐스팅(casting) : 형 변환
su1 = int(input("숫자1 입력 : "))
su2 = int(input("숫자2 입력 : "))

print("결과 : ", su1 + su2)   # 캐스팅 없는 입력은 문자로 처리

# 정수로 형변환
a="100"
b=6.28
c=True
d=int(a)    # a="100"을 int타입 100으로 변경
e="kim1004" # 숫자 형태로 형변환 불가
print("a를 정수로 형변환 : ", type(a), int(a), type(int(a)))
print("b를 정수로 형변환 : ", type(b), int(b), type(int(b)))
print("c를 정수로 형변환 : ", type(c), int(c), type(int(c)))

# 실수로 형변환
a1="62.34"
a2=90
a3=False
print("-------------------------------------------------------------")
print("a1를 실수로 형변환 : ", type(a1), float(a1), type(float(a1)))
print("a2를 실수로 형변환 : ", type(a2), float(a2), type(float(a2)))
print("a3를 실수로 형변환 : ", type(a3), float(a3), type(float(a3)))

# 논리로 형변환
b1="False"
b2=1004
b3=0
b4=32.4
print("-------------------------------------------------------------")
print("b1를 논리로 형변환 : ", type(b1), bool(b1), type(bool(b1))) # 값이 없거나 0인경우에만 false
print("b2를 논리로 형변환 : ", type(b2), bool(b2), type(bool(b2)))
print("b3를 논리로 형변환 : ", type(b3), bool(b3), type(bool(b3)))
print("b4를 논리로 형변환 : ", type(b4), bool(b4), type(bool(b4)))

# 문자로 형변환
c1=3.14
c2=True
c3=200
print("-------------------------------------------------------------")
print("c1를 문자로 형변환 : ", type(c1), str(c1), type(str(c1)))
print("c2를 문자로 형변환 : ", type(c2), str(c2), type(str(c2)))
print("c3를 문자로 형변환 : ", type(c3), str(c3), type(str(c3)))

d1=15
d2=4
print(d1%d2)
