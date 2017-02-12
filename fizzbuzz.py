i = 0
izbrano_stevilo = int(raw_input("Vpisite stevilo med 1 in 100: "))
while i < izbrano_stevilo:
    i = i + 1
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)







