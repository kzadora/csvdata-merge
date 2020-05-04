class BufferedIterator:
    def __init__(self, iter):
        self.iter = iter
        self.buf = []
        self.finished = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.finished:
            raise StopIteration()

        if len(self.buf) > 0:
            return self.buf.pop()
        else:
            try:
                return self.iter.__next__()
            except StopIteration as ex:
                self.finished = True
                raise ex

    def putBack(self, item):
        if self.finished:
            raise StopIteration()
        else:
            self.buf.append(item)
