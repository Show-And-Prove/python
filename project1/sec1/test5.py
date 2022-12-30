import keyword
# 예약어 출력
print(keyword.kwlist)   # kwlist : 예약어, 변수 이름 으로 사용할 수 없다.

# 출력 형식 : %s(문자열), %d(10진정수), %o(8진수), %x(16진수), %c(문자), %f(실수)
# %a (All, 모든 출력 형식)
name = "kim ki tae"
age = 45
height = 173.8
weight = 78.4

print("이름 : %s, 나이 : %d, 키 : %.1f, 몸무게 : %.1f" % (name, age, height, weight))
print("이름 : {}, 나이 : {}, 키 : {}, 몸무게 : {}" .format(name, age, height, weight))

