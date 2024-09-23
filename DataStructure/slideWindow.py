import collections
import heapq
import sys
INT_MIN = (-sys.maxsize)
INT_MAX = (sys.maxsize)
class SlidingWindow:
    def __init__(self):
        pass
    def isAnagram(self, str, wor):
        if len(str) != len(wor):
            return False
        d = [0]*26
        for c in str:
             d[ord(c) - ord('a')] = 1
        for c in wor:
             if d[ord(c) - ord('a')] ==0:
                 return False
        return True

    def sumMax(self, ArgList, k):
        n = len(ArgList)
        if n < k:
            print("Invalid ")
            return -1
        window_sum = sum(ArgList[:k])
        max_sum = window_sum
        for i in range(n - k):
            window_sum = window_sum - ArgList[i] + ArgList[i + k]
            max_sum = max(window_sum, max_sum)
        return max_sum

    def max_sum(self, ArgList, k):
        n = len(ArgList)
        max_min_list = []
        listSum = []
        subList = []
        avg = []
        if n < k:
            print('Invalid ...')
            return -1
        window_sum = 0
        for i in range(k):
            window_sum += ArgList[i]
            subList.append(ArgList[i])
        avg.append(window_sum/k)
        print(subList)
        print(window_sum)
        max_sum = window_sum
        min_sum = window_sum
        for i in range(n-k):
            window_sum = window_sum - ArgList[i] + ArgList[i + k]
            listSum.append(window_sum)
            avg.append(window_sum/k)
            subList.append(ArgList[i+k])
            subList.remove(subList[0])
            print(subList)
            max_sum = max(window_sum, max_sum)
            min_sum = min(window_sum, min_sum)
        print(listSum)
        print(avg)
        print(min(avg))
        print(max(avg))
        print(max(avg) - min(avg))
        listSum.sort()
        print(listSum)
        max_min_list.append(min_sum)
        max_min_list.append(max_sum)
        return max_min_list

def data_value():
    ArgList = [1,12,-5,-6,50,3,0, 4, 2, 5, 6, 3, 8, 1]
    size = 3
    sw = SlidingWindow()
    print(sw.max_sum(ArgList, size))
def dynamic_Sliding_window(arr, target):
    min_length = INT_MIN
    start, end, current_sum = 0, 0, 0
    while end < len(arr):
        current_sum = current_sum + arr[end]
        end += 1
        while start < end and current_sum >= target:
            current_sum = current_sum - arr[start]
            start += 1
            min_length = min(min_length, end - start + 1)
    return min_length

#Maximum Subarray sum
def findMaxsubarraySum_0(arr, n):
    max_sum_subarray =INT_MIN
    for i in range(n):
        for j in range (i, n):
            sum_subarray = 0
            for k in range(i, j+1):
                sum_subarray = sum_subarray + arr[k]
                max_sum_subarray = max(max_sum_subarray, sum_subarray)

    return  max_sum_subarray
#second method to find the max subarray sum 
def findMaxsubarraySum_1(arr, n):
    max_subarray_sum = INT_MIN
    for i in range(n):
        sum_subarray = 0
        for j in range(i, n):
            sum_subarray = sum_subarray + arr[j]
            max_subarray_sum = max(max_subarray_sum, sum_subarray)
    return max_subarray_sum
#second method to find the max subarray sum -> Kadane's Algorithm
def findMaxsubarraySum_2(A, n):
    local_max = 0
    global_max = INT_MIN        

    for i in range(n):
        local_max = max(A[i], A[i] + local_max)
        if local_max > global_max:
            global_max = local_max
    return global_max
def findMaxsubarraySum():
    A = [5, 7, 6, 10, 3]
    A1 = [-4, 5, 7, -6, 10, -15, 3]
    n = len(A1)
    maxSum_0 = findMaxsubarraySum_0(A1, n)
    maxSum_1 = findMaxsubarraySum_1(A1, n)
    maxSum_2 = findMaxsubarraySum_2(A1, n)
    print(maxSum_0)
    print(maxSum_1)
    print(maxSum_2)


# Find the length of the smallest contiguous subarray whose sum is greater than or equal to K
def findSmallestSubarrayWithsum(A, n, k):
    min_length = n + 1
    for i in range(n):
        curr_sum = A[i]
        if curr_sum > k:
            return 1
        for j in range(i + 1, n):
            curr_sum += A[j]
            if curr_sum > k and (j - i + 1) < min_length:
                min_length = j - i + 1
    return min_length
def minSubarrayLen(A:list[int], n:int, k:int)-> int:
    l, sum, minLen = 0, 0, n + 1
    for r in range(n):
        if sum > k:
            sum += A[r]
            while sum > k:
                minLen = min(minLen, r - l + 1)
                sum -= A[l]
                l += 1

    return minLen if minLen <= n else 0

def minSubarrayLenLessthank():
    A = [2,3,1,2,4,3]
    n = len(A)
    k=7
    A1 = [1,2,3,4,3,16,5]
    k1 = 15
    n1 = len(A1)
    minLen_1 = minSubarrayLen(A1, n1, k1)
    print(minLen_1)
def kthLanrgestElement(arr, n, k):
    x = heapq.nlargest(k, arr)
    return x[k-1]
def kthSmallestElement(arr, n, k):
    y = heapq.nsmallest(k, arr)
    return y[k-1]
def updatedList(arr, n):
    ODict = collections.OrderedDict()
    for i in range(n):
        x = kthLanrgestElement(arr, n, i+1)
        ODict[arr.index(x)] = x + i +1
    keys = list(ODict.keys())
    keys.sort()
    newList = [ODict[key] for key in keys]
    return newList

def kthlargestAndSmallestElement():
    newList = collections.OrderedDict()
    A = [2, 13, 4, 6, 3, 9, 7, 8, 1]
    A1 = [70, 90, 110, 80, 60, 100, 40, 20]
    n= len(A)
    n1 = len(A1)
    print(updatedList(A, n))
    print(updatedList(A1, n1))

    #for i in range(n):
       # print(kthSmallestElement(A, n, i + 1))
import heapq

def kth_largest():
    A= [2, 13, 4, 6, 3, 9, 7, 8, 1]
    A1 = [70, 90, 110, 80, 60, 100, 40, 20]
    n= len(A)
    n1 = len(A1)
    arr = [-e for e in A]
    print(arr)
    heapq.heapify(arr)
    print(arr)
    for i in range(5):
        heapq.heappop(arr)
    print(-heapq.heappop(arr))
def firstLast_occerance(A, n, target):
    firstLast = [-1, -1]
    for i in range(n):
        if A[i] == target:
            if firstLast[0] == -1:
                firstLast[0] = i
            firstLast[1] = i
    return firstLast


def fl_ocurance():
    A = [1, 2, 4, 5, 5, 5, 5, 5,5, 6, 6, 7, 8]
    n = len(A)
    target = 5
    print(firstLast_occerance(A, n, target))
def main():
    sw = SlidingWindow()
    findMaxsubarraySum()
    minSubarrayLenLessthank()
    kthlargestAndSmallestElement()
    fl_ocurance()
    str1 = 'gotxxotgxdogt'
    str = 'ogt'
    wor = 'got'
    print(sw.isAnagram(str, wor))
    data_value()

if __name__ =='__main__':
    main()