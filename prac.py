class HashMap:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if (len(element) == 2 and element[0] == key):
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for i in self.arr[h]:
            if i[0] == key:
                return i[1]
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, value in enumerate(self.arr[h]):
            if value[0] == key:
                del self.arr[h][index]


HashTable = HashMap()

HashTable['march 6'] = 4
HashTable['march 17'] = 25
HashTable['John'] = 2
HashTable['lol'] = 3
HashTable['hey'] = 4

del HashTable['John']

print(HashTable.arr)