# Challenge - no nested for loop, accomplish with a pointer in one loop

def picker(prices):
    # Input - prices - list of numbers
    buy = 0 # pointer for the buy date
    indices = [0, 0] # tracker for current profit generation
    greatest = 0
    for i in range(len(prices)):
        if prices[i] < prices[buy]:
            buy = i
        elif prices[i] - prices[buy] > greatest:
            greatest = prices[i] - prices[buy]
            indices = [buy, i]

    return indices

