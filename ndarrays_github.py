#!/usr/bin/env python
# coding: utf-8

# # NumPy `ndarray`: A Multidimensional Array Object
# NumPy's `ndarray` is a fast, flexible container for large datasets in Python. It enables mathematical operations on whole blocks of data using syntax similar to scalar operations.

# In[20]:


import numpy as np
# NumPy's ndarray is a fast, flexible container for large datasets in Python.
# It enables mathematical operations on whole blocks of data using syntax similar to scalar operations.


# In[21]:


# Generate a 2x3 array of random numbers
data = np.random.randn(2, 3)
# Display the array
print('Random Data Array:\n', data)


# In[22]:


# Perform a mathematical operation: multiply all elements by 10
data_multiplied = data * 10
# Display the result of the multiplication
print('\nData Array Multiplied by 10:\n', data_multiplied)


# In[23]:


# Perform another mathematical operation: add the array to itself
data_added = data + data
# Display the result of the addition
print('\nData Array Added to Itself:\n', data_added)


# Each element in the array is multiplied by 10 in the first example, and the corresponding elements are added in the second example.
# 
# An `ndarray` is a multidimensional container for homogeneous data. It has attributes like `shape` and `dtype` that provide information about the array's dimensions and data type.

# In[24]:


# Check the shape of the array (number of rows and columns)
print('\nShape of the Data Array:', data.shape)

# Check the data type of the elements in the array
print('Data Type of the Array Elements:', data.dtype)


# In[ ]:





# ### Creating ndarrays using different methods:

# In[25]:


# 1. Convert a list to a NumPy array
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
# Display the array created from the list
print('\nArray Created from List:', arr1)


# In[26]:


# 2. Convert a nested list to a multidimensional array
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
# Display the multidimensional array
print('\nMultidimensional Array Created from Nested List:\n', arr2)

# Check the number of dimensions of the array
print('\nNumber of Dimensions of arr2:', arr2.ndim)

# Check the shape of the array
print('Shape of arr2:', arr2.shape)

# Check the data type of the array elements
print('Data Type of arr1:', arr1.dtype)
print('Data Type of arr2:', arr2.dtype)


# In[27]:


# Creating arrays using other NumPy functions:

# 1. Create an array of zeros with a specified length
zeros_array = np.zeros(10)
# Display the array of zeros
print('\nArray of Zeros:', zeros_array)

# 2. Create a 3x6 array of zeros
zeros_2d_array = np.zeros((3, 6))
# Display the 3x6 array of zeros
print('\n3x6 Array of Zeros:\n', zeros_2d_array)

# 3. Create a 3D array using np.empty (may contain uninitialized values)
empty_array = np.empty((2, 3, 2))
# Display the uninitialized 3D array
print('\n3D Array Created with np.empty:\n', empty_array)

# 4. Create an array using np.arange, which is similar to Python's range but returns an ndarray
arange_array = np.arange(15)
# Display the array created with np.arange
print('\nArray Created with np.arange:', arange_array)


# ### Summary of array creation functions:
# * `np.array`: Convert input data to an ndarray, inferring the dtype or specifying it explicitly.
# * `np.asarray`: Convert input to ndarray without copying if it's already an ndarray.
# * `np.arange`: Return an ndarray with values within a specified range.
# * `np.ones`, `np.ones_like`: Create arrays filled with 1s.
# * `np.zeros`, `np.zeros_like`: Create arrays filled with 0s.
# * `np.empty`, `np.empty_like`: Create new arrays without initializing their values.
# * `np.full`, `np.full_like`: Create arrays with all elements set to a specified fill value.
# * `np.eye`, `np.identity`: Create an identity matrix with 1s on the diagonal.

# ### **Data Types for ndarrays**

# In NumPy, the data type (`dtype`) is essential for interpreting a chunk of memory as a specific type of data. Here's how you can create arrays with specific data types:

# In[28]:


import numpy as np

arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)

print(arr1.dtype)  
print(arr2.dtype)  


# NumPy's flexibility with data types makes it easy to interact with data from other systems. The numerical data types (`dtypes`) are named with a type name followed by the number of bits per element, such as `float64` for a double-precision floating-point value, which uses 64 bits.

# **Key NumPy Data Types:**
# 
# - `int8`, `uint8`: Signed and unsigned 8-bit integers
# - `int16`, `uint16`: Signed and unsigned 16-bit integers
# - `int32`, `uint32`: Signed and unsigned 32-bit integers
# - `int64`, `uint64`: Signed and unsigned 64-bit integers
# - `float16`: Half-precision floating-point
# - `float32`: Single-precision floating-point
# - `float64`: Double-precision floating-point
# - `bool`: Boolean type
# - `object`: Python object type

# You can convert an array's `dtype` using the `astype` method:

# In[29]:


arr = np.array([1, 2, 3, 4, 5])
float_arr = arr.astype(np.float64)

print(float_arr.dtype) 


# Casting a floating-point array to an integer will truncate the decimal part:

# In[30]:


arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
int_arr = arr.astype(np.int32)

print(int_arr) 


# For string arrays representing numbers, `astype` can convert them to numeric form:

# In[31]:


numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_arr = numeric_strings.astype(float)

print(numeric_arr) 


# ### **Arithmetic with NumPy Arrays**
# 
# Arrays in NumPy allow you to perform batch operations without loops, known as vectorization:

# In[32]:


arr = np.array([[1., 2., 3.], [4., 5., 6.]])
result = arr * arr  # Element-wise multiplication

print(result)


# Scalar operations propagate the scalar across the array:

# In[33]:


scalar_result = 1 / arr

print(scalar_result)


# ### **Basic Indexing and Slicing**
# 
# Indexing and slicing in NumPy arrays are powerful features. For one-dimensional arrays:

# In[34]:


arr = np.arange(10)

print(arr[5]) 
print(arr[5:8]) 


# Slicing two-dimensional arrays selects a range along an axis:

# In[35]:


arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
slice_result = arr2d[:2, 1:]  # Selects first two rows, columns 1 and 2

print(slice_result)


# ### **Boolean Indexing**
# 
# You can use boolean indexing to select elements based on conditions:

# In[36]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)

bob_data = data[names == 'Bob']

print(bob_data)


# Negating a condition with `~` selects all rows except those where the condition is true:

# In[37]:


not_bob_data = data[~(names == 'Bob')]

print(not_bob_data)


# You can also combine multiple boolean conditions using `&` (and) and `|` (or).
