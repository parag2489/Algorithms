class BinMinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1
    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
    def delMin(self):
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[-1]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retVal
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

class BinMaxHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1
    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
    def delMax(self):
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[-1]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retVal
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

class QuickSelect:
    def __init__(self, arr):
        self.group_size = 5
        self.pos_left = 0
        self.pos_right = len(arr)
    def find_median(self, part):
        part = sorted(part)
        return part[(len(part) / 2)]  # + (len(part) % 2) - 1]
    def partition(self, arr, l, r, med):
        # find med in arr and move it to the end
        j = l
        pos = arr.index(med)
        arr[pos], arr[r-1] = arr[r-1], arr[pos]
        for i in range(l, r-1):
            if arr[i] <= med:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1
        arr[j], arr[r-1] = arr[r-1], arr[j]
        return j
    def kth_smallest(self, arr, l, r, k):
        medians = []
        for i in range(l, r, self.group_size):
            last_index = min(r, i + self.group_size)
            if len(arr[i:last_index]) > 1:
                medians.append(self.find_median(arr[i:last_index]))
            else:
                medians.append(arr[l])
        median_of_medians = self.find_median(medians)
        pos = self.partition(arr, l, r, median_of_medians)
        if pos - l == k-1:
            return arr[pos]
        elif pos-l > k-1:
            return self.kth_smallest(arr, l, pos, k)
        return self.kth_smallest(arr, pos + 1, r, k - pos + l - 1)


import numpy as np
import pdb
np.random.seed(20000)

for i in range(1000):
    arr = list(np.random.randint(-1000, 1000, (10000,)))
    k = np.random.randint(1, len(arr), (1,))[0]

    # using min-heap : O(n + k log(n))
    bh = BinMinHeap()
    bh.buildHeap(arr)
    for _ in range(k-1):
        elm = bh.delMin()
    kth_small1 = bh.heapList[1]

    # using max-heap : O(k + (n-k) log(k))
    bh = BinMaxHeap()
    bh.buildHeap(arr[:k])

    for j in range(k, len(arr)):
        if arr[j] < bh.heapList[1]:
            bh.heapList[1] = arr[j]
            bh.percDown(1)
    kth_small2 = bh.heapList[1]#

    # using median of medians : O(n)
    qs = QuickSelect(arr)
    kth_small3 = qs.kth_smallest(arr, 0, len(arr), k)
    kth_small4 = sorted(arr)[k-1]
    if not (kth_small1 == kth_small2 and kth_small2 == kth_small3 and kth_small3 == kth_small4):
        print "Stop", " -- ", "i = ", i
        pdb.set_trace()
    if i % 100 == 0:
        print i