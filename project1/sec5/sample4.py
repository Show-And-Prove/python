# 컴퓨터에서 1~10의 임의의 수를 발생시키고,
# 사용자가 입력한 수가 일치하면, 미션성공으로 출력
# 만약 일치하지 않으면 불일치로 출력하며, 일치할 때 까지
# 입력상태 지속

import random

#num1 = int(input("숫자 입력 : "))

#a = random.randint(1,10)

while(num1):
    num1 = int(input("숫자 입력 : "))
    a = random.randint(1, 10)
    if(num1 == a):
        print("미션성공")
        print(a)
        break
    else:
        print("불일치")








