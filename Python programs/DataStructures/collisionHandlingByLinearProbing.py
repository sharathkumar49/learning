
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def get_next_slot(self, h, val):

        for idx in range(h+1, len(self.arr)):
            if not self.arr[idx]:
                self.arr[idx] = val
                return
        for idx in range(0, h):
            if not self.arr[idx]:
                self.arr[idx] = val
                return

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        if self.arr[h]:
            self.get_next_slot(h, val)
        else:
            self.arr[h] = val

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del" ,index)
                del self.arr[arr_index][index]