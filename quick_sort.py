#pivot
#array
#recursive

    
#left of pivot is smaller
#right of pivot is bigger

def quick_sort(array):
    length = len(array)
    if length <= 1:
        return array
    
    pivot = array.pop()

    less= []
    more = []

    
    
    for item in array:
        if item> pivot:
            more.append(item)
        else:
            less.append(item)

    return quick_sort(less) + [pivot] + quick_sort(more)
        
print(quick_sort([0,9,3,8,2,7,5]))


