inp = open('8.in','r').readlines()

inp = [int(x) for x in inp[0]]

x = 25
y = 6
layers = int(15000/(25*6))
import numpy as np

def color(arr):
    for i in arr:
        if i!=2:
            return i


arr = np.array(inp).reshape((layers,6,25))
res = []
# Part 1
for l in range(layers):
    img = arr[l,:,:]
    print(img)
    count = np.count_nonzero(img)
    ones = np.count_nonzero(img == 1)
    twos = np.count_nonzero(img == 2)
    res.append((count, ones*twos))

print(max(res, key=lambda x: x[0]))


## Part 2
res = np.zeros((25,6))
for i in range(25):
    for j in range(6):
        line = arr[:, j, i]
        res[i][j] = color(line)

print(res.T)
for i in res.T:
    print("".join(str(int(j)) for j in i))
