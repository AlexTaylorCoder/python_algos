

#Return values should be true or false
def can_construct(target,a):
    table = [0] * (len(target)+1)
    table[0] = 1
    for i in range(len(target)+1):
        #Shift target pointer to right
        #"abcde" --> "bcde" 
        if table[i]:
            for j in a:
                try:
                    #Starting at position i
                    #Check prefixes matches
                    target_index = target[i:i+len(j)]
                    print(target_index)
                    if target_index == j:
                        table[i+len(j)] = True
                except:
                    pass
    return table[-1]

print(can_construct("abcde",["ab","cde"]))