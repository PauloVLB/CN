import numpy as np
import matplotlib.pyplot as plt

def phi0(x):
    return 1

def phi1(x):
    return 2*x*x + 3

arq = open('pts', 'r')
lines = arq.readlines()
pts = np.array([[float(x) for x in line.split(' ')] for line in lines[1:]])

b = (np.sum(phi0(pts[:,0])*phi0(pts[:,0])))
c = (np.sum(phi0(pts[:,0])*phi1(pts[:,0])))
d = (np.sum(phi1(pts[:,0])*phi0(pts[:,0])))
e = (np.sum(phi1(pts[:,0])*phi1(pts[:,0])))
f = (np.sum(pts[:,1]*phi0(pts[:,0])))
g = (np.sum(pts[:,1]*phi1(pts[:,0])))

a = np.linalg.solve(np.array([[b, c],[d, e]]), np.array([[f],[g]]))

plt.scatter(pts[:,0], pts[:,1])
x = np.linspace(8, 11, 100)
plt.plot(x, a[0]*phi0(x)+a[1]*phi1(x))
plt.show()