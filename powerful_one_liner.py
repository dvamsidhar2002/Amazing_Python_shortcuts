salary = 4000

if salary > 9000:
    tax = 900
elif 3000<salary<9000:
    tax = 100
else:
    tax = 0
print(f"Tax to pay : ${tax}")

tax = 900 if salary > 9000 else 100 if 3000 < salary < 5000 else 0
print(f"Tax to pay : ${tax}")
