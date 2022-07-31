global int 
i = 71261998

def collatzfind():
    i = 71261998
    while True: # main loop
        number = i
        steps = 0

        while number != 1:

            if number % 2 == 0:
                number /= 2
                steps+=1

            elif number % 2 == 1:
                number = 3 * number + 1
                steps+=1

        if steps >= 1000:
            while True:
                 print('winner winner chicken dinner: ' + str(i) + ' in ' + str(steps) + ' steps.')
            return

        if number == 1:
            print('Ran to 1, ' + str(i) + ' in ' + str(steps) + ' steps.')
            i+=1

collatzfind()