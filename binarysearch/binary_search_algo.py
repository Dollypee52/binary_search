from util import time_it
def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1


    return None
sequence_a = [2,4,5,6,7,8,9,10,11,12,13]
item_a = 3

print(binary_search(sequence_a, item_a))

# binary search complexity
# n=len(seq), k= # steps
# n//2^k
# overall complexity is k = log2 n, the algorithm performs quickly

def binary_search(numbers, number_to_find):
    start_index= 0
    end_index = len(numbers) -1
    mid_index = 0

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_number = numbers[mid_index]

        if mid_number == number_to_find:
            return mid_index
        elif mid_number <= number_to_find:
            start_index = mid_index + 1

        else:
            end_index = mid_index - 1
    return -1
numbers = [1,2,3,4,5,6,7,8,9,10,11]
number_to_find = 9

print(binary_search(numbers, number_to_find))

def binary_search_recursive(numbers, number_to_find, start_index, end_index):
    if end_index < start_index:
        return -1
    mid_index = (start_index + end_index) // 2
    mid_number = numbers[mid_index]

    if mid_number == number_to_find:
        return mid_index
    elif mid_number <= number_to_find:
        start_index = mid_index + 1
    else:
        end_index = mid_index - 1

    return binary_search_recursive(numbers, number_to_find, start_index, end_index)
numbers = [12,15,16,17,18,19,20,23,24,26,28]
number_to_find = 17

index = binary_search_recursive(numbers, number_to_find, 0, len(numbers))
print(binary_search_recursive(numbers,number_to_find,start_index=0,end_index=11))