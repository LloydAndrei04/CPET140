amount = int(input("Enter amount in pesos: "))

hundreds = amount // 100
amount = amount % 100

twenties = amount // 20
amount = amount % 20

fives = amount // 5
amount = amount % 5

ones = amount // 1

print("100 pesos:", hundreds)
print("20 pesos:", twenties)
print("5 pesos:", fives)
print("1 peso:", ones)
