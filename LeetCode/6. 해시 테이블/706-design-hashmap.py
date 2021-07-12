# https://leetcode.com/problems/design-hashmap/

# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

import collections


class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        self._hashsize = 1009
        self.hash_table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        prev_node, hash_node = self._get_node(key)

        # if the key doesn't exist
        if prev_node is None:
            self.hash_table[self._hash(key)] = ListNode(key, value)
            return

        # if the key already exists
        if hash_node:
            hash_node.value = value
            return

        prev_node.next = ListNode(key, value)

    def get(self, key: int) -> int:

        prev_node, hash_node = self._get_node(key)

        # if there's no mapping for the key
        if hash_node is None:
            return -1
        else:
            return hash_node.value

    def remove(self, key: int) -> None:
        hash_index = self._hash(key)
        prev_node, hash_node = self._get_node(key)
        if hash_node is None:
            return

        if prev_node == hash_node:
            if hash_node.next is None:
                self.hash_table[hash_index] = ListNode()
            else:
                self.hash_table[hash_index] = hash_node.next
            return

        prev_node.next = hash_node.next
        del hash_node

    def _get_node(self, key: int) -> tuple:
        prev_node = hash_node = self.hash_table[self._hash(key)]

        # if there's no mapping for the key
        if hash_node.value is None:
            return None, None

        # if there's mapping for the key
        while hash_node:
            if hash_node.key == key:
                return prev_node, hash_node
            prev_node, hash_node = hash_node, hash_node.next

        return prev_node, hash_node

    def _hash(self, key: int) -> int:
        # hash function
        hashval = key % self._hashsize
        return hashval


# test case
obj = MyHashMap()
obj.put(2, 1)
print(obj.get(2))
obj.put(10002, 2)
print(obj.get(2))
obj.remove(10002)
print(obj.get(2))
print(obj.get(10002))
