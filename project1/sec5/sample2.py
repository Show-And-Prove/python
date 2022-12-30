# 3개의 단어를 입력받아 첫 글자만 추출하여 약자를 출력하는 프로그램
# 반복문과 입력/출력/슬라이싱문 이용
# 입력예시
# 첫번째 단어 : Korea
# 두번째 단어 : Baseball
# 세번째 단어 : Organization
# 출력 예시
# KBO

firstLetter = str(input("첫 번째 단어 : "))
print("첫 번째 단어 : ", firstLetter)
secondLetter = str(input("두 번째 단어 : "))
print("두 번째 단어 : ", secondLetter)
thirdLetter = str(input("세 번째 단어 : "))
print("세 번째 단어 : ", thirdLetter)

for i in firstLetter:
    i = firstLetter[0]

for j in secondLetter:
    j = secondLetter[0]

for k in thirdLetter:
    k = thirdLetter[0]


print(i+j+k)


