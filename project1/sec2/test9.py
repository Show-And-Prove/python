# 반복문
i=tot=0
while(i<=100):
    tot+=i
    i+=2    # 증감연산자 되도록 x
print(tot)

j=1
tott=0
while(j<=100):
    tott+=j
    j+=2
print(tott)

print(tot+tott)

# 무한 루프
i=tot=0
while True:
    if(i>=100):
        break
    tot+=i
    i+=2
print(tot)

#
i=tot=0
while True:
    if(i>=100):
        break
    tot+=i
    i+=4
print(tot)