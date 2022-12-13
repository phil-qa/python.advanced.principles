source = ['zero', 'wun', 'two', 'tree', 'fower', 'fife', 'six', 'seven', 'ait', 'niner', 'alpha', 'bravo', 'charlie',
          'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliet', 'kilo', 'lima', 'mike', 'november', 'oscar',
          'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whisky', 'xray', 'yankee', 'zulu']
import string  # delimit numerics


def merge(dictionary1, dictionary2):
    return (dictionary2.update(dictionary1))


def delimit_types(data_to_delimit):
    index_of_alphabet = source.index('alpha')
    numerics = source[0:index_of_alphabet]
    alphabet = source[index_of_alphabet:len(source)]
    return {"numerics": numerics, "alphabet": alphabet}


def develop_key_lists():
    numbers = list(string.digits)
    letters = list(string.ascii_uppercase)
    return {"numbers": numbers, "letters": letters}


def develop_dictionary(keys, values):
    return dict(zip(keys, values))


def main():
    code_values = delimit_types(source)
    code_keys = develop_key_lists()

    numbers_dict = develop_dictionary(code_keys['numbers'], code_values['numerics'])
    letters_dict = develop_dictionary(code_keys['letters'], code_values['alphabet'])
    merge(letters_dict, numbers_dict)
    codes = numbers_dict
    print(codes)

    while True:
        phrase = input("Input a phrase ")
        if phrase == "exit":
            break
        for chr in phrase:
            print(f"{codes[chr.upper()]} " if chr.upper() in codes.keys() else " ", end='')
        print('')


main()
