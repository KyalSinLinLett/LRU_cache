
class Node:
    def __init__(self, key=None, val=None):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._count = 0
        self.head = Node()
        self.tail = Node()
        self.key_table = dict()

    def initialize_cache(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        return self._display_cache()

    def _insert(self, new_node):
        print(f"inserting {new_node.key}:{new_node.val}")
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.key_table[new_node.key] = new_node
        self._count += 1 if self._count < self._capacity else 0

    def _is_full(self):
        return self._count >= self._capacity

    def _remove_node(self, key):
        existing_node = self.key_table[key]
        prev_node = existing_node.prev
        next_node = existing_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        return existing_node

    def _update_head(self, key, val):
        removed_node = self._remove_node(key)
        removed_node.val = val
        self._insert(removed_node)

    def _update_last_node(self):
        new_last_node = self.tail.prev.prev
        self.tail.prev = new_last_node
        new_last_node.next = self.tail

    def _display_cache(self):
        curr = self.head
        cache_str = ""
        while (curr is not self.tail):
            cache_str += f"{curr.key}:{curr.val} -> " if curr.key != None else ""
            curr = curr.next
        return cache_str

    # API
    def get(self, key):
        value = self.key_table[key].val
        if value is not None:
            self._update_head(key, value)
            return value
        print("key not found")

    def put(self, key, val):
        if not key in self.key_table.keys():
            self._insert(Node(key, val))
            if self._is_full():
                self._update_last_node()
                self.key_table.pop(key)

        else:
            self._update_head(key, val)
            

# create LRU cache
lc = LRUCache(5)
# initialize cache
lc.initialize_cache()

lc.put('a', 1)
lc.put('b', 13)
lc.put('c', 23413)
lc.put('d', 113)
lc.put('e', 13111)
print(lc)
print()

lc.get('a')
print(lc)
print()

lc.put('f', 646)
print(lc)
print()

lc.put('g', 646)
print(lc)
print()

lc.put('hg', 3456)
print(lc)
print()

lc.get('a')
print(lc)
print()
