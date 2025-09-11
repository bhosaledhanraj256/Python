import array

arr = array.array('i', [1, 2, 3, 4, 5])
arr.append(6)
arr.insert(2, 10)
arr.remove(3)
print(arr)
