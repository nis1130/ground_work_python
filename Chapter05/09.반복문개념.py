# 반복문
# : 반복해서 명령을 사용하고 싶을 때

# 시퀀스 자료형
# : 순서가 있는 자료형
# 1. 리스트
# 2. 문자열
champions = ["티모","이즈리얼","리신"]

for champion in champions:
    print("선택한 챔피언은", champion , "입니다")
    
# 문자열 사용
fightin_message = "자신감을 가지자!"

for word in fightin_message:
    print(word)
    
# range(시작, 끝)
for i in range(1,10):
    print(i)
    
    
result=[]
sum = 0
for i in range(10):
    x=(input(i))
    result.append(x)
    sum += int(result[i])

print(result)
avg = sum /10 
print(avg)
