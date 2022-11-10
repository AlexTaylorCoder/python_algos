from collections import deque
def stoneGame(piles) -> bool:  
    #Compare difference between first two ele and last ele,
    #Whichever has the greatest difference take (first-second)
    piles_queue = deque(piles)
    sumFirst = 0
    sumSecond = 0
    turn = 0
    while len(piles_queue) > 0:
        print("ran")
        front_diff = piles[0] - piles[1]
        back_diff = piles[-1] - piles[-2]
        if front_diff > back_diff:
            val = piles_queue.popleft()
            if turn % 2 == 0:
                sumFirst += val
            else:
                sumSecond += val
        elif front_diff < back_diff:
            val = piles_queue.pop()
            if turn % 2 == 0:
                sumFirst += val
            else:
                sumSecond += val
        else:
            if turn % 2 == 0:
                if piles[0] > piles[-1]:
                    val = piles_queue.popleft()
                    sumFirst += val
                else:
                    val = piles_queue.pop()
                    sumFirst += val
            else:
                if piles[0] > piles[-1]:
                    val = piles_queue.popleft()
                    sumSecond += val
                else:
                    val = piles_queue.pop()
                    sumSecond += val
        turn += 1
    return sumFirst > sumSecond

print(stoneGame([8,9,7,6,7,6]))
    