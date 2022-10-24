import re


class Textfile:
    def __init__(self, file):
        if not isinstance(file, str):
            raise Exception(f'The argument u\'re passing as a path to a file must be a string')
        if not file[len(file)-4:] == '.txt':
            raise Exception(f'The parameter u passed is not txt file')
        self.txt_file = file

    @property
    def txt_file(self):
        return self.__txt_file

    @txt_file.setter
    def txt_file(self, value):
        if not isinstance(value, str):
            raise Exception(f'The argument u\'re passing as a path to a file must be a string')
        if not value[len(value)-4:] == '.txt':
            raise Exception(f'The parameter u passed is not txt file')
        self.__txt_file = value

    def symbols_quantity(self):
        symbols_quantity = 0
        with open(self.txt_file, "r") as f:
            for line in f:
                symbols_quantity += len(line)
        return symbols_quantity

    def words_quantity(self):
        words_quantity = 0
        with open(self.txt_file, "r") as f:
            for line in f:
                words_quantity += len(re.findall(r'[\'\-\w]+', line))
        return words_quantity

    def sentences_quantity(self):
        sentences_quantity = 0
        with open(self.txt_file, "r") as f:
            for line in f:
                sentences_quantity += len(re.findall(r'\b[\.\!\?]', line))
            return sentences_quantity


txt1 = Textfile('ex4.txt')
print(f'Quantity of symbols: {txt1.symbols_quantity()}\n'
      f'Quantity of words: {txt1.words_quantity()}\n'
      f'Quantity of sentences: {txt1.sentences_quantity()}')
