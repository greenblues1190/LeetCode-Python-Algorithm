class BinaryHeap(object):
    def __init__(self) -> None:
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        index = len(self)
        parent = index // 2
        while parent > 0:
            if self.items[index] < self.items[parent]:
                self.items[index], self.items[parent] = self.items[parent], self.items[index]
            index = parent
            parent = index // 2

    def _percolate_down(self, index):
        left = 2 * index
        right = left + 1
        smallest = index

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != index:
            self.items[smallest], self.items[index] = self.items[index], self.items[smallest]
            self._percolate_down(smallest)

    def insert(self, item):
        self.items.append(item)
        self._percolate_up()

    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items.pop()
        self._percolate_down(1)
        return extracted
