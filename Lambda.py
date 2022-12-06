def separator(title):
    print(f'\n\n\n\n+++++++++++++{title}++++++++++++++++++++\n')
#Lambda functions are the small anonymous functions that can only have one expression

#lambda argumet(s) : expression

#standard representation

def double(x):
    return x+x

print("using the named function ", double(5))


separator("Using the Lambda")
print("using the lambda ", (lambda x:x+x)(5))

