
myMatrix2 = []
number = 0
result = False
for row in range(3):
    myList = []
    for col in range(3):
        check = 0
        while(result != True):
            number = number+1
            for k in range(2, number):
                if number % k == 0:
                    check = check+1
            if check == 0:
                result = True
            check = 0
        result = False
        myList.append(number)
    myMatrix2.append(myList)
for m in myMatrix2:
    print(m)