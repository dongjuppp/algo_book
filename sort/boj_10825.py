class Student():
    def __init__(self,name,korean,english,math):
        self.name=name
        self.korean=korean
        self.english=english
        self.math=math
    
    def print_me(self):
        print(self.name)


num=int(input())
student_list=[]
for i in range(num):
    name,korean,english,math=map(str,input().split( ))
    
    tmp=Student(name,int(korean),int(english),int(math))
    student_list.append(tmp)

student_list.sort(key=lambda s:(-s.korean,s.english,-s.math,s.name))

for i in range(num):
    student_list[i].print_me()

