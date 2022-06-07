with open('img01.txt', 'r') as fp:
    data = fp.read()

data = data.replace('\n', ' ')
data = data.split(' ')
data = [int(x) for x in data[:-1]]

print(len(data))

data = [data[x*128:(x+1)*128] for x in range(64)]
print(data)