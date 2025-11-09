#Print multiplication table
num = int(input("enter the number: "))
table=1
for i in range(1,11):
    table=num*i
    print(num,"X",i,"=",table)