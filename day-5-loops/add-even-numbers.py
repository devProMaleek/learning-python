target = int(input("Enter a number: "))

sum = 0
for even in range(2, target + 1, 2):
    sum += even
print(sum)