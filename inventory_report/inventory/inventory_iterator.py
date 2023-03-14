from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, inventory):
        self.inventory = inventory
        self.index = 0

    def __next__(self):
        if self.index >= len(self.inventory):
            raise StopIteration
        product = self.inventory[self.index]
        self.index += 1
        return product
