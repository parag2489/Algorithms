def int2BinStr(num):
    if num <= 1:
        return str(num)
    else:
        return int2BinStr(num >> 1) + str(num&1)
    # return str(num) if num <= 1 else int2BinStr(num >> 1) + str(num&1)

def bitLen(num):
    count = 0
    while num != 0:
        count += 1
        num = num >> 1
    return count

def setBits(num):
    count = 0
    while num != 0:
        # count += int(num&1)
        # num = num >> 1
        num &= num - 1
        count += 1
    return count

def computeParity(num):
    parity = 0
    while num != 0:
        num &= num - 1
        parity = ~parity
    return parity

def my_lowestBitSet(num):
    pos = 0
    while num != 0:
        if (num & 1):
            return pos
        pos += 1
        num >>= 1
    return pos

def lowestBitSet(int_type):
    low = (int_type & -int_type)
    lowBit = -1
    while (low):
        low >>= 1
        lowBit += 1
    return(lowBit)

def testBit(num, offset):  # output 2 ** offset if bit at index "offset" = 1 in num
    mask = 1 << offset
    return (mask & num)

def setBit(num, offset):
    mask = 1 << offset
    return (mask | num)

def clearBit(num, offset):
    mask = ~(1 << offset)
    return num & mask

def toggleBit(num, offset):
    mask = 1 << offset
    return num ^ mask

def isPowerOfTwo(num):
    return num > 0 and num & (num-1) == 0

def isEvenBitSet(num):
    return num & 0x55555555

def isPowerOfFour(num):
    return (num > 0 and (num & (num - 1) == 0) and (num & 0x55555555) != 0)

s = int2BinStr(10)
s = bitLen(10)
s = setBits(10)
s = computeParity(10)
s = my_lowestBitSet(10)
s = isEvenBitSet(16)
s = isPowerOfFour(256)