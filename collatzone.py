def collatz(number):
    steps = 0

    if number % 2 == 0:
        print(number // 2)
        number /= 2
        steps += 1
        return

    elif number % 2 == 1:
        result = 3 * number + 1
        steps += 1
        return result

steps = 0

i = int(input("Enter a number: "))
while i != 1:
    i = collatz(int(i))
while i == 1:
    print('Ran into 1 in ' + str(steps) + ' steps')
    break 
