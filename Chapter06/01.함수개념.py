# 함수를 사용하는 이유
# --> 재사용성

# 함수를 사용하지 않은 경우
print("안녕하세요. 동준님")
print("안녕하세요. 동준님")
print("안녕하세요. 동준님")
print("현재 프리미엄 서비스 사용기간이 5일 남았습니다.")

# 함수를 사용한 경우
def printMessage(name, data):
    print("안녕하세요. ", name,"님")
    print("현재 프리미엄 서비스 사용기간이 ",data, "일 남았습니다.")
printMessage("동준",30)