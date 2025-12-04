numbers = [40, 10, 20, 50, 30]
print("Original list:", numbers)

numbers.sort()
print("List after sort():", numbers)

position = numbers.index(30)
print("Index of 30:", position)

numbers.insert(2, 25)  # insert 25 at index 2
print("List after insert(2, 25):", numbers)


numbers.append(60)
print("List after append(60):", numbers)