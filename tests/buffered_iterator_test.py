import unittest

from lib.buffered_iterator import BufferedIterator

class BufferedIteratorTests(unittest.TestCase):

    def test_empty_iterator(self):
        bi = BufferedIterator(iter([]))

        count = 0
        for item in bi:
            count += 1

        self.assertEqual(count, 0, 'Empty iterator should have no elements')

    def test_put_back(self):
        bi = BufferedIterator(iter([1,2,3]))
        result = []
        first_try = True

        for item in bi:
            result.append(item)
            if first_try:
                bi.putBack(item)
            first_try = not first_try

        self.assertEqual(result, [1,1,2,2,3,3], 'putBack() does not work as expected')

    def test_no_put_back_on_exhausted_iterator(self):
        bi = BufferedIterator(iter([1,2]))

        for item in bi:
            pass

        self.assertRaises(StopIteration, lambda: bi.putBack(7))

    def test_put_back_into_empty_iterator(self):
        bi = BufferedIterator(iter([]))

        bi.putBack(1)
        bi.putBack(2)
        result = []

        for item in bi:
            result.append(item)

        self.assertEqual(result, [2,1], 'putBack() should have stack semantics')

        self.assertRaises(StopIteration, lambda: bi.putBack(3))
