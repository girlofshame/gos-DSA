import math
def merge_sort(array):
    length = len(array)
    if length <= 1:
        return array
    
    mid = math.floor(length/2)
    left=merge_sort(array[0:mid])
    right = merge_sort(array[mid:])

    output = []
    i=0
    j=0

    while i< len(left) and j< len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i+=1
        else:
             output.append(right[j])
             j+=1
    
    #any leftovers if one list shorter than the other
    output.extend(left[i:])
    output.extend(right[j:])
    return output


    