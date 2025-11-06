# task4_bonus.py
import sys
from task2 import FileReader, TextData

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task4_bonus.py <file1> <file2> ...")
        sys.exit(1)

    for path in sys.argv[1:]:
        text = FileReader.read_file_into_string(path)
        data = TextData(path, text)
        print(data)
        print("-" * 40)
