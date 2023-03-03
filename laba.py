import string


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang  # Язык
        self.letters = letters  # Список букв

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    _letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letters):
        return letters in string.ascii_uppercase

    def letters_num(self):
        return self._letters_num

    @staticmethod
    def example():
        return 'something'


pt = EngAlphabet()
print(pt.letters)
print(pt.letters_num())
print(pt.is_en_letter('F'))
print(pt.is_en_letter('П'))
print(pt.example())


