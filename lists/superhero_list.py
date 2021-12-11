
class HerosList:

    def __init__(self):
        self._heros = ['spider man', 'thor',
                       'hulk', 'iron man', 'captain america']

    def list_len(self):
        """ 1. Length of the list """
        return len(self._heros)

    def add_hero(self):
        """ 2. Add 'black panther' at the end of this list """
        self._heros.append('Black Panther')
        return self._heros

    def update_index(self):
        """ 3. You realize that you need to add 'black panther' after 'hulk',
            so remove it from the list first and then add it after 'hulk' """
        self._heros.remove('Black Panther')
        self._heros.insert(3, 'Black Panther')
        return self._heros

    def change_heros(self):
        """ 4. Now you don't like thor and hulk because they get angry easily :)
            So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
            Do that with one line of code. """
        self._heros[1:3] = ['Doctor Strange']
        return self._heros

    def sort_heros(self):
        """ 5. Sort the heros list in alphabetical order 
           (Hint. Use dir() functions to list down all functions available in list) """
        self._heros.sort()
        return self._heros


if __name__ == '__main__':
    heros = HerosList()
    print(heros.list_len())
    print(heros.add_hero())
    print(heros.update_index())
    print(heros.change_heros())
    print(heros.sort_heros())
