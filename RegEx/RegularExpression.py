import heapq
from collections import Counter
from functools import reduce


def comperehention():
    threeD = [[[x for x in range(5)] for _ in range(5)] for _ in range(5)]
    
    print(threeD)

def highOrderFunc():
    list1 = [1,2,3,4,5,6,7,8.9]
    func = lambda x : x**3    
    cubic = list(map(func, list1))
    print(cubic)
    
    func = lambda x : x%2 == 0
    even = list(filter(func, list1))
    print(even)
    func = lambda x, y: x + y
    sum1 = reduce(func, list1)
    print(sum1)

def frequnecy():
    dataList = [1,2,3,4,5,1,1,1,3,2,2,2,2,3,4,3,2,2,2]
    dataDic = Counter(dataList)
    print(dataDic)
    print(min(dataDic.values()))
    print(max(dataDic.values()))
    print(min(dataDic.keys()))
    print(max(dataDic.keys()))
    print(heapq.nsmallest(1,dataDic.values()))
    print(heapq.nlargest(1, dataDic.values()))
    print(heapq.nsmallest(1,dataDic.keys()))
    print(heapq.nlargest(1, dataDic.keys()))

def myHeap():
    data1 = [1,9,5,3,6,2,7,4]
    heapq.heapify(data1)
    print(data1)

    smallest = heapq.heappop(data1)
    print(smallest)
    heapq.heappush(data1, 10)
    print(data1)
    heapq.heappushpop(data1, 11)
    print(data1)
    heapq.heapreplace(data1, 1)
    print(data1)

    nsmallest = heapq.nsmallest(2, data1)
    print(nsmallest)

    nlargest  = heapq.nlargest(4, data1)
    print(nlargest)
    for i in range(len(nlargest)):
        print(nlargest[i])

def kthSmallest(vector, k):
    value =[]
    value1 = [n for row in vector for n in row]
    heapq.heapify(value1)
    ksmallestList, klargestList = heapq.nsmallest(k, value1), heapq.nlargest(k, value1)
    ksmallest, klargest = ksmallestList[-1], klargestList[-1]
    
    for row in vector:
        for ele in row:
            heapq.heappush(value, ele)
    print(value)
    kthSmallestList = heapq.nsmallest(k, value)
    print(kthSmallestList)
    return kthSmallestList[-1]

def main():  
    input = [[10, 25, 20, 40],
        [15, 45, 35, 30],
        [24, 29, 37, 48],
        [32, 33, 39, 50]]
    print(len(input))
    for i in input:
        print(i)
    one_dim = [n for row in input for n in row]
    print('--------------------------', one_dim)
    k = 7
    print(kthSmallest(input, k))    
    frequnecy()    
    highOrderFunc()  
    
if __name__ == "__main__":
    #main()
    comperehention()