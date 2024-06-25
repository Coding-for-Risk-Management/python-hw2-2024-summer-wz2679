def FizzBuzz(start, finish):
    outlist = []
    for num in range(start, finish + 1):
        if num % 3 == 0 and num % 5 == 0:
            outlist.append("FizzBuzz")
        elif num % 3 == 0:
            outlist.append("Fizz")
        elif num % 5 == 0:
            outlist.append("Buzz")
        else:
            outlist.append(str(num))  # Convert number to string and append
    
    return outlist


