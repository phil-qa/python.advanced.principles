#!/usr/local/bin/python3
import sys
import unittest

if sys.version_info[0] == 2:  # Not named on 2.6
    from StringIO import StringIO
else:
    from io import StringIO

from containers import *

class containersTest (unittest.TestCase):
#class TestClass (object):

    def assertEqual(self, lhs, rhs):
        assert lhs == rhs
        
    def test_stack_push(self):
        astack = Stack()   
        astack.push(42)
        astack.push(37)
        astack.push(99)
        astack.push(12)
    
        actual = len(astack)
        required = 4
        self.assertEqual(actual, required)
        
    def test_stack_pop(self): 
        astack = Stack()   
        astack.push(42)
        astack.push(37)
        astack.push(99)
        astack.push(12)
         
        actual = astack.pop()
        required = 12
        self.assertEqual(actual, required)
        actual = astack.pop()
        required = 99
        self.assertEqual(actual, required)
        actual = astack.pop()
        required = 37
        self.assertEqual(actual, required)
        actual = astack.pop()
        required = 42
        self.assertEqual(actual, required)
     
        actual = len(astack)
        required = 0
        self.assertEqual(actual, required)
    
    def test_stack_iter(self):
        astack = Stack()   
        astack.push(42)
        astack.push(37)
        astack.push(99)
        astack.push(12)
        
        actual = [item for item in astack]
        required = [12, 99, 37, 42]
        self.assertEqual(actual, required)
    
    def test_stack_str(self):
        astack = Stack()   
        astack.push(42)
        astack.push(37)
        astack.push(99)
        astack.push(12)
        
        actual = str(astack)
        required = "12,99,37,42"
        self.assertEqual(actual, required)
    
    def test_empty_stack(self):
        astack = Stack()
        self.assertRaises(IndexError, lambda: astack.pop())
    
    def test_queue_enqueue(self):
        aqueue = Queue()   
        aqueue.enqueue(42)
        aqueue.enqueue(37)
        aqueue.enqueue(99)
        aqueue.enqueue(12)
    
        actual = len(aqueue)
        required = 4
        self.assertEqual(actual, required)
        
    def test_queue_dequeue(self): 
        aqueue = Queue()   
        aqueue.enqueue(42)
        aqueue.enqueue(37)
        aqueue.enqueue(99)
        aqueue.enqueue(12)
         
        actual = aqueue.dequeue()
        required = 42
        self.assertEqual(actual, required)
        actual = aqueue.dequeue()
        required = 37
        self.assertEqual(actual, required)
        actual = aqueue.dequeue()
        required = 99
        self.assertEqual(actual, required)
        actual = aqueue.dequeue()
        required = 12
        self.assertEqual(actual, required)
     
        actual = len(aqueue)
        required = 0
        self.assertEqual(actual, required)

    def test_queue_iter(self):
        aqueue = Queue()   
        aqueue.enqueue(42)
        aqueue.enqueue(37)
        aqueue.enqueue(99)
        aqueue.enqueue(12)
        
        actual = [item for item in aqueue]
        required = [42, 37, 99, 12]
        self.assertEqual(actual, required)
    
    def test_queue_str(self):
        aqueue = Queue()   
        aqueue.enqueue(42)
        aqueue.enqueue(37)
        aqueue.enqueue(99)
        aqueue.enqueue(12)
    
        actual = str(aqueue)
        required = "12,99,37,42"
        self.assertEqual(actual, required)
        
    def test_deque_push(self):
        adeque = Deque()   
        adeque.push(42)
        adeque.push(37)
        adeque.push(99)
        adeque.push(12)
    
        actual = len(adeque)
        required = 4
        self.assertEqual(actual, required)
        
    def test_deque_pop(self): 
        adeque = Deque()   
        adeque.push(42)
        adeque.push(37)
        adeque.push(99)
        adeque.push(12)
         
        actual = adeque.pop()
        required = 12
        self.assertEqual(actual, required)
        actual = adeque.pop()
        required = 99
        self.assertEqual(actual, required)
        actual = adeque.pop()
        required = 37
        self.assertEqual(actual, required)
        actual = adeque.pop()
        required = 42
        self.assertEqual(actual, required)
     
        actual = len(adeque)
        required = 0
        self.assertEqual(actual, required)

    def test_deque_unshift(self):
        adeque = Deque()   
        adeque.unshift(42)
        adeque.unshift(37)
        adeque.unshift(99)
        adeque.unshift(12)
    
        actual = len(adeque)
        required = 4
        self.assertEqual(actual, required)
        
    def test_deque_shift(self): 
        adeque = Deque()   
        adeque.unshift(42)
        adeque.unshift(37)
        adeque.unshift(99)
        adeque.unshift(12)
         
        actual = adeque.shift()
        required = 12
        self.assertEqual(actual, required)
        actual = adeque.shift()
        required = 99
        self.assertEqual(actual, required)
        actual = adeque.shift()
        required = 37
        self.assertEqual(actual, required)
        actual = adeque.shift()
        required = 42
        self.assertEqual(actual, required)
     
        actual = len(adeque)
        required = 0
        self.assertEqual(actual, required)

        
if __name__ == '__main__':
    #unittest.main()
    

    import trace
    # Create a trace object.  trace=0: don't display lines, count=1: create output files
    tobj = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix],
                       count=1, trace=0)  
    tobj.runfunc(unittest.main, exit=False)  # Exit = False allows the prog to continue
    results = tobj.results()   # create a CoverageResults object

    results.write_results(summary=True,coverdir='.') 

    
    print("ending")