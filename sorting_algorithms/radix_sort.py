# author: alex o

def counting_sort_int(array, base, col):
    # initialise count array
    count_array = [0]*base

    # get the digit in position column and add them into "buckets"
    for elem in array:
        digit = elem // 10 ** (col)
        count_array[digit % base] += 1

    # initialise position array
    position = [0]*base

    position[0] = 1
    for i in range(1, base):
        position[i] = position[i - 1] + count_array[i - 1]

    # initialise output array
    output = [0]*len(array)

    # put back elements from initial array into output array
    for elem in array:
        output[position[elem // 10 ** (col) % base] - 1] = elem
        position[elem // 10 ** (col) % base] += 1 

    return output

def radix_sort(arr):
    # O(MN), M = number of digits, N = counting sort 

    # gets the maximum length of digits
    m = max(arr)
    for i in range(len(str(m))):
        arr = counting_sort_int(arr, 10, i)
    
    yield arr
    return arr
