class BufferedIterator:
    def __init__(self, iter):
        self.iter = iter
        self.buf = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.buf) > 0:
            return self.buf.pop()
        else:
            return self.iter.__next__()

    def putBack(self, item):
        self.buf.append(item)
