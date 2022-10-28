
def insertion_sort(a):
   #Move sorted elemnts to left
    range_num = range(1,len(a))
    for i in range_num:
        while a[i] < a[i-1]:
            print(i)
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1
    return a



print(insertion_sort([1,5,234,53,436,3,235,4453,1,3,4,6,13,4]))