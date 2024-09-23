import math


class SortAlgo(object):
    def __init__(self):
       pass
    def bubbleSort(self, arr, n):
        swapped = False
        for i in range(n):
            for j in range(n -i -1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            if swapped:
                swapped = False
            else:
                break
        return arr
    def selectionSort(self, arr, n):
        for s in range(n):
            min_indx = s
            for i in range(s+1, n):
                if arr[i] < arr[min_indx]:
                    min_indx = i
            arr[s], arr[min_indx] = arr[min_indx], arr[s]
        return arr
    def insertionSort(self, arr, n):
        for i in range(1, len(arr)):
            ele = arr[i]
            j = i-1
            while j >=0 and ele < arr[j]:
                arr[j+1] = arr[j]
                j-=i
            arr[j+1] = ele
        return arr
    #partion function
    def partition(self, arr, low, high):
        pivot = arr[high] # choose the right most elemet as pivot
        i = low -1
        # Traverse through all elements compare each element with pivot
        for j in range(low, high):
            if arr[j] <= pivot: #If element smaller than pivot is found swap it with greater element point by i
                i += 1
                #swap beteween element at i with element at j
                arr[i], arr[j] = arr[j], arr[i]
        #swap pivot element with the greater element specified by i
        arr[i+1], arr[high]=arr[high], arr[i+1]

        #return the position from where partion is done
        return i+1
    def quickSort(self, arr, low, high):

        if low < high:
            pi = SortAlgo.partition(self, arr, low, high)
            SortAlgo.quickSort(self, arr, low, pi - 1) #Recurcive call to the left of pivot
            SortAlgo.quickSort(self, arr, pi+1, high) #Recurcive call to the right of pivot
        return arr

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1 # left = 2*i + 1
        r = 2 * i + 2 # right = 2*i + 2
        #see if left child of root exists and is greater than root
        if l < n and arr[largest] < arr[l]:
            largest = l
        #see if right child of root exists and is greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            #heapfiy the root
            SortAlgo.heapify(self, arr, n, largest)
    def heapSort(self, arr, n):
        for i in range(n//2-1, -1, -1):
            SortAlgo.heapify(self, arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            SortAlgo.heapify(self,arr, i, 0)
        return arr

    def countSort(self, arr, n):
        output = [0 for i in range(n)]
        count = [0 for i in range(256)]
        ans = ["" for _ in arr]
        for i in arr:
            count[ord(i)] += 1
        for i in range(256):
            count[i] += count[i-1]
        for i in range(n):
            output[count[ord(arr[i])]-1] = arr[i]
            count[ord(arr[i])] -= 1
        for i in range(n):
            ans[i] = output[i]
        return ans
    def shellSort(self, arr, n):
        k = int(math.log2(n))
        interval = 2**k - 1
        while interval > 0:
            for i in range(interval, n):
                tmp = arr[i]
                j = i
                while j >= interval and arr[j - interval] > tmp:
                    arr[j] = arr[j - interval]
                    j -= interval
                arr[j] = tmp
            k -= 1
            interval = 2**k -1
        return arr
    def mergeSort(self, arr, n):
        if n == 1:
            return arr
        mid = (n -1) //2
        lis1 = SortAlgo.mergeSort(self, arr[:mid+1], len(arr[:mid+1]))
        lis2 = SortAlgo.mergeSort(self, arr[mid+1:], len(arr[mid+1:]))
        result = SortAlgo.merge(self, lis1, lis2)
        return result
    def merge(self, lst1, lst2):
        lst = []
        j, i = 0, 0
        while(i <= len(lst1) - 1) and ( j <= len(lst2) -1):
            if lst1[i] < lst2[j]:
                lst.append(lst1[i])
                j+=1
            else:
                lst.append(lst2[j])
                j+=1
        if i > len(lst1)-1:
            while(j<= len(lst2)-1):
                lst.append(lst2[j])
                j+=1
        else:
            while(i<=len(lst1)-1):
                lst.append(lst1[i])
                j+=1
        return lst

    '''
    def bucketSort(self, arr, n):
        a = []
        slot_num = 10
        for i in range(slot_num):
            a.append([])
        for j in arr:
            index_b = int(slot_num * j)
            a[index_b].append(j)
        for i in range(slot_num):
            a[i] = SortAlgo.insertionSort(a[i], len(a))
        k = 0
        for i in range(slot_num):
            for j in range(len(a[i])):
                arr[k] = a[i][j]
                k+=1
        return arr
    '''







def main():
    data = [2,1,10,23,5, 6,9, 4]
    n = len(data)
    s = SortAlgo()
    b_data = s.bubbleSort(data, n)
    print(b_data)
    s_data = s.selectionSort(data, n)
    print(s_data)
    i_data = s.insertionSort(data, n)
    print(i_data)
    q_data = s.quickSort(data, 0, n-1)
    print(q_data)
    h_data = s.heapSort(data, n)
    print(h_data)
    # bk_data = s.bucketSort(data, n)
    # print(bk_data)
    sh_data = s.shellSort(data, n)
    print(sh_data)

    m_data = s.mergeSort(data, n)
    print(f'merge sorting data  {m_data}')



if __name__ == "__main__":
    main()