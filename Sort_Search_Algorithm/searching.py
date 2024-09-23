
class SearchAlgo(object):
    def __init__(self):
        pass
    def linearSearch(self, arr, n, target):
        for i in range(n):
            if arr[i] == target:
                return i
        return -1
    def binarySearch(self, arr, target, low, high):
        if high >= low:
            mid = (low + high) //2 #int(low + (high - low)//2)
            x = arr[mid]
            if x == target:
                return mid
            elif x > target:
                return SearchAlgo.binarySearch(self, arr, target, low, mid-1)
            else:
                return SearchAlgo.binarySearch(self,arr, target, mid+1, high)
        else:
            return -1



def main():
    s = SearchAlgo()
    data = [3, 4, 9, 0, 5, 2, 7, 8]
    arr = [1,2,3,4,5,6,7,8]
    n = len(data)
    x = 4
    l_data = s.linearSearch(data, n, x)
    print(l_data)
    data = data.sort()
    print(data)
    b_data = s.binarySearch(arr, x, 0, 8)
    print(b_data)

if __name__=='__main__':
    main()