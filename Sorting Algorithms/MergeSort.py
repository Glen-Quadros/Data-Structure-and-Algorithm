def mergeSort(customList):
    if len(customList) > 1:
        left_array = customList[:len(customList)//2]
        right_array = customList[len(customList)//2:]

        mergeSort(left_array)
        mergeSort(right_array)

        # To merge
        i = 0 # Left index
        j = 0 # Right index
        k = 0 # Merged array index

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                customList[k] = left_array[i]
                i += 1
            elif left_array[i] > right_array[j]:
                customList[k] = right_array[j]
                j += 1
            k += 1
        
        while i < len(left_array):
            customList[k] = left_array[i]
            i += 1
            k += 1
        
        while j < len(right_array):
            customList = right_array[j]
            j += 1
            k += 1

customList = [9, 7, 5, 3, 1]   
mergeSort(customList)
print(customList)