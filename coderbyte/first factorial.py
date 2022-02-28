def FirstFactorial(num):

    # code goes here
    for i in range(1, num):
        num *= i
    return num


# keep this function call here
print(FirstFactorial(input()))
