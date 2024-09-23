
def KMPSearch(pat, txt):
    m = len(pat)
    n = len(txt)
    listInedx = []
    for i in range(n-m+1):
        j = 0
        while ((j < m) and pat[j] == txt[i+j]):
            j+=1
        if j == m :
            listInedx.append(i)
            #return i
        #print("Pattern found at index ", listInedx)

    return listInedx
def linearSearch(ArgList, target):
    for position, item in enumerate(ArgList):
        print(position, item)
        if item == target:
            return position
    return -1

def binarySearch(ArgList, l, r, target):
    while l <= r:
        mid = (l + (r -1))//2
        #check if target is present at mid
        if ArgList[mid] == target:
            return target
        elif ArgList[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return  -1
def binarySearch_recurcive(ArgList, l, r, target):
    if r >= l:
        mid = (l + (r -1))//2
        #check if target is present at mid
        if ArgList[mid] == target:
            return target
        elif ArgList[mid] < target:
            return binarySearch_recurcive(ArgList, l , mid -1, target)
        else:
            return binarySearch_recurcive(ArgList, mid+1, r, target)
    return  -1
import sys
INT_MIN = (-sys.maxsize -1)
INT_MAX = (sys.maxsize)
print(INT_MIN, INT_MAX)

def sum_Max(ArgList, k):
    max_sum = INT_MIN
    for i in range(n - k +1):
        curr_sum = 0
        for j in range(k):
            curr_sum = curr_sum + ArgList[i + j]
        max_sum = max(curr_sum, max_sum)
    return  max_sum
def testKMP():
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    KMP = KMPSearch(pat, txt)
    print(KMP)

def main():
    dataList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    target = 7
    k = 3
    #print(linearSearch(dataList, target))
    print(binarySearch(dataList, 0, len(dataList) -1, target))
    #print(sum_Max1(dataList, k))
    testKMP()

if __name__=='__main__':
    main()