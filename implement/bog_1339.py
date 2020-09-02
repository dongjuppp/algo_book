#백준 1339번 단어 수학
import operator

num=int(input())
words=[]


numbers=[0,1,2,3,4,5,6,7,8,9]
alphabets={}

for i in range(num):
    words.append(input())

words=sorted(words,key=lambda x:len(x),reverse=True)



for word in words:
    word_length=len(word)
    for i in range(len(word)):
        if not word[i] in alphabets:
            alphabets[word[i]]=word_length-i


alphabets=sorted(alphabets.items(),key=operator.itemgetter(1),reverse=True)


result={}
start=9
for i in range(len(alphabets)):
    result[alphabets[i][0]]=start-i

re=[]

for word in words:
    answer=''
    for i in range(len(word)):
        answer+=str(result[word[i]])
    re.append(int(answer))


print(sum(re))
