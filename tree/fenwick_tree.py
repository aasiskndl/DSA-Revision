"""
It is binary indexed tree, that efficiently manages an array of values, allowing for both 
point updates (changing a single element) and prefix sum queries (calculating the cumulative sum
up to a specific index) in logarithmic time.

core idea: instead of storing full segments like segment tree, 
- store partical sums at clever indeces
- indices are chosen using binary properties
"""

class Fenwick:
    def __init__(self, n):
        self.n = n 
        self.tree = [0] * (n+1)
        
    # add value at index i 
    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] += val
            i += i & -i
            
    # prefix sum form 0 to i
    def query(self, i):
        i += 1
        s = 0 
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s
    
    # range sum L to R
    def range_sum(self, L, R):
        return self.query(R) - self.query(L - 1)
    
arr = [2, 5, 1, 4]
ft = Fenwick(len(arr))

# build tree
for i, val in enumerate(arr):
    ft.update(i, val)

print(ft.range_sum(1,3))
ft.update(2,9)
print(ft.range_sum(1,3))    
    
    