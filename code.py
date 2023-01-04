class Solution:
    def divide(self, dividend, divisor):

        # this is necessary; otherwise phase 1 never terminates
        if dividend == 0: return 0

        # initialize
        i, result, p, q = map(abs, (0, 0, dividend, divisor))
        
        # phase 1
        while q << i <= p: i += 1 # Phase 1: Figure out how far left you should go

        # phase 2
        for j in reversed(range(i)): # Phase 2: Divide like we were kids 
            if q << j <= p: p, result = p - (q << j), result + (1 << j)

        # restrictions to 32 bit
        if (dividend > 0) != (divisor > 0) or result < -1 << 31: result = -result #32 bit
        return min(result, (1 << 31) - 1)
'''
“>” is an output operator that overwrites the existing file, while “>>” is also an output operator but appends the data in an already existing file
'''


