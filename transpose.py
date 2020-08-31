import sys, os

def read_file(filepath):
    wordlist = []
    with open(f'{filepath}', 'r') as wordlist_file:
        content = wordlist_file.readlines()
        for line in content:
            wordlist.append(line.rstrip())

    return wordlist

def find_larget(wordlist):
    longest_string = max(wordlist, key=len)
    return longest_string

def transpose_word(word):
    return word[::-1]

def init():
    if len(sys.argv) < 2:
        raise IndexError('Expecting only one arg as filepath')
    else:
        filepath = sys.argv[1]
        if os.path.exists(filepath) == False:
            raise FileNotFoundError('Invalid filepath')
        else:
            wordlist = read_file(filepath)
            largest_word = find_larget(wordlist)
            xposed_word = transpose_word(largest_word)

            print(largest_word)
            print(xposed_word)


if __name__ == "__main__":
    init()