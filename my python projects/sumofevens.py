n = int(input("Wite your number here: "))
total = 0
 
for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print("The sum of even numbers from 1 to", n, "is", total)