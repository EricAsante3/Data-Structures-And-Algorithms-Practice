#sorted list
SortedList = [1,2,3,4,5,6,7,8,9,10]



def binarysearch(arr, searching_value):
    low = 0
    high = len(arr) - 1

    while low <= high:

        middle =  low + (high - low) // 2


        if arr[middle] == searching_value:
            return middle

        elif arr[middle] < searching_value:
            low = middle + 1
        
        else:
            high = middle - 1

    return None


print(binarysearch(SortedList, 11))