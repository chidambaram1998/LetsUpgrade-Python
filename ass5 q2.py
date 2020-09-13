def prime(x):
  for n in range (2, x):
      if(x % n == 0):
          return False
      else:
          return True

lst = list(range(2500))
lst_prime = []

for item in lst:
  if prime(item):
    lst_prime.append(item)

filter_prime = filter(prime, lst)
print(list(filter_prime))