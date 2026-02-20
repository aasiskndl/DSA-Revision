"""
It is a tree based Data structure used to efficiently perform:
- range queries(sum, min, max, gcd, etc)
- point updates
on an array, in O(log n) time per operation.

core idea is: instead of recomputing sums again and again:
- we store results of smaller segments
- combine them to answer larger queries quickly

"""

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self._build(nums, 0, 0, self.n - 1)
        
    # build
    def _build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
        else:
            mid = (start + end) // 2
            
            # build left and right 
            self._build(nums, 2 * node +1, start, mid)
            self._build(nums, 2 * node + 2, mid + 1, end)
            
            # merge
            self.tree[node] = self.tree[2*node +1] + self.tree[2 * node + 2]
            
    # query
    def query(self, left, right):
        return self._query(0,0,self.n - 1, left, right)
    
    def _query(self, node, start, end, L, R):
        # no overlap
        if R < start or end < L:
            return 0 
        
        # total overlap 
        if L <= start and end <= R:
            return self.tree[node]
        
        # partial overlap 
        mid = (start + end) // 2
        left_sum = self._query(2 * node + 1, start, mid, L, R)
        right_sum = self._query(2 * node + 2, mid + 1, end, L, R)
        
        return left_sum + right_sum 
    
    
    def update(self, index, value):
        self._update(0, 0, self.n-1, index, value)
        
    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            
            if idx <= mid:
                self._update(2 * node + 1, start, mid, idx,val)
            else:
                self._update(2 * node + 2, mid + 1, end, idx, val)
                
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
            
arr = [2,5,1,4]
st = SegmentTree(arr)

print(st.query(1,3))

st.update(2,10)
print(st.query(1,3))
