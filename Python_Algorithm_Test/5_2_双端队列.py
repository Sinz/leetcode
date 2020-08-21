class Deque(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self,item): # 队头添加元素
        self.items.insert(0,item)

    def add_rear(self,item): # 队尾添加元素
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)
    
    def remove_rear(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print (deque.size())
    print (deque.remove_front())
    print (deque.remove_front())
    print (deque.remove_rear())
    print (deque.remove_rear())

