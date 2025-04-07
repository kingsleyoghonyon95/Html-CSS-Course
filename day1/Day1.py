# last_name = "Igho"
# print(last_name)

# last_name = "John"
# print(last_name)

my_tuple = ('A', 2, 'B', 7, 'C', '%', 'A', 10, 'A', '&')
print(my_tuple)

first_index = my_tuple.index('A')
print(first_index)

second_index = my_tuple.index('A', first_index + 1)
print(second_index)

third_index = my_tuple.index('A', second_index + 1)
print(third_index)

new_tuple = (first_index, second_index, third_index)
print(new_tuple)

second_newtuple = (my_tuple[first_index], my_tuple[second_index], my_tuple[third_index])
print(second_newtuple)

print(f"Formatted output: {second_newtuple}")


