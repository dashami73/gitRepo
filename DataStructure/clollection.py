'''

from collections import Counter
import heapq
#count frequency in list using for loop
a ="aabbbcaabaabccdddedfffddffd"
dict1 = {}
for item in a:
    if item in dict1:
        dict1[item] += 1
    else:
        dict1[item] = 1
print(f"The frequency of each elsemt:  {dict1} ")
List_count = Counter(a)
oDict = {}
for k, v in List_count.items():
    print(k , ":" , v)
    oDict[k] = v
print(List_count)
print(oDict)
print(List_count.most_common(1))

A1 = [70, 90, 110, 110, 80, 60, 100, 40, 20]

print(heapq.nlargest(2, A1))
for i in range(len(A1)):
    print(A1.index(heapq.nlargest(i+1, A1)[i]))
print(heapq.nsmallest(1, A1))

'''
import sys
import itertools
def findsubset(s, n):
    #return set(itertools.combinations(s, n))
    return list(map(set, itertools.combinations(s,n)))
str = {0,1,2,3,4}
for i in range(len(str) + 1):
    print(findsubset(str, i))

INT_MIN= ( -sys.maxsize -1)
INT_MAX = sys.maxsize

#Sliding Window: Array, String, SubArraay, SubString, Largest Sum, Maximum Sum, Minumum Sum
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sliding_window(elem, winSize):
    if len(elem) <= winSize:
        return elem
    for i in range(len(elem) - winSize + 1):
        #return elem[i : i + winSize]
        print(elem[i : i + winSize])


sliding_window(lis, 5)
def maxSum(arr, n, k):
    max_sum  = INT_MIN
    for i in range( n - k +1):
        curr_sum = 0
        for j in range(k):
            curr_sum = curr_sum + arr[i + j]
        max_sum = max(max_sum, curr_sum)
    return max_sum

def maxSum_sliding_win(arr, n, k):
    max_sum = INT_MIN
    if n <= k:
        return -1
    win_sum = sum(arr[:k])
    for i in range(n-k):
        win_sum = win_sum -arr[i] + arr[i + k]
        max_sum = max(win_sum, max_sum)
    return max_sum
print(maxSum(lis, len(lis), 5))

# Q: Find a non-empty subarray with the largest summ

def bruteForce(nums):
    LargestSum = nums[0]
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            LargestSum = max(LargestSum, curr_sum)
            #print(LargestSum)
    return LargestSum
def kadances(nums):
    max_sum = nums[0]
    cur_sum = 0
    for n in nums:
        cur_sum = max(cur_sum, 0)
        cur_sum += n
        max_sum = max(max_sum, cur_sum)
    return max_sum
def slideWinLargestSum(nums):
    max_sum = nums[0]
    curr_sum = 0
    l, maxL, maxR = 0, 0, 0

    for r in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
            l = r
        curr_sum += nums[r]
        if curr_sum > max_sum:
            curr_sum = max_sum
            maxL, maxR = l, r
    return [maxL, maxR]
# Given an array of N elements, what is the smallest subarray size that the sum of its elements is greater than or equal to a constant S
def minSubarrayCount(arr, s):
    minCount = INT_MAX
    n = len(arr)
    for i in range(n -1):
        sum = 0
        count = 0
        for j in range(i, n):
            sum += arr[j]
            count += 1
            if sum >= s:
                break
        minCount = min(count, minCount)
    return minCount
def minSubarrayCount_slidingWindow(arr, s):
    minCount = INT_MAX
    n = len(arr)
    l, sum = 0, 0
    for r in range(n):
        sum += arr[r]
        while sum >= s:
            minCount = min(minCount, r -l +1)
            sum += arr[l]
            l += 1
    return minCount



n = [4, -1, 2, -7, 3, 4]
arr = [5, 1, 3, 5, 10, 7, 4, 9, 2, 1]
s = 15
lisLarg = [1, 2, 3, -19, 4, 5, 0,  6, 7, 8, 9]

#print(f'largest sum {bruteForce(lisLarg)}')
print(f'largest sum {bruteForce(n)}')
print(slideWinLargestSum(n))
print(minSubarrayCount(arr, s))
