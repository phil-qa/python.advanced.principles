def translate_character(character_to_translate, dictionary):
    return dictionary[character_to_translate]
def load_dictionary():
    with open('phoneticlist.txt' , 'r') as f:
        translated = {line.split(',')[0]: ''.join([content for content in line.split(',')[1] if ord(content) > 31 and ord(content)<126]) for line in f.readlines()}
    return translated

dictionary = load_dictionary()


user_input = input("data to parse")
response = [translate_character(char.upper(), dictionary) for char in user_input if char.isalpha()]
print(''.join(response), end='')