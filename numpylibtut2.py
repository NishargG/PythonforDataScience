import numpy as np 
#numpy supports similar indexing as native python lists
#with exceptions
a=np.array([[1,2,3],[6,7,8],[4,5,6]])
print(a[0:2,2])
print(a[-1])
print(a[0:3:2,0:3:2])
for cell in a.flat:
    print(cell)
#cool pythonic code
a=np.arange(6).reshape(3,2)

b=np.arange(6,12).reshape(3,2)
print(np.vstack((a,b)))
print(np.hstack((a,b)))

c=np.arange(30).reshape(2,15)
c=np.hsplit(c,3)
print(c)
a=np.arange(12).reshape(3,4)
b=a>4
print(b)
#this is fucking lit man
#some type of hasing wtf?
print(a[b])