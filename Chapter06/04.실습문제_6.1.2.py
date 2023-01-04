import random

# def getRandomNumber():
#     for i in range(1,6+1):
#         number = random.randint(1,45)
#         list1.append(number)
#     return list1

# print(getRandomNumber())

def getRandomNumber1():
    num = random.randint(1,45)
    return num

list2= []
count=0 # 현재 뽑은 숫자 갯수

while True:
    if count == 6:
        break
    random_num = getRandomNumber1()
    if random_num not in list2:
        list2.append(random_num)
        count += 1
    
list2.sort()
for num in list2:
    print(num, end =" ")

# 함수 , 리스트 , 반복문 , 제어문
# 로또 당첨번호 만들기
