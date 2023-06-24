from queue import Queue
queue = Queue()
queue.put(10)
queue.put(20)
queue.put(30)


print(queue.qsize())  


print(queue.get())  
print(queue.get())  


print(queue.empty())  


print(queue.queue[0])  

queue.queue.clear()
print(queue.qsize())  
