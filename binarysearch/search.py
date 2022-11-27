from util import time_it

@time_it
def search(sequence, item):
    start_index = 0
    end_index = len(sequence) - 1

    while start_index <= end_index:
        midpoint = start_index + (end_index - start_index) // 2
        midpoint_value = sequence[midpoint]

        if midpoint_value == item:
            return midpoint

        elif item <= midpoint_value:
            end_index = midpoint - 1

        else:
            start_index = midpoint + 1

    return None
sequence_b = [i for i in range(1000001)]
item_b = 1000000

print(search(sequence_b, item_b))

# using linear search

# @time_it
# def linear_search(numbers, number_to_find):
#     for index, element in enumerate(numbers):
#         if element == number_to_find:
#             return index
#     return -1
# numbers = [i for i in range(1000001)]
# number_to_find = 1000000
# print(linear_search(numbers, number_to_find))
#
