import string
import random



def main():
    key = ""
    valid_charset = list(c for c in string.printable if not c.isspace())

    for i in range(8):
        char = random.choice(valid_charset)
        second_char = chr(ord(char)+1)
        key+=char+second_char
    

    print(key)

if __name__ == "__main__":
    main()