korean_dic = ["사랑해","귀엽다","고마워","행복해"]

cor=len(korean_dic)
count =0
for korean in korean_dic:
    print(korean)
    word = input("")
    if korean == word:
        count+=1
        

print("전체문제",cor)
print("맞은 문제",count)
print("틀린문제",cor-count)

# 전체 문제 개수 : 4개
