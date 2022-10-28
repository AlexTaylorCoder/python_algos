# Choose pivot
# Compare list values to pivot if greater add right left is smaller add left list

#Change pivot
#Seems like recursive solution is optimal

def quicksort(a):
        print(a)
        length = len(a)        
        if length <= 1:
            return a
        pivot = a.pop()
        items_greater = []
        items_lesser = []
        for n in range(len(a)):
            #Add to right
            if a[n] > pivot:
                items_greater.append(a[n])
            #Add to left
            else:
                items_lesser.append(a[n])

        return quicksort(items_lesser) + [pivot] + quicksort(items_greater)
        




print(quicksort([1,5,234,53,436,3,235,4453,1,3,4,6,13,4]))