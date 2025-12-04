my_list = [10, 20, 30, 20, 40]
print("Original list:", my_list)

print("Count of 20:", my_list.count(20))

copied_list = my_list.copy()
print("Copied list:", copied_list)

extra = [50, 60]
my_list.extend(extra)
print("List after extend:", my_list)

my_list.clear()
print("List after clear:", my_list)