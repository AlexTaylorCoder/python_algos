

def all_construct(target,a):
    table = [[]] * (len(target)+1)
    table[0] = [[]]
    for i in range(len(target)+1):
        
        for word in a:
            #initial first ele which represents a to...
            if target[i:i+len(word)] == word:
                updatedCurrent = list(map(lambda x: x + [word],table[i]))
                table[i+len(word)] = table[i+len(word)] + updatedCurrent
            # elif table[i:i+len(word)] == word:
            #     table[i+len(word)] = table[i] + [word]
    return table[-1]


print(all_construct("purple",["le","purp","l","e"]))
# print(all_construct("banana",["b","awf"]))
# print(all_construct("banana",["b","an","a"]))
# print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","ee","eeee","eeeeeeee","eeeeeeeeeeee","eeeeeeeeeeeeeeee"]))
