# 비교연산
a=40
b=30
c=70
print("a>b ", a>b)
print("a>=b ", a>=b)
print("a<b ", a<b)
print("a<=b ", a<=b)
print("a==b ", a==b)
print("a!=b ", a!=b)

# 논리 연산자
print("a>b && b>c ", (a>b and b>c))     #키워드로 코드 작성 (and, or, not)
print("a>b || b>c ", (a>b or b>c))
print("!(a>b) ", not(a>b))

# 비트 연산자
print("a & b ", (a & b))
print("a | b ", (a | b))
print("a ^ b ", (a ^ b))
print("bin(a) = ~a : ", ~a)     # 보수
print(a>>1) #10100
# 40 = 1 0 1 0 0 0
# 30 = 0 1 1 1 1 0
