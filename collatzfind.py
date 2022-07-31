def collatzfind():
    i = int(input('What number to start with? (default is 1) '))
    maxSteps = int(input('In how many steps without running into 1 do you want the program to stop? '))
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

        if steps >= maxSteps:
            while True:
                print('Number did not run into 1: ' + str(i) + ' in ' + str(steps) + ' steps.')
                break
            return

        if number == 1:
            print('Ran to 1, ' + str(i) + ' in ' + str(steps) + ' steps.')
            i+=1

collatzfind()
