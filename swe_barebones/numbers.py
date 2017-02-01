import numpy as np

class Numbers:
    
    def __init__(self):
        pass

    def perfect_number(self,n):
        factors = []
        factors.append(1)
        factors.append(n)
        for i in range(2,n):
            if (n % i == 0):
                factors.append(i)
        # sum factors
        sum = 0
        for f in factors:
        	sum += f
        
        # decide if it's perfect
        return (sum - n == n)
