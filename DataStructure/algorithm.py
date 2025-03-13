import time
from collections import Counter
import sys

class MostFrequent:
    def __init__(self, List):
         self.List = List
    def nativeApproach(self):
         return max(set(self.List), key = self.List.count)
    def max_occurance(self):
         result = []
         for i in self.List:
             result.append(self.List.count(i))
         return result
    def Collection_Counter(self):
         itemList = Counter(self.List)
         print(itemList)
         return sorted(itemList.values())
    def dictFreq(self) -> dict:
        freq = {}
        for item in self.List:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        return freq

'''
  Dynamic Programming (DP)  
  1. Memomrization- Top-Down
  2. Tabulation - Bottom-up 

'''
class DyanmicProgramming:
    def __init__(self):
        pass
    def fib(self, n):
        if n < 2:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)
      
    #Memorization technique of Dymanic programming

    def dyna_fib(self, n, lookup = {}):
        if n <= 2:
            return 1
        elif n in lookup:
            return lookup[n]
        else:
            lookup[n] = self.dyna_fib(n-1, lookup) + self.dyna_fib(n-2, lookup)
            return lookup[n]

    def tabulization_fib(self, n):
        fin_1, fin_2 = 0, 1
        for i in range(2, n + 1):
            fin = fin_1 + fin_2
            fin_1, fin_2 = fin_2, fin
            #print("{0} === {1}".format(i -1, fin))

        return fin
    def tabulizationFib(self, n):
        #Create an array of size (n+1) to store the computed values
        fib_table = [0, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            #Compute the ith fibonacci number
            fib_table[i] = fib_table[i-1] + fib_table[i-2]
        return fib_table[n]

    def countRecurent(self, coins, n, sum):
        if sum == 0:
            return 1
        elif sum < 0 or n == 0:
            return 0
        else:
            return self.countRecurent(coins, n, sum - coins[n - 1]) + self.countRecurent(coins, n - 1, sum)
    
    #coins change problems
    '''
        In this approach, we can use recursion to solve this as we have to iterate over all the possible combinations 
        of coins that equal the given sum every time update the minimum no of coins needed to create this sum.
    
        
    def coinChange(self, S, sum):
        coins = sys.maxsize
        if sum == 0:
            return 0
        if sum < 0:
            return coins
        for c in S:
            result = self.coinChange(S, sum - c)
            if result != coins:
                coins = min(coins, result + 1)
        return coins
    '''
    def coinChangeGA(self, D, sum):
        D.sort(reverse=True)
        l =[]
        for i in range(len(D)):
            while sum > D[i]:
                l.append(D[i])
                sum -= D[i]
            if sum == 0:
                break
        
        return l    
'''
The algorithm finds the maximum number of activities that can be done in a given time without them overlapping.
'''
class GreedyAlgorithms:
    def __init__(slef):
        pass
    def Activity(self):
        data = {
            'start_time' : [2, 6, 4, 10, 13, 7],
            'finish_time' : [5, 10, 8, 12, 14, 15],
            'activity' : ["Homework" , "Presentation" , "Term paper" , "Volleyball practice" , "Biology lecture" , "Hangout"]
        }
        print('Start Time ', data['start_time'])
        print('Finished Time ', data['finish_time'])
        print('Activity ', data['activity'] )
        selected_activity = []
        start_position = 0
        term = 0
        for i in range(len(data['finish_time'])):
            for j in range(len(data['finish_time'])):
                if data['finish_time'][i] < data['finish_time'][j]:
                    term = data['activity'][i], data['finish_time'][i], data['start_time'][i]
                    data['activity'][i] , data['finish_time'][i] , data['start_time'][i] = data['activity'][j] , data['finish_time'][j] , data['start_time'][j]
                    data['activity'][j] , data['finish_time'][j] , data['start_time'][j] = term
        print("After soring based on start time \n")
        print('Start Time ', data['start_time'])
        print('Finished Time ', data['finish_time'])
        print('Activity ', data['activity'] )

        selected_activity.append(data['activity'][start_position])
        for pos in range(len(data['finish_time'])):
            if data['start_time'][pos] >= data['finish_time'][start_position]:
                selected_activity.append(data['activity'][pos])
                start_position = pos
        print(f"The student can work on the following activities : {selected_activity} ")

class knapsack:
    """
    1. [0/1] knapsack (at most weight)
    Given N items where each item has some weight and profit associated with it and also given a bag with capacity W, 
    [i.e., the bag can hold at most W weight in it]. The task is to put the items into the bag such that the sum of profits associated with them is the maximum possible
    
    2. Fractional knapsack (max total including fraction)
    Given the weights and profits of N items, in the form of {profit, weight} put these items in a knapsack of capacity W to get the maximum total profit in the knapsack. 
    In Fractional Knapsack, we can break items for maximizing the total value of the knapsack
    """
    def __init__(self):
        self.memo = [[-1 for i in range(1001)] for j in range(1001)]
    def FractionalKnapsack(self):
        data = {
            'weight': [10, 6, 2],
            'profit' : [40, 30, 6]        
        }
        max_weight = 17
        selected_wt = 0
        max_profit = 0
        ratio = [int(data['profit'][i] / data['weight'][i]) for i in range(len(data['profit']))]
        print(ratio)
        print(len(ratio))
        for i in range(len(ratio)):
            for j in range(i + 1, len(ratio)):
                if ratio[i] < ratio[j]:
                    ratio[i], ratio[j] = ratio[j], ratio[i]
                    data['weight'][i], data['weight'][j] = data['weight'][j], data['weight'][i]
                    data['profit'][i], data['profit'][j] = data['profit'][j], data['profit'][i]

        for i in range(len(ratio)):
            if selected_wt + data['weight'][i] <= max_weight:
                selected_wt += data['weight'][i]
                max_profit += data['profit'][i]
            else:
                frac_wt = (max_weight - selected_wt) / data['weight'][i]
                frac_val = data['profit'][i] * frac_wt
                max_profit += frac_val
                selected_wt += (max_weight - selected_wt)
        print(f"The maximum profit that can be made from each item is: {round(max_profit , 2)} dollar")

    def knapsack01(self, W, wt, val, n):
        if W == 0 or n == 0:
            return 0
        elif wt[n-1] > W:
            return self.knapsack01(W, wt, val, n - 1)
        else:
            return max(val[n - 1] + self.knapsack01(W - wt[n - 1], wt, val, n - 1), self.knapsack01(W, wt, val, n - 1))

    def knapsack011(self, W, wt, val, n):
        if self.memo[n][W] != -1:
            return self.memo[n][W]
        if W == 0 or n == 0:
            return 0
        elif wt[n-1] > W:
            self.memo[n][W] = self.knapsack011(W, wt, val, n - 1)
            return self.memo[n][W]
        else:
            self.memo[n][W] = max(val[n - 1] + self.knapsack011(W - wt[n - 1], wt, val, n - 1), self.knapsack011(W, wt, val, n - 1))     
            return self.memo[n][W]
            
    '''        
    def knapsack012(self, W, wt, val, n, mem = {}):
        if mem is not None:
            return mem[n][W]
        if W == 0 or n == 0:
            return 0
        elif wt[n-1] > W:
            mem[n][W] = self.knapsack012(W, wt, val, n - 1, mem )
            return smem[n][W]
        else:
            mem[n][W] = max(val[n - 1] + self.knapsack012(W - wt[n - 1], wt, val, n - 1, mem), self.knapsack012(W, wt, val, n - 1, mem))
            return mem[n][W]
    '''        

def fizz_buzz(num):
    ''' 
        1. Fizz - number divided by 3
        2. Buzz - number divided by 5
        3. FizzBuzz - number divided by 15
    '''
    fizzbuzz = []
    for i in range(1, num+1):
        if i % 15 == 0:
          fizzbuzz.append("FizzBuzz")
        elif i % 5 == 0:
           fizzbuzz.append("Buzz")
        elif i % 3 == 0 :
           fizzbuzz.append("Fizz")
        else:
           fizzbuzz.append(i)
           
    return fizzbuzz    

def main():
    dp = DyanmicProgramming()
    start = time.time()
    print(dp.fib(15))
    stop = time.time()
    print(stop - start)
    
    coins = [1,5,10,25]
    sum = 500
    n = len(coins)

    print(dp.countRecurent(coins, n, sum))
   
def towerOfHanoi(n, src, dest, temp):
    if n==0:
       return 
    towerOfHanoi(n-1, src, temp, dest)
    print("Mode Disc {} from rod {} to rod {}".format(n, src, dest))
    towerOfHanoi(n-1, temp, dest, src)  
   
if __name__ == "__main__":
   main()
   print(fizz_buzz(25))
   nums = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
   mf = MostFrequent(nums)
   print(mf.Collection_Counter())
   dp = DyanmicProgramming()
   print(dp.dyna_fib(50))
   print(dp.tabulization_fib(50))
   print(dp.tabulizationFib(50))
   denominationList = [1, 5, 10, 25]
   total_change = 99
   print(dp.coinChangeGA(denominationList, total_change))

   ga = GreedyAlgorithms()
   ga.Activity()

   k = knapsack()
   k.FractionalKnapsack()

   val = [20, 25, 8, 10, 5, 6, 8] #[300, 200, 400, 500]
   wt = [8, 10, 2, 4, 1, 4, 1] #[2, 1, 5, 3]
   W = 16 #10
   n = len(val)

   print(k.knapsack01(W, wt, val, n))
   print(k.knapsack011(W, wt, val, n))
   #print(k.knapsack012(W, wt, val, n))
