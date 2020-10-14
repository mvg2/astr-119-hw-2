import numpy as np          # import numpy library

# integers

i = 10          # integer
print("The type of i is", type(i))  # print out the data type of i

a_i = np.zeros(i, dtype=int)        # declare an array of ints
print("The type of a_i is", type(a_i))        # print out the data type (nd array)
print("The type of a_i[0] is", type(a_i[0]))  # print out the data type (int64)

# floats

x = 119.0       # floating point number
print("The type of x is", type(x))  # print out the data type of x

y = 1.19e2      # floating point number in scientific notation
print("The type of y is", type(y))  # print out the data type of y

z = np.zeros(i, dtype=float)        # array of floats
print("The type of z is", type(z))  # print out the data type (nd array)
print("The type of z[0] is", type(z[0]))      # print out the data type (float64)
