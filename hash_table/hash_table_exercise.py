class NycWeather:

    def __init__(self):
        self.arr = []

    def read_file(self):
        # Reads the file and passes every day temperature to the list
        with open('hash_table/nyc_weather.csv', 'r') as f:
            for line in f.readlines()[1:]:
                formated = int(line.split(',')[1])
                self.arr.append(formated)

        return self.arr

    def get_everage(self):
        # What was the average temperature in first week of Jan
        total = 0
        for day in self.arr[:7]:
            total += day
        return total / 7

    def get_max(self):
        # What was the maximum temperature in first 10 days of Jan
        return max(self.arr[:10])


if __name__ == '__main__':
    wheater = NycWeather()
    wheater.read_file()
    print(wheater.get_everage())
    print(wheater.get_max())
