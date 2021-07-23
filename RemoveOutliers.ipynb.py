import numpy as np

print("kick")
k = input()
x = np.array([0])
while 1:
    print("give me number")
    a = raw_input()
    if a == 'q' or a == 'Q':
        break ;
    x = np.append(x, int(a))

x = np.delete(x, 0)

x = np.sort(x)

m = np.array([0])
for i in range(k):
    ll = x.size -1
    m = np.append(m, x[0])
    m = np.append(m, x[ll])
    x = np.delete(x, ll)
    x = np.delete(x, 0)

m = np.delete(m, 0)
print(x)
print(m)
