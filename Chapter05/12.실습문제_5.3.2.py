print("[메뉴를 입력하세요]")
while True:
    x = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료 >>> "))
    if x == 1:
        print("-> 게임을 시작합니다.")
    elif x == 2:
        print("-> 실시간 랭킹 조회")
    elif x == 3:
        print("-> 게임을 종료합니다.")
        break
    else:
        print("-> \다시 입력해 주세요")
        