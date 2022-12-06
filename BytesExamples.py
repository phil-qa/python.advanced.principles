test_string = 'Prógrammïng'

enc = bytes(test_string, 'ascii', errors='ignore')

print('Bytes conversion with ignore', enc)

enc = bytes(test_string, 'ascii', errors='replace')

print('Bytes conversion with replace', enc)

enc = bytes(test_string, 'ascii', errors='strict')

print('Bytes conversion with strict', enc)