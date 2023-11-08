"""
array.typecodes :     A string with all available type codes.
array.typecode :   The typecode character used to create the array.
array.itemsize :     The length in bytes of one array item in the internal representation.
array.append(x):  Append a new item with value x to the end of the array.
array.buffer_info() :     Return a tuple (address, length) giving the current memory address and the length in elements of the buffer used to hold array’s contents. The size of the memory buffer in bytes can be computed as array.buffer_info()[1] * array.itemsize. This is occasionally useful when working with low-level (and inherently unsafe) I/O interfaces that require memory addresses, such as certain ioctl() operations. The returned numbers are valid as long as the array exists and no length-changing operations are applied to it.
array.byteswap() :   “Byteswap” all items of the array. This is only supported for values which are 1, 2, 4, or 8 bytes in size; for other types of values, RuntimeError is raised. It is useful when reading data from a file written on a machine with a different byte order.
array.count(x) :     Return the number of occurrences of x in the array.
array.extend(iterable) :  Append items from iterable to the end of the array. If iterable is another array, it must have exactly the same type code; if not, TypeError will be raised. If iterable is not an array, it must be iterable and its elements must be the right type to be appended to the array.
array.frombytes(s) :     Appends items from the string, interpreting the string as an array of machine values (as if it had been read from a file using the fromfile() method).
array.fromfile(f, n) :   Read n items (as machine values) from the file object f and append them to the end of the array. If less than n items are available, EOFError is raised, but the items that were available are still inserted into the array. f must be a real built-in file object; something else with a read() method won’t do.
array.fromlist(list) :     Append items from the list. This is equivalent to for x in list: a.append(x) except that if there is a type error, the array is unchanged.
array.fromstring() :    Deprecated alias for frombytes().
array.fromunicode(s) :     Extends this array with data from the given unicode string. The array must be a type 'u' array; otherwise a ValueError is raised. Use array.frombytes(unicodestring.encode(enc)) to append Unicode data to an array of some other type.
array.index(x) :    Return the smallest i such that i is the index of the first occurrence of x in the array.
array.insert(i, x) :     Insert a new item with value x in the array before position i. Negative values are treated as being relative to the end of the array.
array.pop([i]) :     Removes the item with the index i from the array and returns it. The optional argument defaults to -1, so that by default the last item is removed and returned.
array.remove(x) :     Remove the first occurrence of x from the array.
array.reverse() :     Reverse the order of the items in the array.
array.tobytes() :     Convert the array to an array of machine values and return the bytes representation (the same sequence of bytes that would be written to a file by the tofile() method.)
array.tofile(f) :     Write all items (as machine values) to the file object f.
array.tolist() :     Convert the array to an ordinary list with the same items.
array.tostring() :     Deprecated alias for tobytes().
array.tounicode() :     Convert the array to a unicode string. The array must be a type 'u' array; otherwise a ValueError is raised. Use array.tobytes().decode(enc) to obtain a unicode string from an array of some other type.

"""

import array as arr
a = arr.array('d', [1.1, 3.5, 4.5])
print(a)


b = arr.array('B', [11, 12, 23, 45, 0 ] )
print(b)

c =arr.array('l')
d =arr.array('u', 'hello \u2641')
e =arr.array('l', [1, 2, 3, 4, 5])
f =arr.array('d', [1.0, 2.0, 3.14])

print( f.itemsize )
