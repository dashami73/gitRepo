
class LeeCode:
    '''
    7. Rerverse Integer
        Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    '''
    def anagramCheck(self, str1, str2):
        if (sorted(str1) == sorted(str2)):
            return True
        else:
            return False

    def reverseint(self, x):
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = int( '-' + str(x)[::-1][:-1])
        return -2**31 <= x <= 2**31 and x or 0
    '''
    9. Palindrome Numbers
        Given an integer x, return true if x is a palindrome, and false otherwise. 
    '''
    def isPalindrome(self, s):
        return s == s[::-1]

    

    '''
    1.Two Sum: 
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    '''
    def twosum(self, nums: list[int], target: int) -> list[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
            if target - num in numToIndex:
                return numToIndex[target - num] , i
            else:
                numToIndex[num]=i
    def sumTwo(self, num, target):
        for i in range(len(num)):
            for j in range(i +1, len(num)):
                if num[i] + num[j] == target:
                    return[i, j]
                else:
                    return 0
    '''
    15. 3Sum
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets        
    '''            
    def threeSum1(self, nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                sum = a+nums[l]+nums[r]
                if sum>0:    r+=1
                elif sum < 0:  l -= 1
                else: 
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[r] and l<r:
                        l+=1
        return res
    
    def threeSum(self, nums):
       nums.sort()
       result = []
       for i in range(len(nums) -2):
           if i > 0 and nums[i] == nums[i -1]:
               continue
           l = i + 1
           r = len(nums) -1
           while l < r:
               sum = nums[i] + nums[l] + nums[r]
               if sum < 0: 
                   l += 1
               elif sum > 0:
                   r -= 1
               else:
                   result.append([nums[i], nums[l], nums[r]])
                   while l <len(nums) -1 and nums[l] == nums[l+1]: l +=1
                   while r > 0 and nums[r] == nums[r -1]: r -=1
                   l +=1
                   r -=1
       return result
    def letterCombinations1(self,digits):
        if len(digits) == 0:
            return []
        letters = {  '2': 'abc',
                     '3':'def',
                     '4':'ghi',
                     '5': 'jkl',
                     '6': 'mno',
                     '7':'pqrs',
                     '8':'tuv',
                     '9':'wxyz'
                     }
        combinations = []
        '''
        def backtrack(self, index, path):
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        backtrack(0, [])
        return combinations
         '''
    def letterCombinations(self, digit):
        if not digit:
            return
        digit_map = {
                     '0': '',
                     '1': '',
                     '2': 'abc',
                     '3':'def',
                     '4':'ghi',
                     '5': 'jkl',
                     '6': 'mno',
                     '7':'pqrs',
                     '8':'tuv',
                     '9':'wxyz'
                     }
        combinations= []
        '''
        def generate_cobination(self, -combination, position):
            if position==len(digit):
                combinations.append(combination)
                return
            for ch in digit_map[digit[position]]:
                generate_cobination(combination+ch, position+1)
        generate_cobination('', 0)
        return combinations
        '''
    def rotate(self, M:list[list[int]])->None:
        n = len(M)
        depth = n//2
        for i in range(depth):
            rlen, opp = n -2 *i -1, n -i -1
            for j in range(rlen):
                temp = M[i][i+j]
                M[i][j] = M[opp -j][i]
                M[opp-j][i] = M[opp][opp -j]
                M[opp][opp-j]= M[i+j][opp]
                M[i+j][opp] = temp


    def rotateImag(self, matrix:list[list[int]]) ->None:
        l, r, = 0, len(matrix) -1
        while l < r:
            top, bottom = l, r
            for i in range(r):
                #save top left
                topleft = matrix[top][l + i];
                #move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]
                #move top right to bottom right
                matrix[bottom - i][l] = matrix[bottom][r - i]
                #move top left to top right
                matrix[bottom][r - i] = matrix[top + i][r]
                #move top left to top right
                matrix[top +i][r] = topleft
            r -= 1
            l += 1



def test():
    leecode = LeeCode() 
    s = 'malayalam'

    ans = leecode.isPalindrome(s)
    if ans:
        print('---------> Yes')
    else:
        print('----------> No')
def main():
    num_list = [6,8,2,7,11,15]
    matrix = [[1,2,3], [4, 5, 6], [7, 8, 9]]
    matrix1 = [[5,1,9,11], [2,4,8,10], [13,3,6,7],[15,14,12,16]]
    target = 9
    breakpoint()
    lc = LeeCode()
    #print(lc.sumTwo(num_list, target))
    #lc.rotateImag(matrix1)
    lc.threeSum(matrix1)
    print(matrix1)
    print(lc.twosum(num_list, target))

    print(lc.reverseint(-123456789))

    num = [-1,0,1,2,-1,-4, 3, -1, -1]
    #print(lc.threeSum(num))

    #print(len(lc.letterCombinations1('12')))
if __name__ == '__main__':
    main()