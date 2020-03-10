class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next is not None:
            cur = cur.next
            yield cur.data
    def insert(self, idx, value):
        cur = self.head
        cur_idx = 0
        if cur is None:
            raise Exception('串列為空')
        while cur_idx < idx-1:
            cur = cur.next
            if cur.next is None:
                raise Exception('索引超過範圍')
            cur_idx += 1
        node = Node(value)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node
    def remove(self, idx):
        cur = self.head
        cur_idx = 0
        if cur is None:
            raise Exception('串列為空')
        while cur_idx < idx - 1:
            cur = cur.next
            if cur.next is None:
                raise Exception('索引超過範圍')
            cur_idx += 1
        if idx == 0:
            self.head = cur.next
            cur = cur.next
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return
        cur.next = cur.next.next
        if cur.next is None:
            self.tail = cur
    def size(self):
        cur = self.head
        count = 0
        if cur is None:
            return '串列為空'
        while cur is not None:
            cur = cur.next
            count += 1
        return count
    def search(self, item):
        cur = self.head
        found = False
        while cur is not None and not found:
            if cur.data == item:
                found = True
            else:
                cur = cur.next
        return found
