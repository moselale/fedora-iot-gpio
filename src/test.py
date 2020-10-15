import time

value = 0
i = 4

def getOpposite(val):
    if val == 0:
        return 1
    else:
        return 0

while i>0:
    i = i-1
    print(i)
    print(value)
    value = getOpposite(value)
    print(value)

    time.sleep(1)

