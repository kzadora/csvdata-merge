import unittest

from lib.buffered_iterator import BufferedIterator

class BufferedIteratorTests(unittest.TestCase):
    def test_empty_iterator(self):
        bi = BufferedIterator(iter([]))

        count = 0
        for item in bi:
            count += 1

        self.assertEqual(count, 0, 'Empty iterator should have no elements')