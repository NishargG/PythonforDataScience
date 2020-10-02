import numpy 
'''a=numpy.array([1,2,3])
print(a)
numarray=numpy.arange(1000)
print(numarray)  
#//numarray
hey=1000000
a1=numpy.arange(hey)
a2=numpy.arange(hey)
#numpy array arithemetic
a3=a1+a2
print(a3[0:5:1])
a3=a1*a2
print(a3[0:5:1])
a3=a1-a2
print(a3[0:5:1])
a3=a1/a2
print(a3[0:5:1])'''
#basic array operations of numpy
#aray.ndim prints number of dimensions
#a1.itemsize return sizeof element
a=numpy.array([[1,2],[1,2],[3,4]],dtype=numpy.float64)
print(a)
print(a.itemsize)
#a.dtype prints data ttype
print(a.dtype)
'''PS D:\Desktop\Codes> python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> np.twos(3,4)

AttributeError: module 'numpy' has no attribute 'twos'
>>> np.ones((3,4))
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]]) 
>>> np.zeros((3,4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.arange(1,5)
array([1, 2, 3, 4])
>>> np.arange'''
#np.linespace(1,5,10) produces linealry spaced 10 numbers b/w 1 and 5
b=numpy.array([[1,2],[3,4],[5,6]])
print(b.shape)
print(b.reshape(2,3))
#flatten a 2d array by b.ravel returns new array


#MATHEMATI<AL FU<S
#a.min() a.max() a.sum()
#in numpy coulumns| are axis 0
# rows_ are axis one
#numpy.sqrt(a) is sqrt funcs not a member function of cclass array though

#np.std(a) gives stddev of elements
print("\n")
a=numpy.array([[1,2],[3,4]])
b=numpy.array([[[5],[6],[7],[8]],[[5],[6],[7],[8]]])
#print(a.dot(b))

print(help(numpy))