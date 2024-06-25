import numpy as np

def FizzBuzz(start, finish):
    # Create the number array
    numvec = np.arange(start, finish+1, dtype=object)
    
    # Initialize the array for results
    objvec = np.array(numvec, dtype=object)
    
    # Vectorized FizzBuzz
    fizz_mask = (numvec % 3 == 0)
    buzz_mask = (numvec % 5 == 0)
    fizzbuzz_mask = fizz_mask & buzz_mask
    
    objvec[fizzbuzz_mask] = "FizzBuzz"
    objvec[fizz_mask & ~fizzbuzz_mask] = "Fizz"
    objvec[buzz_mask & ~fizzbuzz_mask] = "Buzz"
    
    # Convert the result to a list by appending elements
    myEmptyList = []
    for elem in objvec:
        myEmptyList.append(elem)
    
    return myEmptyList


# Test
start = 1
finish = 15
result = FizzBuzz(start, finish)
print(result)
