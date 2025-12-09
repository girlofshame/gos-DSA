array = [100,1,2,3,4,5,6]
def bubble_sort(array):
    j = len(array)
    while(j >= 1):
        for i in range (1,j):
            temp = None
            if array[i] < array[i-1]:
                #swap elements
                temp = array[i-1]
                array[i-1] = array[i]
                array[i] = temp
        j-=1
    return array    
print(bubble_sort(array))