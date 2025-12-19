a = int(input("Enter the value of a: "))
if a % 2 == 0:
    limit = a - 1
else:
    limit = a

odd_numbers = []

for i in range(1, limit + 1):
    odd_numbers.append(2 * i - 1)
print(", ".join(map(str, odd_numbers)))
