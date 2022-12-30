# 튜플(tuple) : 읽기 전용 - immutable(고정) 자료형으로 한 번 데이터가 저장되면 변화되지 않는 자료구조
tp=(124,False,"lee")
print(tp[0])
# tp[1]=True 튜플은 원소의 변경 불가능
lst=list(tp)        # 튜플의 내용을 변경하고 싶으면 리스트로 변환 후 변경한뒤 다시 튜플로 변경
print(lst)
lst[1]=True
tp=tuple(lst)
print(tp)
a=tp[0:2]
print(a)
b=tp[:3]            # 슬라이싱 가능
c=tp[1:]
d=tp[::2]
e=tp[::-1]

dt1 = [10,20,30,40]
dt2 = (10,20,30,40)
dt3 = (50,60,70,80)
dt4 = dt2+dt3       # 튜플 합치기
print(dt4)
lst = dt1 * 3                   # 반복
print(lst)
lst2 = [num*3 for num in dt1]   # 내포 : 원 데이터에 곱하기를하여 할당
print(lst2)
tp1 = dt2 * 3
print(tp1)
tp2 = [num*3 for num in dt2]    # 튜플은 원소 값 변경이 불가능, 내포하게되면 리스트로 바뀜
print(tp2)
tp2 = tuple(tp2)                # 내포 후 다시 튜플로 변경
print(tp2)

first, second, third, fourth = tp2      # 할당
data1, *data2 = tp2
print(tp1)
print(tp2)
print(first, second, third, fourth)
print(data1, *data2)

