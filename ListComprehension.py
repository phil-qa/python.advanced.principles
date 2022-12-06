import glob
import os

def separator(title):
    print(f'\n\n\n\n+++++++++++++{title}++++++++++++++++++++\n')

#source pattern
pattern = f'C:/program files/*'

#develop basic list comprehension
separator('basic list comprehension')
sizes = [os.path.getsize(file_name) for file_name in glob.iglob(pattern)]
print(sizes)


#develop advanced list comprehension
separator('advanced list comprehension')
file_details = [{'name': file_name, 'size': os.path.getsize(file_name)} for file_name in glob.iglob(pattern)]
print(file_details)



#develop advanced list comprehension with filter
separator('advanced list comprehension with filter')
file_details = [{'name': file_name, 'size': os.path.getsize(file_name)} for file_name in glob.iglob(pattern) if os.path.isdir(file_name)]
print(file_details)

#show sets in comprehension
separator('Sets in comprehension')
def get_size(value):
    return(len(value))

test_set = {'Liverpool', 'Manchester', 'Everton'}

results = {get_size(ob) for ob in test_set}

print(results)

#dictionaries in comprehension:
separator('Using dictionary in comprehension')
print('develop a basic tuple series')
series = [(file_name, os.path.getsize(file_name)) for file_name in glob.iglob(pattern) ]
print('develop a dictionary from the tuple series')
dictionary_details = {file_name: size for file_name, size, in series if size>0}

print(dictionary_details)