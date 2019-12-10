
import unittest
class EmptyStack(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
          self._element = element
          self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def push_seq(self, seq):
        for i in seq:
            self._head = self._Node(i, self._head)
            self._size += 1

    def top(self):
        if self.is_empty():
            raise EmptyStack('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise EmptyStack('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def as_string(self,s,temp_Head):
        if temp_Head != None:
            s = s + str(temp_Head._element)
            temp_Head = temp_Head._next
            return self.as_string(s,temp_Head)
        return s

    def get_head(self):
        return self._head

class TestLinkedStackMethods(unittest.TestCase):
    def test_init(self):
        stack = LinkedStack()
        self.assertEqual(len(stack), 0)

    def test_is_empty(self):
        stack = LinkedStack()
        with self.assertRaises(EmptyStack):
            stack.top()

    def test_push(self):
        stack = LinkedStack()
        stack.push("Pizza")
        self.assertEqual(stack.top(), "Pizza")

    def test_push_seq(self):
        stack = LinkedStack()
        stack.push_seq(["Burger","BBQ", "Pie"])
        self.assertEqual(len(stack), 3)

    def test_top(self):
        stack = LinkedStack()
        stack.push("Meat Tornado")
        self.assertEqual(stack.top(), "Meat Tornado")

    def test_top_exception(self):
        stack = LinkedStack()
        with self.assertRaises(EmptyStack):
            stack.top()

    def test_pop(self):
        stack = LinkedStack()
        stack.push("Ice-Cream")
        stack.push("Bacon")
        stack.pop()
        self.assertEqual(len(stack), 1)

    def test_pop_exception(self):
        stack = LinkedStack()
        with self.assertRaises(EmptyStack):
            stack.pop()

    def test_as_string(self):
        stack = LinkedStack()
        stack.push_seq(["Bacon","Burrito", "Pizza"])
        tempHead = stack.get_head()
        stack.as_string("",tempHead) #Not sure if you wanted us to print the string

if __name__ == '__main__':
    unittest.main()
