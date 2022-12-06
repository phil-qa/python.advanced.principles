

def separator(title):
    print(f'\n\n\n\n+++++++++++++{title}++++++++++++++++++++\n')

distances = [100, 89, 33,108]
locations = ['Birmingham', 'Gloucester', 'Cirencester', 'Solihul']

separator("First case using zip")
print(dict(zip(locations,distances)))

separator("using dictionary comprehension")
print({key : value for key, value in zip(locations, distances)})

separator("Develop a list of tuples using zip and map")
print(zip(locations, distances))
print(map(locations, distances))
for element in map(locations, distances):
    print(element)