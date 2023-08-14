input_num=int(input("Provide a integer number: "))

numbers=[]
for i in range (1,input_num+1):
    numbers.append(i)

print(numbers)

for number in numbers:
    if number%5==0 and number%3==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)

