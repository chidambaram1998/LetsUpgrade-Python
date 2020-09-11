  
start=1042000
end=702648265

for num in range(start,end+1):
    order =len(str(num))

    sum=0

    temp=num
    while temp > 0:
        digit=temp%10
        sum+=digit**order
        temp//=10

    if(num==sum):
        print(num)
        break