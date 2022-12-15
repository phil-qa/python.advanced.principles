from multiprocessing import Queue

things = ['my_thing', 'your_thing', 'their_thing', 'no_thing']
counter = 1
# instantiating a queue object
queue = Queue()
print('pushing items to queue:')
for thing in things:
    print('item no: ', counter, ' ', thing)
    queue.put(thing)
    counter += 1

print('\npopping items from queue:')
counter = 0
while not queue.empty():
    print('item no: ', counter, ' ', queue.get())
    counter += 1