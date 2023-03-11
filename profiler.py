import time
import random
import statistics

def read_file():
    local_dict = {}
    with open('dictionary.csv', 'r') as file:

        for line in file.readlines():
            delimit = line.replace('"', '').replace('\n','').split(',')
            local_dict[delimit[0]] = delimit[2]

    return local_dict


def profile_this(thing, source, words):
    now = time.time()
    print(now)
    for word in thing(source, words):
        print(word)
    new_now = time.time()
    print(new_now)
    time_taken = new_now - now
    return time_taken

def finder(source, words):
    response = []
    for word in words:
       response.append(f'The meaning of {word} is {source[word]}')
    return response



english_dict = read_file()
blocks = []
for block in range(100):
    random_set = random.sample(list(english_dict.keys()), 5000)
    blocks.append(random_set)

timings = []
for block in blocks:
    timings.append(profile_this(finder, english_dict, block))

print(f'The mean search time was {statistics.mean(timings)} the range was {statistics.stdev(timings)} quartiles {statistics.quantiles(timings)}')