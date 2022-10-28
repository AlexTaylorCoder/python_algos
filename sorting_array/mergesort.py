
#Recurse continually split into two
def merge_sort(a):

    if len(a) > 1:
        mid = len(a) // 2
        merge_sort([mid:]) 
        merge_sort([mid:])
        


merge_sort([[1,5,234,53,436,3,235,4453,1,3,4,6,13,4]])