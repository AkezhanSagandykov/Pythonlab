numheads = 35
numlegs = 94
def solve(numheads, numlegs):
    '''x - количество куриц
    y - количество кроликов
    x + y = 35
    2x + 4y = 94'''
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    print (x, y)
solve(numheads, numlegs)