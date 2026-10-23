correct_pin = "1234"
tries = 0

while tries < 3:
    pin = input("PIN: ")

    if pin == correct_pin:
        print("Access granted")
        break

    tries += 1

if tries == 3:
    print("Card blocked")
