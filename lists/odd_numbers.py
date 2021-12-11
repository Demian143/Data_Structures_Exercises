""" Create a list of all odd numbers between 1 and a max number.
    Max number is something you need to take from a user using input() function """


def get_odd_max():
    max_number = int(input('Give me a number: '))
    odd_numbers = [number for number in range(max_number) if number % 2 == 1]

    return odd_numbers


if __name__ == '__main__':
    print(get_odd_max())
