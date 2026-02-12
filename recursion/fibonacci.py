'''
Docstring for dsa.recursion.fibonacci
Recursion is a process where a function calls itself, either directl or indirectly, to solve a problem by breaking it down into smaller, identical sub-problems
until a simple "base case" is reached, which stops the process, preventing infinite loops.

'''

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

print(fact(3))