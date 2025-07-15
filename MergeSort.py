def Merge(array, leftarray, rightarray):
    i = 0 # left index
    j = 0 # right index
    k = 0 # merged index

    while i < len(leftarray) and j < len(rightarray):
        if leftarray[i] < rightarray[j]:
            array[k] = leftarray[i]
            i += 1
            k += 1
        else:
            array[k] = rightarray[j]
            j += 1
            k += 1

    while i < len(leftarray):
        array[k] = leftarray[i]
        i += 1
        k += 1

    while j < len(rightarray):
        array[k] = rightarray[j]
        j += 1
        k += 1



def MergeSort(array):

    if len(array) > 1:
        leftarray = array[:len(array)//2]
        rightarray = array[len(array)//2:]


        MergeSort(leftarray)
        MergeSort(rightarray)
    
        Merge(array, leftarray, rightarray)



list = [7,4,2,78,9,4,2,67,8,2]
MergeSort(list)
print(list)