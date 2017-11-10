#!env python

'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.

By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
even-valued terms

--

Solution -
1. Create a generator that yields fibonacci numbers
2. Wrap it in a filter that only lets even numbers through
3. Sum up the values coming out of the filter

'''

def createFibonacciGenerator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    evenFibs = filter(lambda x: x % 2 == 0, createFibonacciGenerator(4e6))
    print("Sum of even-values fibonacci terms that do not exceed 4 million: ", sum(evenFibs))

'''Output
Sum of even-values fibonacci terms that do not exceed 4 million:  4613732
'''