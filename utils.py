import re
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(string: str):
    return NUM_OR_DOT_REGEX.search(string)

def isEmpty(string: str):
    return len(string) == 0

if __name__ == '__main__':
    print(NUM_OR_DOT_REGEX.search('2'))

    print(isEmpty(' '))