from queue import Queue

s = Queue()

s.put(1)
s.put(2)
s.put(3)

print(s.qsize())

s.get()
s.get()

print(s.qsize())