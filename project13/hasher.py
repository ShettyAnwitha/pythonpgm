import hashlib
filename = 'E:/hash.txt'
hasher = hashlib.md5()
with open(filename,'rb') as open_file:
    content = open_file.read()
    hasher.update(content)
print(hasher.hexdigest())
