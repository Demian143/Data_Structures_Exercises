from hash_table.hash_table1 import HashTable

""" I dicided to re-use the HashTable class to get used with the Hash Table 
    idea, so I traded complexity for knowledge. """


class PoemReciter(HashTable):
    def __setitem__(self, key):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx][1] = element[1] + 1
                found = True
                break
        if not found:
            self.arr[h].append([key, 1])

    def poem_reader(self):
        with open('hash_table/poem.txt', 'r') as f:
            for line in f:
                for word in line.split():
                    self.__setitem__(word)

        return self.arr


if __name__ == '__main__':
    poem = PoemReciter()
    poem.__setitem__('curves')
    poem.__setitem__('curves')
    poem.__setitem__('curves')
    poem.__setitem__('curves')

    print(poem.poem_reader())
    print('diverged:', poem['diverged'])
    print('in:', poem['in'])
    print('I:', poem['I'])
