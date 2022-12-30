# 지방, 탄수화물, 단백질의 그램을 키보드로 입력하면 칼로리를
# 계산하여 출력하는 프로그램
# 총 칼로리 = 지방 * 9 + 단백질 * 4 + 탄수화물 * 4
# 총 칼로리(calorie), 단백질(protein), 지방(fat),
# 탄수화물(carbohydrate) 으로 변수 선언

fat = 0.0;
carbohydrate = 0.0;
protein = 0.0;
calorie = 0.0;

fat = float(input("지방 : "))
print("지방 :", fat)
carbohydrate = float(input("탄수화물 : "))
print("탄수화물 :", carbohydrate)
protein = float(input("단백질 : "))
print("단백질 : ", protein)

calorie = float(fat * 9) + (protein * 4) + (carbohydrate * 4)
print("총 칼로리 : ", calorie)

