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