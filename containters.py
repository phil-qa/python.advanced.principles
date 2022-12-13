#!/usr/local/bin/python3
"""
containers
Python 3 version
This is a simple implementation of Stack, Queue, and Deque
Under the covers these are all derived from a doubley
linked list class

Clive Darke QA
"""


class _Node:
    def __init__(self, Data):
        self.NextNode = None
        self.PrevNode = None
        self.Data = Data

    def SetNext(self, Next):
        self.NextNode = Next

    def SetPrev(self, Prev):
        self.PrevNode = Prev

    def __str__(self):
        return str(self.Data)

    def GetNext(self, current):
        return current.NextNode

    def GetPrev(self, current):
        return current.PrevNode


################################################################################

class _DLinkList:
    __delim = ','

    @classmethod
    def SetDelim(cls, delim):
        _DLinkList.__delim = delim

    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):

        StrList = []

        node = self.__head
        while node:
            StrList.append(str(node))
            node = node.NextNode

        return _DLinkList.__delim.join(StrList)

    def __len__(self):
        # Consider instead maintaining a class
        # variable holding the current length (like Perl)
        count = 0

        node = self.__head
        while node:
            count += 1
            node = node.NextNode

        return count

    def _AddToLeft(self, Data):
        NewNode = _Node(Data)

        if self.__head:
            NewNode.SetNext(self.__head)
            self.__head.SetPrev(NewNode)
        else:
            self.__tail = NewNode

        self.__head = NewNode
        NewNode.SetPrev(None)

    def _AddToRight(self, Data):

        NewNode = _Node(Data)

        if self.__tail:
            NewNode.SetPrev(self.__tail)
            self.__tail.SetNext(NewNode)
        else:
            self.__head = NewNode

        self.__tail = NewNode
        self.__tail.SetNext(None)

    def _GetNextFromLeft(self, from_node):
        if from_node is None:
            from_node = self.__head

        return from_node.NextNode

    def _GetNextFromRight(self, from_node):
        if from_node is None:
            from_node = self.__tail

        return from_node.PrevNode

    def _GetHead(self):
        return self.__head

    def _GetTail(self):
        return self.__tail

    def _RemoveFromLeft(self):
        if self.__head:
            OldHead = self.__head
            self.__head = OldHead.NextNode
            return OldHead.Data
        else:
            raise IndexError("Attempt to remove from an empty container")

    def _RemoveFromRight(self):
        if self.__tail:

            OldTail = self.__tail
            if self.__tail is self.__head:
                self.__head = None
                self.__tail = None
            else:
                self.__tail = OldTail.PrevNode
                if self.__tail:
                    self.__tail.SetNext(None)

            return OldTail.Data
        else:
            raise IndexError("Attempt to remove from an empty container")


################################################################################

class Stack(_DLinkList):
    """
    Implementation of a stack
    Items are placed on the stack and are accessed as First-In Last-Out (FILO)
    """

    def __init__(self):
        super(Stack, self).__init__()

    def push(self, Data):
        "Push an item onto the stack"
        super(Stack, self)._AddToLeft(Data)

    def pop(self):
        "Pop an item from the stack"
        return super(Stack, self)._RemoveFromLeft()

        # TODO __iter__
    def __iter__(self):
        pos = self._GetHead()
        while pos:
            yield pos.Data
            pos = self._GetNextFromLeft(pos)


###############################################################################

class Queue(_DLinkList):
    """
    Implementation of a queue
    Items are placed on the queue and are accessed as First-In First-Out (FIFO)
    """

    def __init__(self):
        super(Queue, self).__init__()

    def enqueue(self, Data):
        "Places an item in the queue"
        super(Queue, self)._AddToLeft(Data)

    def dequeue(self):
        "Remove and return the next item from the queue"
        return super(Queue, self)._RemoveFromRight()

        # TODO __iter__
    def __iter__(self):
        pos = self._GetTail()
        while pos:
            yield pos.Data
            pos = self._GetNextFromRight(pos)


###############################################################################

class Deque(_DLinkList):
    """
    Implementation of a double-ended queue
    Items are placed on either end and can be accessed from either end
    """

    def __init__(self):
        super(Deque, self).__init__()

    def unshift(self, Data):
        "Places an item on the left"
        super(Deque, self)._AddToLeft(Data)

    def pop(self):
        "Remove and return the item on the right"
        return super(Deque, self)._RemoveFromRight()

    def push(self, Data):
        "Places an item on the right"
        super(Deque, self)._AddToRight(Data)

    def shift(self):
        "Remove and return the item on the left"
        return super(Deque, self)._RemoveFromLeft()

        # Does it make sense to iterate through a deque?
        # TODO from_right()
    def from_right(self):
        pos = self._GetTail()
        while pos:
            yield pos.Data
            pos = self._GetNextFromRight(pos)

            # TODO from_left()

    def from_left(self):
        pos = self._GetHead()
        while pos:
            yield pos.Data
            pos = self._GetNextFromLeft(pos)


            ###############################################################################

if __name__ == "__main__":
    import sys

    print("STACK:")
    astack = Stack()
    astack.push(42)
    astack.push(37)
    astack.push(99)
    astack.push(12)

    print("Number of items in stack:", len(astack))

    print("stack iterator")
    print("Should print 12, 99, 37, 42")
    try:
        for item in astack:
            print(item)
    except TypeError as err:
        print("****", err, file=sys.stderr)

    print("\nQUEUE:")
    aqueue = Queue()
    aqueue.enqueue(12)
    aqueue.enqueue(99)
    aqueue.enqueue(37)
    aqueue.enqueue(42)

    print("Number of items in queue:", len(aqueue))

    print("queue iterator")
    print("Should print 12, 99, 37, 42")
    try:
        for item in aqueue:
            print(item)
    except TypeError as err:
        print("****", err, file=sys.stderr)

    print("\nDEQUE:")
    adeque = Deque()
    adeque.push(42)
    adeque.push(37)
    adeque.push(99)
    adeque.push(12)

    print("Number of items in deque:", len(aqueue))

    try:
        print("deque from_right iterator")
        for item in adeque.from_right():
            print(item)
    except AttributeError as err:
        print("****", err, file=sys.stderr)

    try:
        print("deque from_left iterator")
        for item in adeque.from_left():
            print(item)
    except AttributeError as err:
        print("****", err, file=sys.stderr)

        # TODO: List comprehensions

    print("the stack as it is ")
    print(astack)
    stack_as_list = [item for item in astack ]
    print("The stack list is ")
    print(stack_as_list)
    print("Using list()")
    stack_as_a_list = list(astack)
    print(stack_as_list)

    queue_as_a_list = [item for item in aqueue]
    print("queue as a list")
    print(queue_as_a_list)

    deque_as_a_list = [item for item in adeque.from_left()]
    print("deque as a list ")
    print(deque_as_a_list)
    deque_as_a_list = [item for item in adeque.from_right()]
    print(deque_as_a_list)
'''
11.	Iterators. Only the iterator functions are shown, which should be the same in either version of Python.
class Stack(_DLinkList):

    # TODO __iter__
    def __iter__(self):
        pos = self._GetHead()
        while pos:
            yield pos.Data
            pos = self._GetNextFromLeft(pos)

############################################

class Queue(_DLinkList):

    # TODO __iter__
    def __iter__(self):
        pos = self._GetTail()
        while pos:
            yield pos.Data
            pos = self._GetNextFromRight(pos)

############################################

class Deque(_DLinkList):

    def from_right(self):
        pos = self._GetTail()
        while pos:
            yield pos.Data
            pos = self._GetNextFromRight(pos)

    def from_left(self):
        pos = self._GetHead()
        while pos:
            yield pos.Data
            pos = self._GetNextFromLeft(pos)

2.	List comprehensions:
    slist = [item for item in astack]
    print slist

    qlist = [item for item in aqueue]
    print qlist

    ldeque = [item for item in adeque.from_left()]
    print ldeque

    rdeque = [item for item in adeque.from_right()]
    print rdeque


3.	Named tuple.  A Python 2 solution is shown, the Python 3 solution only differs by the print statements.
import platform
from collections import namedtuple
import sys

Version = namedtuple("Version", ['major', 'minor', 'patchlevel'])
nt = Version._make(platform.python_version_tuple())

print nt
print nt.major
print nt[1]

od = nt._asdict()
print od.keys()

for k, v in od.items():
    print "%-10s: %s" % (k, v)


'''

