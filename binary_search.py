import math
#set value 
value = 0
#set array
array = []
def binary_search(array,value):
    start=0
    end=len(array) -1
    half=math.floor((start + end)/2)
    while(start <= end):
        if array[half] == value:
            return half
        elif array[half] < value:
            end = half -1
            half=math.floor((start + end)/2)
        else:
            start= half + 1
            half=math.floor((start + end)/2)