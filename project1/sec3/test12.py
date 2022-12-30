# 리스트 : 요소를 선언, 추가, 삽입, 수정, 정렬
# 인덱스가 존재하여 순서 제어가 가능
a=[]        # 빈 리스트
b=["kim", 1004, 6.28, True]      # 각기 다른 데이터 타입을 저장가능
print(type(b), id(b), b)
print(id(b[0]), type(b[0]))     # 변수명[인덱스] : 특정 번째 데이터
print(b[1:3])                   #
print(b[0:])                    # 시작점만 지정
print(b[:4])
print(b[0:4:2])                 #
print(len(b))                   # 리스트의 길이 확인
print(b[-1])                    #
print(b[::-1])                  # 역순 정렬
b.append(18)                    # 요소 추가
print(b)
del b[1]                        # 요소 제거되며 뒤에 요소를 당겨옴
print(b)
b[3]=1004                       # 요소 수정
print(b)
b.insert(2, "Angel")            # 요소 삽입
print(b)

c=["park",100,"A",False]
d=b+c                           # 요소 합치기
print(d)
comment = "aa bb cc dd ee ff ee"
e=comment.split()               # 요소 분리
print(e)
print(e.index('aa'))              # 요소 위치 찾기 .index(찾을내용)
print(e.count('ee'))                   # 특정 요소 갯수확인
print(len(e))
e = [90,40,100,70,60,80,50]
e.sort()
print(e)                  # 요소 오름차순 정렬
e.reverse()               # 내림차순 정렬
print(e)
e.pop()                   # 가장 최근에 입력된 값 지워짐
print(e)
e.pop(1)                  # 특정 인덱스 위치 원소를 끌어내기
print(e)
e.extend([90,80])         #
print(e)
# help(list)                # 관련 도움말