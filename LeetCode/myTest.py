
numtest = [-1,0,1,2,-1,-4, 2]
numToIndex = {}
for i, num in enumerate(numtest):
    #print(f'{i} --->{num}')
    numToIndex[num] = i
    print(f'{numToIndex} ')



def threesum(num: list[int]) ->list[int]:
    num.sort()
    print(num)
    n = len(num)
    triplets = []

    for i in range(n):
        print(i, num[i], num[i - 1])
        if i > 0 and num[i] == num[i -1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            if num[i] + num[j] + num[k] == 0:
                triplets.append([num[i], num[j], num[k]])
                j+=1
                while j < k and num[j] == num[j -1]:
                    j+=1
            elif num[i] + num[j] + num[k] < 0:
                j+=1
            else:
                k -=1
    return triplets


#print(threesum(numtest))
def find3Sum(nums, arr_size, target):
    for i in range(0, arr_size - 1):
        s = set()
        curr_sum = target - nums[i]
        for j in range(i+1, arr_size):
            if curr_sum - nums[j] in s:
                print('Triplet is ', nums[i], nums[j], curr_sum - nums[j])
                return True
            s.add(nums[j])
    return False

find3Sum(numtest, 7, 0)
#def twosum(self, nums: list[int], target: int) -> list[int]:
def twosum(nums, target):
    numToIndex = {}
    for i, num in enumerate(nums):
        if target - num in numToIndex:
            return numToIndex[target - num], i
        else:
            numToIndex[num] = i