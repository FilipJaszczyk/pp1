class Queue:

    def __init__(self):
        self.queue = []

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def push(self, item):
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)


queue1 = Queue()
queue1.push(1)
queue1.push(2)
queue1.push(3)
queue1.push(4)
queue1.push(5)
print(queue1)
queue1.pop()
queue1.pop()
queue1.pop()
print(queue1)
