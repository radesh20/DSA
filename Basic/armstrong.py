num=int(input("Enter a number: "))
original=num
temp=num
armstrong=0
count=0
while num>0:
    tem=num%10
    count+=1
    num=num//10
while temp>0:
    digit=temp%10
    armstrong+=digit**count
    temp=temp//10
if armstrong==original:
    print(original," number is an amrstrong number")
else:
    print(original,"is not a armstrong number")