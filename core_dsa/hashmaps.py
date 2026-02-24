
class _Node:
    def __init__(self, key, value, nxt=None):
        self.key = key
        self.value = value
        self.next = nxt

class HashMap:
    def __init__(self, initial_capacity=8, load_factor=0.75):
        self.capacity = max(4, initial_capacity)
        self.size = 0
        self.load_factor = load_factor
        # buckets: list of head nodes (or None)
        self.buckets = [None] * self.capacity

    def _bucket_index(self, key):
        # Python's hash() may be negative, but % capacity yields non-negative index
        return hash(key) % self.capacity

    def put(self, key, value):
        idx = self._bucket_index(key)
        node = self.buckets[idx]

        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next

        new_node = _Node(key, value, self.buckets[idx])
        self.buckets[idx] = new_node
        self.size += 1


        if self.size / self.capacity > self.load_factor:
            self._resize(self.capacity * 2)

    def get(self, key, default=None):
        idx = self._bucket_index(key)
        node = self.buckets[idx]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return default

    def remove(self, key):
        idx = self._bucket_index(key)
        node = self.buckets[idx]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[idx] = node.next
                self.size -= 1
                return node.value
            prev = node
            node = node.next
        raise KeyError(key)

    def contains_key(self, key):
        idx = self._bucket_index(key)
        node = self.buckets[idx]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False

    def _resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [None] * self.capacity
        old_size = self.size
        self.size = 0

        for head in old_buckets:
            node = head
            while node:
                self.put(node.key, node.value)
                node = node.next
        
        assert self.size == old_size

    def keys(self):
        for head in self.buckets:
            node = head
            while node:
                yield node.key
                node = node.next

    def values(self):
        for head in self.buckets:
            node = head
            while node:
                yield node.value
                node = node.next

    def items(self):
        for head in self.buckets:
            node = head
            while node:
                yield (node.key, node.value)
                node = node.next

    def __len__(self):
        return self.size

    def __repr__(self):
        items = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"HashMap({{{items}}})"



class HashSet:
    def __init__(self):
        self._map = HashMap()

    def add(self, key):
        self._map.put(key, True)

    def remove(self, key):
        return self._map.remove(key)

    def contains(self, key):
        return self._map.contains_key(key)

    def __len__(self):
        return len(self._map)

    def __iter__(self):
        return self._map.keys()

    def __repr__(self):
        return "HashSet({" + ", ".join(repr(k) for k in self) + "})"


# Example usage
if __name__ == "__main__":
    m = HashMap()
    m.put("apple", 3)
    m.put("banana", 5)
    m.put("apple", 4)  
    print(m.get("apple"))    
    print(m.get("cherry", "missing"))  
    print("banana" in [k for k in m.keys()])  
    print(m) 

    s = HashSet()
    s.add("red")
    s.add("blue")
    s.add("red")   
    print(len(s))  
    print(s.contains("green")) 
    print(s)  