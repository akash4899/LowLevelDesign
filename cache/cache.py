from node import Node

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.eviction_policy = eviction_policy
        self.mp = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keys = []

    def put(self, key, value):
        # print("here")
        if self.mp.get(key):
            node = self.mp[key]
            self._move_to_head(node)
            node.value = value

        if len(self.mp) == self.capacity:
            removed_node = self._remove_tail()
            del self.mp[removed_node.key]
            node = Node(key, value)
            self._add_to_head(node)
            self.mp[key] = node
        else:
            node = Node(key, value)
            self._add_to_head(node)
            self.mp[key] = node


    def get(self, key):
        if key in self.mp.keys():
            node = self.mp[key]
            self._move_to_head(node)
            print(key)
            print(f"Value for key {key} is {node.value}")
            return
        print(f"Key {key} doesnt exist.")
        return



    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

    def _remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)




