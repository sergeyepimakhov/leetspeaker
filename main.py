import sys
import re

vacabular = {
    'a': '4',
    #'b': 'ß',
    #'i': '!',
    's': '$',
    'o': '0'
}

if __name__ == "__main__":
    if len(sys.argv[1:]) == 1:
        input = sys.argv[1]
        output = str(input)
        output = re.sub("-", "", output)
        for key, value in vacabular.items():
            output = re.sub(key, value, output)
        print(output)
    else:
        print("Usage: python main.py 'yourstring")
