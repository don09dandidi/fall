# task2_textdata.py
import sys
import string

class FileReader:
    @staticmethod
    def read_file_into_string(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

class TextData:
    def __init__(self, filename, text):
        self.__file_name = filename
        self.__text = text
        self.__number_of_vowels = sum(1 for c in text.lower() if c in "aeiou")
        self.__number_of_consonants = sum(1 for c in text.lower() if c in string.ascii_lowercase and c not in "aeiou")
        self.__number_of_letters = self.__number_of_vowels + self.__number_of_consonants
        self.__number_of_sentences = text.count('.') + text.count('!') + text.count('?')
        self.__longest_word = max(text.split(), key=len, default="")

    def __str__(self):
        return (
            f"File: {self.__file_name}\n"
            f"Letters: {self.__number_of_letters}\n"
            f"Vowels: {self.__number_of_vowels}\n"
            f"Consonants: {self.__number_of_consonants}\n"
            f"Sentences: {self.__number_of_sentences}\n"
            f"Longest word: {self.__longest_word}\n"
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task2_textdata.py <path_to_file>")
        sys.exit(1)

    path = sys.argv[1]
    text = FileReader.read_file_into_string(path)
    data = TextData(path, text)
    print(data)
# python3 task2.py text1.txt