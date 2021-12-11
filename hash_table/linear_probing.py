
class LinearProbing:
    """ Implement hash table where collisions are handled using linear probing. 
        We learnt about linear probing in the video tutorial. 
        Take the hash table implementation that uses chaining and modify methods to use linear probing. 
        Keep MAX size of arr in hashtable as 10. """

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        if len(self.arr[h]) == 1:
            if self.arr[h][0][0] == key:
                # updating values
                self.arr[h][0] = (key, val)
                return

            for emp_arr in self.arr:
                if len(emp_arr) == 0:
                    # probing linearly
                    emp_arr.append((key, val))
                    break

        else:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


if __name__ == '__main__':
    linear = LinearProbing()
    # linear['march 17'] = 17
    # print(linear['march 17'])
    linear['march 17'] = 18
    # breakpoint()
    linear['march 17'] = 19
    print(linear.arr)
    print('\n')
    linear['march 6'] = 68
    linear['march 6'] = 68
    print(linear.arr)
