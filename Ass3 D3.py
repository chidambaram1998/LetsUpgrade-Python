#Question 1:
a=int(input("Enter the feet of the Flight:"))
if a <= 1000 :
  print("Safe to Land")
elif a <= 5000 :
  print("Bringdown to 1000")   
else :
  print("Turn Around")


#Question 2:
a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:1"))
for num in range(a, b+ 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
