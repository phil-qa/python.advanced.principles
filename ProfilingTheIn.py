from time import time


def profiler(executable):
    now = time()
    print(now)
    executable
    finish = time()
    print(finish)
    print(f"difference = {finish-now}")


def searcher_one():
    with open("Shakespeare.as.you.like.it.txt", 'r') as fi:
        for x in range(1000000):
            for line in fi.readlines():
                for content in line:
                    if content == "bacon":
                        print("here")

def searcher_two():
    with open("Shakespeare.as.you.like.it.txt", 'r') as fi:
        for x in range(1000000):
            if 'bacon' in fi:
                print("here")

test_one = searcher_one

test_two = searcher_two()

profiler(test_one())

profiler(test_two())