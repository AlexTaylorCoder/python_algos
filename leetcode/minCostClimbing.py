#Tabulation>

def minCost(cost):
        count = 0
        i = 0
        if cost[]
        while i <= len(cost)-1:
            count += cost[i]
            if cost[i] >= cost[i+1]:
                i += 2
            else:
                i += 1
        return count

cost = [1,100,1,1,1,100,1,1,100,1]
print(minCost(cost))