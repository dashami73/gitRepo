'''

from collections import Counter
mylist = ['a', 'a', 'b', 'c', 'c', 'c', 'c', 'd','d']
d = Counter(mylist)
print(d)

from collections import deque
import heapq
def findKthLargest(nums, k):
    heapq.heapify(nums)
    for _ in range(len(nums) -k):
        heapq.heappop(heap)
    return heapq.heappop(heap)

def smallestSubSum(arr, n, x):
    min_len = n +1
    for start in range(0, n):
        cur_sum = arr[start]
        if (cur_sum > x):
            return 1
        for end in range(start+1, n):
            cur_sum += arr[end]
            if cur_sum > x and (end - start+1) < min_len
                min_len = (end - start + 1)
    return  min_len
def toString(List):
    return ''.join(List)
def maxMinute(arr, n, k):
    ans, sum, r = 0, 0, 1
    for l in range (1, n):
        if l > 1:
            sum -=arr[l -1]
        while r <= n and sum + arr[r] <= k:
            sum += arr[r]
            r+=1
        ans = max(ans, r-l)
    return ans

def permutes(s, answer):
    if(len(s) == 0):
        print(answer, end= ' ')
        return
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i+1:]
        rest =left_substr + right_substr
        permutes(rest, answer + ch)

answer = ''
s = input('Enter the string : ')
permutes(s, answer)
def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

nums = [3, 6, 2, 8,23,12,15]
#nums = sorted(nums, reverse=False)
print(nums)
highest = max(nums)
print(highest)
res_dict = {i: nums[i] for i in range(len(nums))}
print(res_dict)
'''
import heapq as hq
def findLargestNum():
    listArr = [21, 67, 33, 13, 40, 89, 71, 19]
    n = len(listArr)
    print(hq.nlargest(8, listArr))


def rotate(M: list[list[int]]) -> None:
    n = len(M)
    depth = n // 2
    for i in range(depth):
        rlen, opp = n - 2 * i - 1, n - i - 1
        for j in range(rlen):
            temp = M[i][i + j]
            M[i][j] = M[opp - j][i]
            M[opp - j][i] = M[opp][opp - j]
            M[opp][opp - j] = M[i + j][opp]
            M[i + j][opp] = temp


def lengthOfLongestSubstring(s:str)->int:
    if not s:
        return
    start, cur_len, maxLength, sub = 0, 0, 0, {}
    for i, letter in enumerate(s):
        if letter in sub and sub[letter] >= start:
            start = sub[letter] + 1
            cur_len = i - sub[letter]
            sub[letter] = i
        else:
            sub[letter] = i
            cur_len += 1
            maxLength = max(maxLength, cur_len)

    return maxLength

findLargestNum()
s ='ABBBCDEFGXYXABEF'
maxL = lengthOfLongestSubstring(s)
print(maxL)
print(s[0:2])

matrix1 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(matrix1)
print(matrix1)