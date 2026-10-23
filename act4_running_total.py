total = 0
count = 0

price = float(input("Price (0 to stop): "))

while price != 0:
    total += price
    count += 1
    price = float(input("Price (0 to stop): "))

print("Items:", count, "Total:", f"{total:.2f}")

if count > 0:
    average = total / count
else:
    average = 0

print("Average:", f"{average:.2f}")