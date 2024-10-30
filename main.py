def fizzbuzz(number):
    for i in range(number):
        if i%3 == 0:
            print("Fizz")
        if i%5 == 0:
            print("Buzz")
        if i%3 and i%5 == 0:
            print("Fizz Buzz")
        else:
            print(i)

fizzbuzz(100)