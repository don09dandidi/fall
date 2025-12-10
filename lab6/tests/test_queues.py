import unittest


class TestQueues(unittest.TestCase):
    """Test all queue implementations"""
    
    def test_array_queue_basic_operations(self):
        """Test ArrayQueue enqueue and dequeue"""
        queue = ArrayQueue()
        
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)
        
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size(), 3)
        
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.size(), 1)
        
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.is_empty())
    
    def test_linked_queue_with_strings(self):
        """Test LinkedQueue with strings"""
        queue = LinkedQueue()
        
        queue.enqueue("first")
        queue.enqueue("second")
        queue.enqueue("third")
        
        self.assertEqual(queue.dequeue(), "first")
        self.assertEqual(queue.dequeue(), "second")
        self.assertEqual(queue.dequeue(), "third")
        self.assertIsNone(queue.dequeue())
    
    def test_circular_queue_capacity(self):
        """Test CircularQueue resizing"""
        queue = CircularQueue(capacity=2)
        
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)  # Should trigger resize
        
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
