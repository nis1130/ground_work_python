# 1. 리스트 만들기
# - 데이터가 있는 리스트
animals = ["가물치","변명규","이황식","박수아"]


print(animals[2])

# - 데이터 추가하기
animals.append("고라니")
print(animals)

animals[1] = "청개구리"
print(animals)

# - 데이터 삭제하기
del animals[2]
print(animals)

# - 리스트 슬라이싱 (끝 index +1)
print(animals[1:2+1])
print(animals[:]) # 전체
print(animals[:3])
print(animals[1:])

# - 리스트 정렬
animals.sort()
print(animals)

# - 리스트 정렬(역순)
animals.sort(reverse=True)
print(animals)

