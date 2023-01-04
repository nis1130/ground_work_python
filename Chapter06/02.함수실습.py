# 기본형
# 1. 정의하기
def printHello():
    print("Hello")

# 2. 호출하기
printHello()

# 매개변수가 있는 함수
def sum(a, b):
    print(a+b)
    
import random
def getRandomNumber():
    number = random.randint(1,10)
    return number

print(getRandomNumber())