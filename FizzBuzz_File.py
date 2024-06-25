def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1)
    
    # Conditions for FizzBuzz
    condlist = [
        (numbers % 15 == 0),
        (numbers % 3 == 0),
        (numbers % 5 == 0)
    ]
    
    choicelist = ['FizzBuzz', 'Fizz', 'Buzz']
    
    output = np.select(condlist, choicelist, default=numbers.astype(str))
    
    # Convert numpy array to Python list
    return output.tolist()

# Test
start = 1
finish = 15
result = FizzBuzz(start, finish)
print(result)