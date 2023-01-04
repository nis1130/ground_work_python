# 구구단

x = int(input("몇단을 출력할까요?>>> "))
for i in range(x, x+1):
    for j in range(1, 9+1):
        print(i,"*",j,'=',i * j)