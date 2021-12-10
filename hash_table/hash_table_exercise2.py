from hash_table.hash_table1 import HashTable

""" I dicided to re-use the HashTable class to get used with the Hash Table 
    idea, so I traded complexity for knowledge."""


class NycWeather(HashTable):
    def set_days(self):
        with open('hash_table/nyc_weather.csv', 'r') as f:
            # hashtable = HashTable()
            for line in f.readlines()[1:]:
                array = line.split(',')
                self.__setitem__(array[0], int(array[1]))

        return self.arr


if __name__ == '__main__':
    weather = NycWeather()
    # breakpoint()
    print(weather.set_days())
    # What was the temperature om Jan 9?
    print(weather['Jan 9'])
    # What was the temperature on Jan 4?
    print(weather['Jan 4'])
