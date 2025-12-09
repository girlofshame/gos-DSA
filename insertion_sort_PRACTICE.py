#array
#sort
#comparing every value to all elements to the left of it and inserting it in the right place
temp = None
array = [0,-4,2,3,1,67,7,0]
print("print check \n\n\n")

def insertion_sort_clean(array):
    for i in range(1, len(array)):
        temp = array[i]
        if(temp > array[i-1]):
            continue
        j = i
        while (j> 0 and temp < array[j-1] ):
            array[j] = array[j-1] #move comparative one right 
            j-=1
        array[j] = temp
        print(f"{array}\n\n\n")
    return array




def insertion_sort_verbose(array):
    for i in range(1, len(array)):
        temp = array[i]
        print("temp is", temp)
        print(f"array is {array}")
        if(temp > array[i-1]):
            print(f"{temp} > {array[i-1]}")
            print("no need to swap, keep looking\n\n\n")
            continue
        j = i
        while (j> 0 and temp < array[j-1] ):
            print(f"{temp} is < {array[j-1]}")
            array[j] = array[j-1] #move comparative one right 
            print(f"{array[j-1]} moved right")
            print(array)
            j-=1
        if(j-1 <= 0):
            print("reached end of array")
        else:
            print(f"temp ({temp}) >= {array[j-2]}, so replace temp in array")
        print("putting temp in correct place")
        array[j] = temp
        print(f"{array}\n\n\n")

    print("your sorted array is")         
    return array


print(insertion_sort_verbose(array))