
def moveAllZeroToleft(arr, n):
    #count = 0
    list1 = []
    for i in range(n):
        if arr[i] == 0:
            list1.append(0)
            #count += 1

    for i in range(n):
        if arr[i] != 0:
            list1.append(arr[i])
            #count += 1
    return list1


arr2 = [-1, 0, 0, -2, 9]
arr1 = [1, 10, 20, 0, 59, 63, 0, 88, 0]
arr = [1, 2, 0, 0, 0, 6, 0, 3, 4, 5, 0, 0, 0]
n = len(arr2)
#print(moveAllZeroToleft(arr2, n))

def moveZeroLeft(arr, n):
    index_write, newlist = n, [0] * n


    for index_read in range(n -1, -1, -1):
        if arr[index_read -1] != 0:
            newlist[index_write -1] = arr[index_read -1]
            index_write -= 1
    return newlist

arr2 = [-1, 0, 0, -2, 9]
arr1 = [1, 10, 20, 0, 59, 63, 0, 88, 0]
arr = [1, 2, 0, 0, 0, 6, 0, 3, 4, 5, 0, 0, 0]
n = len(arr2)
print(moveZeroLeft(arr2, n))

listz = [ x for x in range(len(arr2) -1, -1, -1)]
print(listz)

def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0])
    result = [intervals[0]]
    for interval in intervals:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result


intervals = [[6, 10], [11, 15], [2, 5], [1, 4], [7, 9]]

#print(merge(intervals))
listIn = [[6, 10], [11, 15], [2, 5], [1, 4], [7, 9]]



set1 = [0, 1, 2, 3]

from itertools import chain, combinations
def powerset(iterable):
    s= list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) +1))

print(list(powerset(set1)))
def subset(s):
    if len(s) == 0:
        return [[]]
    x = subset(s[:-1])
    return x+[[s[-1]] + y for y in x]
#print(subset(set1))




