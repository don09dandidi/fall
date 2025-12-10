from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional
from collections import deque

T = TypeVar('T')


class Queue(ABC, Generic[T]):
    """Abstract Queue interface/protocol"""
    
    @abstractmethod
    def enqueue(self, item: T) -> None:
        """Add item to queue"""
        pass
    
    @abstractmethod
    def dequeue(self) -> Optional[T]:
        """Remove and return item from queue"""
        pass
    
    @abstractmethod
    def is_empty(self) -> bool:
        """Check if queue is empty"""
        pass
    
    @abstractmethod
    def size(self) -> int:
        """Return queue size"""
        pass


class ArrayQueue(Queue[T]):
    """Queue implementation using list"""
    
    def __init__(self):
        self._items = []
    
    def enqueue(self, item: T) -> None:
        self._items.append(item)
    
    def dequeue(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._items.pop(0)
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    def size(self) -> int:
        return len(self._items)


class LinkedQueue(Queue[T]):
    """Queue implementation using deque (double-ended queue)"""
    
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item: T) -> None:
        self._items.append(item)
    
    def dequeue(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._items.popleft()
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    def size(self) -> int:
        return len(self._items)


class CircularQueue(Queue[T]):
    """Queue implementation using circular buffer"""
    
    def __init__(self, capacity: int = 100):
        self._capacity = capacity
        self._items = [None] * capacity
        self._front = 0
        self._rear = 0
        self._size = 0
    
    def enqueue(self, item: T) -> None:
        if self._size == self._capacity:
            self._resize()
        self._items[self._rear] = item
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1
    
    def dequeue(self) -> Optional[T]:
        if self.is_empty():
            return None
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def size(self) -> int:
        return self._size
    
    def _resize(self):
        """Double capacity when full"""
        new_capacity = self._capacity * 2
        new_items = [None] * new_capacity
        for i in range(self._size):
            new_items[i] = self._items[(self._front + i) % self._capacity]
        self._items = new_items
        self._front = 0
        self._rear = self._size
        self._capacity = new_capacity
