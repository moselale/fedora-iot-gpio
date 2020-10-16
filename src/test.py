import time

i = 4

def getOpposite(val):
    if val == 0:
        return 1
    else:
        return 0

while i<8:
    i = i+1
    strin = 'strin + ' + str(i)
    print(strin)
    time.sleep(1)

