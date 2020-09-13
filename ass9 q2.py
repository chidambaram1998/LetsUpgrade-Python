
def ArmStrong(n):
  for i in n:
    l = len(str(i))
    sum = 0
    temp = i
  
    while temp > 0:
        d = temp % 10
        sum += d ** l
        temp //= 10

    if i == sum:
        yield i

lst = list(range(1,1000))
print(list(ArmStrong(lst)))