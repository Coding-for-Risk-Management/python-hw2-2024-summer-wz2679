
import numpy as np

def FizzBuzz(start, finish):
  
    numvec = np.arange(start, finish+1, dtype=object)
       
    objvec = np.array(numvec, dtype=object)
    
    fizz_mask = (numvec % 3 == 0)
    buzz_mask = (numvec % 5 == 0)
    fizzbuzz_mask = fizz_mask & buzz_mask
    
    objvec[fizzbuzz_mask] = "fizzbuzz"
    objvec[fizz_mask & ~fizzbuzz_mask] = "fizz"
    objvec[buzz_mask & ~fizzbuzz_mask] = "buzz"
    
    myEmptyList = []
    for elem in objvec:
        myEmptyList.append(elem)
    
    return myEmptyList


