class MojIterator:
    def __init__(self, limit=None):
        self.counter = -1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 2
        if self.limit is not None and self.counter >= self.limit:
            raise StopIteration
        else:
            return self.counter

# Bez limitu iterator będzie nieskońćzony
# it = MojIterator()

# Ale teraz można podać limit i iterator będzie dawałe elementy tylko do tego limitu
it = MojIterator(20)
for x in it:
    print(x)


# To jest równoważne:
# try:
# while True:
#     x = it.__next__()
#     print(x)
# except StopIteration:
#    pass

