
def prime_first(number):
    check = True
    if number == 2:
        return print(number)
    elif number == 0 or number == 1:
        check=False
    for k in range(2, number):
        if (number % k) == 0:
            check = False
    if check == True:
        return print(number)
    else:
        return False

def prime_second(number):
    check = True
    for k in range(2, number):
        if (number % k) == 0:
            check = False
    if check == True:
        return False
    else:
        return print(number)


for i in range(1000):
    if i < 500:
        prime_first(i)
    else:
        prime_second(i)



