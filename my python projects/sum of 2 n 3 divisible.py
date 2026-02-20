n = int (input ("Enter your number here: "))
total = 0
 
for i in range (1, n+1):
  if i % 2 == 0 and i % 3 == 0:
      total += i
      
print ("the sum of divisible by 2 and 3 from 1 to", n, "is", total)