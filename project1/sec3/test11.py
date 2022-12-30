# 자료 구조 : 기본형(int, float, bool, str), 열거형(list, set, tuple, dict)
lst = [60,70,50,90,70,80]   # list []
tp = (60,70,50,90,70,80)    # tuple ()  읽기전용(추가 수정 불가)
st = {60,70,50,90,70,80}    # set {}    중복되는값은 하나만 출력, 순서x 인덱스 불가
dct = {'kor':60,'eng':70,'mat':50,'sci':90,'his':70,'art':80}   # dict {'key':x,'key':y,.....}

print(type(lst), lst)
print(type(tp), tp)
print(type(st), st)
print(type(dct), dct)

