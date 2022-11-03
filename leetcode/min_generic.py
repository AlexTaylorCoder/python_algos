# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.


#Recursive solution seems optimal

#How many steps to get to closest value of bank
def min_mutation(start,end,bank):
    count = 0
    contains_prev = -1
    for i in range(len(start)+1):
        contains_index = bank_contains(start[:i],bank)
        if contains_index == -1:
            count += 1
            start = start[:i-1] + bank[contains_prev][i-1:i] + start[i:]
        contains_prev = contains_index
    return count 


def bank_contains(substring,bank):
    for i, s in enumerate(bank):
        if substring in s:
            return i
    return -1

#
def check_count(start,end,bank):
    for i in range(len(bank)):
        print(min_mutation(start,bank[i],bank))

#Maybe find differing chars?
print(check_count(start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]))
print(check_count(start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(check_count(start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))

#  shortest = 0
#     for i in range(len(bank)):
#         path_count = check_path(start,bank[i],bank)
#         if path_count != 0:
#             shortest = path_count
#     return shortest