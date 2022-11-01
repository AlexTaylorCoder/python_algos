

#Return values should be true or false
def count_construct(target,a):
    table = [0] * (len(target)+1)
    table[0] = 1
    for i in range(len(target)+1):
        #Shift target pointer to right
        #"abcde" --> "bcde" 
        for j in a:
            try:
                #Starting at position i
                #Check prefixes matches
                target_index = target[i:i+len(j)]
                if target_index == j:
                    table[i+len(j)] += table[i]
            except:
                pass
    return table[-1]

print(count_construct("purple",["le","purp"]))
print(count_construct("banana",["b","awf"]))
print(count_construct("banana",["b","an","a"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","ee","eeee","eeeeeeee","eeeeeeeeeeee","eeeeeeeeeeeeeeee"]))