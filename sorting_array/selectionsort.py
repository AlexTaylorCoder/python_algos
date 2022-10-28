# Similar to insertion sort in that first element of array is by default min, and sorted on left 
# Difference is that min is compare to every other item in list and swapped with lwoer value
# Repeatedly find min element and place at beggining


def selection_sort(a):
    for i in range(1, len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        if min != i:
            a[i], a[min] = a[min], a[i]
        
        
    return a
print(selection_sort([1,5,234,53,436,3,235,4453,1,3,4,6,13,4]))