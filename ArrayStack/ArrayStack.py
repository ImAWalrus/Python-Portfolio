
import unittest
class EmptyStack(Exception):
    """Custom Exception"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise EmptyStack('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise EmptyStack('Stack is empty')
    return self._data.pop()               # remove last item from list

  def get_data(self):
        """returns the underlying data structure for the stack."""
        return self._data

  def push_seq(self, seq):
      """Iteratively push each element in seq to stack."""
      for i in seq:
          self._data.append(i)

  def as_string(self, s):
      if not s:
          return ''
      return self.as_string(s[1:]) + str(s[0]) + ' '

class TestArrayStackMethods(unittest.TestCase):
    """Unit tests for ArrayStack"""

    def test_init(self):
        array = ArrayStack()
        self.assertEqual(len(array), 0)

    def test_is_empty(self):
        array = ArrayStack()
        with self.assertRaises(EmptyStack):
            array.top()

    def test_push(self):
        array = ArrayStack()
        array.push("Pizza")
        self.assertEqual(array.top(), "Pizza")

    def test_push_seq(self):
        array = ArrayStack()
        array.push_seq(["Burger","BBQ","Pie"])
        self.assertEqual(len(array.get_data()), 3)

    def test_top(self):
        array = ArrayStack()
        array.push("Burrito")
        self.assertEqual(array.top(), "Burrito")

    def test_top_exception(self):
        """Tests whether top correctly raises EmptyStack exception."""
        array = ArrayStack()
        with self.assertRaises(EmptyStack):
            array.top()

    def test_pop(self):
        array = ArrayStack()
        array.push("IceCream")
        array.push("Bacon")
        array.pop()
        self.assertEqual(len(array), 1)

    def test_get_data(self):
        array = ArrayStack()
        array.push_seq(["Bacon", "CheeseBurger"])
        self.assertEqual(array.get_data(), ["Bacon", "CheeseBurger"])

    def test_pop_exception(self):
        """Tests whether pop correctly raises EmptyStack exception."""
        array = ArrayStack()
        with self.assertRaises(EmptyStack):
            array.pop()

    def test_as_string(self):
        """Tests that as_string correctly lists the contents of the stack in indicated order (bottom -> top)."""
        array = ArrayStack()
        array.push_seq([1,2,3,4,5])
        self.assertEqual(array.as_string(array.get_data()), '5 4 3 2 1 ')

if __name__ == '__main__':
    unittest.main()
    test_as_string()
