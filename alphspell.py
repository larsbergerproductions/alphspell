import csv


class Translator:
    def __init__(self, dictionary_path: str = "dict_nato.csv"):
        self.dictionary = self.__load_alphabet_file(dictionary_path)

    def __load_alphabet_file(self, file_path: str) -> dict:
        """this throws ValueError, if lines are malformed"""
        try:
            with open(file_path, 'r') as dict_file:
                return self.__dict_from_csv(dict_file)
        except FileNotFoundError:
            print(f"file {file_path} wasn't found. exiting.")
            exit(1)

    def __dict_from_csv(self, dict_file):
        csvreader = csv.reader(dict_file, delimiter=':')
        try:
            return dict(csvreader)
        except ValueError:
            print(f"file \"{dict_file.name}\" contains lines of unsupported format.")
            exit(2)

    def __spell_letter(self, letter):
        try:
            return self.dictionary[letter]
        except KeyError:
            return letter

    def spell_word(self, word: str):
        """ takes a string and returns the phonetic spelling as specified in
            the dict file"""
        return " ".join([self.__spell_letter(letter) for letter in word.upper()])


def main() -> None:
    print(Translator().spell_word("phonetic spelling 123"))


if __name__ == "__main__":
    main()
