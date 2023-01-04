# while
# : 보통 반복 회수가 정해지지 않았을 때 사용한다.

i = 0 # 초기식
while i < 10: # 조건식
    print(i, "번쨰 다짐, 나는 할 수 있다.")
    i += 1 # 증감식

# 무한루트
# : 조건식에 true

while True:
    x = input("종료하려면 exit를 입력하세요>>>")
    if x == "exit":
        break