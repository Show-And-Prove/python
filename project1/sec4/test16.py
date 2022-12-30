# 함수(function) 그리고 클래스(class)
def plus1():            # 매개변수 X, 리턴 X
    print("더하기")

def plus2(a, b):        # 매개변수 O, 리턴 X
    print(a+b)

def plus3():            # 매개변수 X, 리턴 O
    a = int(input("숫자1 : "))
    b = int(input("숫자2 : "))
    return a+b

def plus4(a, b):        # 매개변수 O, 리턴 O
    return a+b

plus1()     # 매개변수 X, 리턴 X
a = int(input("숫자1 : "))
b = int(input("숫자2 : "))
plus2(a, b) # 매개변수 O, 리턴 X
hap1 = plus3()   # 매개변수 X, 리턴 O
print(hap1)
hap2 = plus4(a, b)  # 매개변수 O, 리턴 O
print(hap2)
