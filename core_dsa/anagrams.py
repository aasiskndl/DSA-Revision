'''
Docstring for dsa.core_dsa.anagrams
An anagram is a string/ word formed by rearranging the letters of another, using all original characters exactly once.
For eg: "listen" and "silent" are anagrams because they can be formed by interchanging the letters within them.

Time complexity: (O(N log N))

'''

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    freq = {}
    
    # count characters in s
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    # subtract counts using t 
    for ch in t:
        if ch not in freq:
            return False
        
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
        
    return True

print(is_anagram("listen", "silent"))
print(is_anagram("rat", "car"))