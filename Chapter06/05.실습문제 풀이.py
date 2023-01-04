import random
list1 = []
def lotto():
    x = random.randint(1,45)
    return x
count = 0
while True:
    if count > 5:
        break
    num=lotto()
    if  num not in list1:
        list1.append(num)
        count += 1
        
list1.sort()

for i in list1:
    print(i , end=" ")
    