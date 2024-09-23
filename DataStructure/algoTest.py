import sys
INT_MIN =(-sys.maxsize -1)
INT_MAX =(sys.maxsize)
print(INT_MIN, INT_MAX)
def getMaxSum(arr, k):
    maxSum, windowSum, start = INT_MIN, 0, 0
    for i in range(len(arr)):
        windowSum += arr[i]
        if (i - start + 1) == k:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1

    return maxSum
    '''
    Maximun Average subarray
    You are given an integer array of nums consisting of n elements, and an integer k.
    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10–5 will be accepted.
    '''
def findMaxAve(arr, k):
    max_sum, window_sum, n = INT_MIN, 0, len(arr)
    if(k > n):
        print('Invalid ...')
        return -1
    max_sum = window_sum = sum(arr[:k])
    for i in range(n-k):
        window_sum = window_sum + arr[i+k] - arr[i]
        max_sum = max(window_sum, max_sum)
    return max_sum/k

def AvgMAx():
    nums, k = [1, 12, -5, -6, 50, 3], 4
    print('%.2f'%(findMaxAve(nums, k)))

def sum_max(ArgList, n, k):
    answer = 0
    sum = 0
    R =1
    for L in range(1, n):
        if L > 1:
            sum = sum - ArgList[L-1]
        while (R <= n) and (sum + ArgList[R] <= k):
            sum = sum + ArgList[R]
            R += 1
        answer = max(answer, R - L)
    return answer

def windowList(ArgList, k):
    windowSum =0
    n = len(ArgList)
    print(n)
    listSubArr = []
    if n<k:
        print("invalid")
        return -1

    for i in range(k):
        windowSum += ArgList[i]
        listSubArr.append(ArgList[i])
    print(listSubArr)
    for i in range(n-k):
        listSubArr.append(ArgList[k + i])
        listSubArr.remove(listSubArr[0])
        print(listSubArr)
    return listSubArr

def numOfSubArr(arr, k, threshold):
    sum_num = INT_MIN
    window_sum =0
    n = len(arr)
    sublist = []
    sumList = []
    cout = 0
    totalSubList = []
    if k > n:
        print("invalid")
        return -1
    for i in range(k):
        window_sum+=arr[i]
        sublist.append(arr[i])
    sum_num = window_sum
    #sumList.append(window_sum)
    for i in range(n - k):

        if(window_sum/k >= threshold):
            #print(window_sum/k)
            sumList.append(window_sum)
            totalSubList.append(sublist)
            print(sublist)
            cout += 1
        window_sum = window_sum + arr[i+k] - arr[i]
        #sum_num = max(window_sum, sum_num)
        #print(sublist)
        sublist.append(arr[i+k])
        sublist.remove(sublist[0])
       # print(sublist)

    print(sumList)
    print(cout)
    return totalSubList
def main():
    ArgList = [1, 12, -5, -6, 50, 3, 0, 4, 2, 5, 6, 3, 8, 1]
    size = 3
    #print(getMaxSum(ArgList, size))
    #print(windowList(ArgList,size))
    #print(numOfSubArr(ArgList, 3, 4))
    AvgMAx()
if __name__ == '__main__':
    main()